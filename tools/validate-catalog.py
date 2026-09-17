#!/usr/bin/env python3
"""Check the catalog files.

Three layers, each stricter than the last:

  (none)     every entry complete, licences redistributable, ids unique across
             both catalogs, hashes the right shape
  --fetch    download each pack and check its size and SHA-256
  --install  install the downloaded pack with AI-2 itself and compare the
             manifest inside it against what the catalog entry claims

The third layer is the one that matters for a contributed pack: the hash only
proves the bytes are the ones the entry described, not that the entry
describes them truthfully. It needs the `ai2` package importable.

CI installs **v0.18.0 on purpose**, which is the oldest released ai-2 that
understands a pack's `revision`, so the check answers "does this artifact
install on the oldest AI-2 that knows about packs as they are now", not merely
"does it install here". Contributors build with a newer one (0.18.1 added
`ai-2 doc index --embedder`); that difference is the point, not an oversight.
Raise this baseline only when a pack-format change makes an older AI-2 unable
to install a current pack at all.

  pip install "ai2 @ git+https://github.com/ProWoos-Devs/ai-2@v0.18.0"

  python3 tools/validate-catalog.py [--fetch] [--install] [catalog/*.yml]
"""
import hashlib
import os
import re
import sqlite3
import sys
import tempfile
import urllib.request

import yaml

REQUIRED = ("id", "title", "version", "revision", "languages", "license", "embedder", "url",
            "size_bytes", "sha256", "documents", "parts")
# `revision` is required even though a missing one would be read as 1: it is the
# field AI-2 orders by, and a contributor who never wrote it down is a
# contributor who will forget to raise it on the next rebuild.

# Redistribution allowed, and any attribution the licence wants goes in the
# manifest, where AI-2 prints it with every answer. Non-commercial and
# no-derivatives licences are not here on purpose.
LICENCES = {"CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "CC-BY-SA-3.0", "CC-BY-SA-2.5", "CC-BY-3.0",
            "MIT", "Apache-2.0", "GFDL-1.3-or-later", "public-domain", "PSF-2.0", "OGL-3.0"}
ID = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
SHA = re.compile(r"^[0-9a-f]{64}$")
ATTRIBUTION_NEEDED = ("CC-BY", "GFDL", "PSF", "OGL", "MIT", "Apache")
# These two require the recipient to RECEIVE the licence (Apache-2.0 §4a, and
# GFDL's requirement to include a copy), which no attribution line can do. The
# pack is the distribution, so the licence text has to travel inside it as one
# of its documents. Being on this list does not make a pack compliant; it makes
# the one obligation we can check mechanically checkable.
LICENCE_TEXT_NEEDED = ("Apache-2.0", "GFDL")
LICENCE_DOC = re.compile(r"(licen[cs]e|notice|copying)", re.I)


# What the catalog entry and the pack's own manifest must agree on. Everything
# here is what a person reads before deciding to install, so a catalog that
# says one thing while the artifact says another is the failure this catches.
# `attribution` is deliberately not here: the catalog may word it more briefly
# than the pack does, and what matters (that the pack carries one at all) is
# checked below.
COMPARED = ("id", "title", "version", "license", "languages", "revision")


def check(path: str, fetch: bool, install: bool = False, seen_ids: set | None = None) -> list[str]:
    problems = []
    data = yaml.safe_load(open(path, encoding="utf-8")) or {}
    if data.get("version") != 1:
        problems.append(f"{path}: catalog version {data.get('version')!r}, expected 1")
    seen = set()
    for i, p in enumerate(data.get("packs") or []):
        where = f"{path}[{i}]"
        if not isinstance(p, dict):
            problems.append(f"{where}: not a mapping")
            continue
        where = f"{path} {p.get('id', '?')}"
        for field in REQUIRED:
            if p.get(field) in (None, "", []):
                problems.append(f"{where}: {field} is missing")
        if not ID.match(str(p.get("id", ""))):
            problems.append(f"{where}: id is not usable as a collection name")
        if p.get("id") in seen:
            problems.append(f"{where}: id appears twice")
        seen.add(p.get("id"))
        if seen_ids is not None:
            if p.get("id") in seen_ids:
                problems.append(f"{where}: id is already used by another catalog; ids are global, so a "
                                "community pack can never be mistaken for an official one")
            seen_ids.add(p.get("id"))
        if p.get("license") not in LICENCES:
            problems.append(f"{where}: licence {p.get('license')!r} is not one this catalog carries "
                            f"({', '.join(sorted(LICENCES))})")
        elif any(p["license"].startswith(k) for k in ATTRIBUTION_NEEDED) and not str(p.get("attribution", "")).strip():
            problems.append(f"{where}: {p['license']} needs an attribution line")
        if not SHA.match(str(p.get("sha256", ""))):
            problems.append(f"{where}: sha256 is not 64 hex characters")
        if not str(p.get("url", "")).startswith("https://"):
            problems.append(f"{where}: url is not https")
        if not isinstance(p.get("languages"), list):
            problems.append(f"{where}: languages is not a list")
        if fetch and not problems:
            downloaded, trouble = fetch_check(where, p)
            problems += trouble
            if install and downloaded and not trouble:
                problems += install_check(where, p, downloaded)
            if downloaded:
                os.remove(downloaded)
    return problems


