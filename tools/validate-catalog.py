#!/usr/bin/env python3
"""Check the catalog files: every entry complete, licences redistributable,
ids unique, hashes the right shape. With --fetch it also downloads each pack
and checks its size and SHA-256, which is what CI does on a pull request.

  python3 tools/validate-catalog.py [--fetch] [catalog/community.yml ...]
"""
import hashlib
import re
import sys
import urllib.request

import yaml

REQUIRED = ("id", "title", "version", "languages", "license", "embedder", "url",
            "size_bytes", "sha256", "documents", "parts")
# Redistribution allowed, and any attribution the licence wants goes in the
# manifest, where AI-2 prints it with every answer. Non-commercial and
# no-derivatives licences are not here on purpose.
LICENCES = {"CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "CC-BY-SA-3.0", "CC-BY-SA-2.5", "CC-BY-3.0",
            "MIT", "Apache-2.0", "GFDL-1.3-or-later", "public-domain", "PSF-2.0", "OGL-3.0"}
ID = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
SHA = re.compile(r"^[0-9a-f]{64}$")
ATTRIBUTION_NEEDED = ("CC-BY", "GFDL", "PSF", "OGL", "MIT", "Apache")


def check(path: str, fetch: bool) -> list[str]:
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
            problems += fetch_check(where, p)
    return problems


def fetch_check(where: str, p: dict) -> list[str]:
    print(f"  downloading {p['url']}", flush=True)
    h = hashlib.sha256()
    size = 0
    try:
        with urllib.request.urlopen(p["url"], timeout=300) as r:
            for block in iter(lambda: r.read(1 << 20), b""):
                h.update(block)
                size += len(block)
    except OSError as exc:
        return [f"{where}: cannot download ({exc})"]
    out = []
    if size != p["size_bytes"]:
        out.append(f"{where}: {size} bytes, the entry says {p['size_bytes']}")
    if h.hexdigest() != p["sha256"]:
        out.append(f"{where}: sha256 is {h.hexdigest()}, the entry says {p['sha256']}")
    return out


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    fetch = "--fetch" in sys.argv
    problems = []
    for path in args or ["catalog/official.yml", "catalog/community.yml"]:
        problems += check(path, fetch)
    for line in problems:
        print("error:", line)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