class HttpsOnlyRedirect(urllib.request.HTTPRedirectHandler):
    """A redirect may not leave HTTPS. The same rule as `ai2.pack`, which is
    the source of truth; it is repeated here so the plain `--fetch` layer needs
    nothing but PyYAML, and so CI cannot be gentler than the machine it speaks
    for."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not str(newurl).lower().startswith("https://"):
            raise OSError(f"the download was redirected to {str(newurl).split(':')[0]}, which is not https")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_check(where: str, p: dict) -> tuple[str | None, list[str]]:
    """Download the pack; returns the file (for the install check) and what is
    wrong with it. The read stops once the response passes the size the entry
    declares, so a wrong URL cannot pull a hundred gigabytes into CI."""
    print(f"  downloading {p['url']}", flush=True)
    h = hashlib.sha256()
    size = 0
    limit = int(p["size_bytes"])
    fd, path = tempfile.mkstemp(suffix=".ai2pack")
    try:
        opener = urllib.request.build_opener(HttpsOnlyRedirect)
        with os.fdopen(fd, "wb") as out, opener.open(p["url"], timeout=300) as r:
            for block in iter(lambda: r.read(1 << 20), b""):
                h.update(block)
                size += len(block)
                out.write(block)
                if size > limit:
                    return None, [f"{where}: the file is larger than the entry's {limit} bytes; stopped"]
    except OSError as exc:
        os.path.exists(path) and os.remove(path)
        return None, [f"{where}: cannot download ({exc})"]
    problems = []
    if size != limit:
        problems.append(f"{where}: {size} bytes, the entry says {limit}")
    if h.hexdigest() != p["sha256"]:
        problems.append(f"{where}: sha256 is {h.hexdigest()}, the entry says {p['sha256']}")
    if problems:
        os.remove(path)
        return None, problems
    return path, []


def install_check(where: str, p: dict, path: str) -> list[str]:
    """Install the downloaded pack with AI-2 itself and compare the manifest
    inside it with the catalog entry. This is what a hash cannot do: the hash
    says the bytes are the ones described, not that the description is true."""
    try:
        from ai2 import doc, pack
    except ImportError:
        return [f"{where}: --install needs the ai2 package "
                "(pip install \"git+https://github.com/ProWoos-Devs/ai-2@v0.18.0\")"]
    before = os.environ.get("XDG_DATA_HOME")
    with tempfile.TemporaryDirectory() as home:
        os.environ["XDG_DATA_HOME"] = home          # install into a machine of its own
        try:
            collection, manifest, _ = pack.install_pack(path)
            index_file = doc.index_path(collection)     # while XDG_DATA_HOME still points here
        except pack.PackError as exc:
            return [f"{where}: AI-2 refuses this pack ({exc})"]
        finally:
            if before is None:
                os.environ.pop("XDG_DATA_HOME", None)
            else:
                os.environ["XDG_DATA_HOME"] = before
        problems = []
        for field in COMPARED:
            fallback = pack.DEFAULT_REVISION if field == "revision" else None
            claimed, actual = p.get(field, fallback), manifest.get(field, fallback)
            if claimed is not None and actual != claimed:
                problems.append(f"{where}: the catalog says {field}={claimed!r}, the pack says {actual!r}")
        # The manifest names the embedder as an id with the SHA-256 of the model
        # file; the catalog entry carries only the id, which is what a person
        # needs to know (a pack is only searchable by the model that built it).
        built_with = (manifest.get("embedder") or {}).get("id")
        if p.get("embedder") != built_with:
            problems.append(f"{where}: the catalog says embedder={p.get('embedder')!r}, "
                            f"the pack was built with {built_with!r}")
        index = manifest.get("index") or {}
        for field in ("documents", "parts"):
            if p.get(field) is not None and index.get(field) != p[field]:
                problems.append(f"{where}: the catalog says {field}={p[field]}, the pack says {index.get(field)}")
        conn = sqlite3.connect(index_file)
        rows = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        if index.get("parts") is not None and rows != index["parts"]:
            problems.append(f"{where}: the installed index holds {rows} parts, "
                            f"the manifest says {index['parts']}")
        licence = str(manifest.get("license", ""))
        if any(licence.startswith(k) for k in LICENCE_TEXT_NEEDED):
            names = [r[0] for r in conn.execute("SELECT name FROM docs")]
            if not any(LICENCE_DOC.search(n or "") for n in names):
                problems.append(f"{where}: {licence} requires the recipient to receive the licence, so the pack "
                                "must carry its text as one of its documents (a file named LICENSE, NOTICE or "
                                "COPYING). None of these is in it: " + ", ".join(names[:8]))
        if not str(manifest.get("attribution", "")).strip() and \
                any(licence.startswith(k) for k in ATTRIBUTION_NEEDED):
            problems.append(f"{where}: {manifest.get('license')} needs an attribution line in the manifest, "
                            "which is where AI-2 reads it from when it prints an answer")
        conn.close()
        print(f"  installed as {collection}: {rows} parts, {manifest.get('license')}", flush=True)
        return problems


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    fetch = "--fetch" in sys.argv or "--install" in sys.argv
    install = "--install" in sys.argv
    problems = []
    seen_ids: set = set()
    for path in args or ["catalog/official.yml", "catalog/community.yml"]:
        problems += check(path, fetch, install, seen_ids)
    for line in problems:
        print("error:", line)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
