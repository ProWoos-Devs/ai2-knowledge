#!/usr/bin/env python3
"""Give a pack built before ai-2 0.18.6 its paragraphs back, without touching a
single vector.

Until 0.18.6 a part was stored as its words joined by spaces, so every document
read back as one unbroken block. 0.18.6 keeps a blank line where a paragraph
began, and embeds the text with those breaks taken out, which is exactly the
old text. So an old pack and a new one differ only in the stored text, and a
pack can be brought up to date from its sources with no embedding at all:

  python3 tools/restore-paragraphs.py OLD.ai2pack NEW.ai2pack SOURCES_DIR [...]

For every document it re-cuts the source with the current chunker and requires
the result, breaks removed, to equal what the pack already stores, part for
part. Only then is the text replaced. A document whose source has drifted is
left exactly as it was and named, so nothing is ever guessed. The vectors are
the published ones, byte for byte, which is why every retrieval measurement
made on the old pack still stands for the new one.

The manifest gets the new index checksum, `revision` raised by one and today's
`version`; everything else is carried over. Needs the `ai2` package (0.18.6+).
"""
import hashlib
import os
import shutil
import sqlite3
import sys
import tempfile
import time
import zipfile

import yaml


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    from ai2 import doc
    old_pack, new_pack, source_dirs = sys.argv[1], sys.argv[2], sys.argv[3:]
    sources = {}
    for d in source_dirs:
        for name in os.listdir(d):
            sources.setdefault(name, os.path.join(d, name))

    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(old_pack) as z:
            z.extract("index.sqlite", tmp)
            manifest = yaml.safe_load(z.read("manifest.yml"))
        index = os.path.join(tmp, "index.sqlite")
        conn = sqlite3.connect(index)
        before = hashlib.sha256(b"".join(r[0] for r in conn.execute("SELECT vec FROM chunks ORDER BY id"))).hexdigest()
        restored = left = broken_parts = 0
        for doc_id, name in conn.execute("SELECT id, name FROM docs ORDER BY name").fetchall():
            stored = conn.execute("SELECT id, text FROM chunks WHERE doc_id = ? ORDER BY ord", (doc_id,)).fetchall()
            path = sources.get(name)
            if path is None:
                print(f"  left as it was, no source found:        {name}")
                left += 1
                continue
            pages, paged = doc.extract_pages(path)
            # a counter of 0 never splits a part; if the original had been
            # split to fit the model, the comparison below fails and says so
            texts, _, _ = doc.make_chunks(pages, paged, lambda c: 0, limit=1 << 30)
            if [doc.flat(t) for t in texts] != [doc.flat(t) for _, t in stored]:
                print(f"  left as it was, the source has changed: {name}")
                left += 1
                continue
            for (chunk_id, _), text in zip(stored, texts):
                conn.execute("UPDATE chunks SET text = ? WHERE id = ?", (text, chunk_id))
                broken_parts += doc.PARAGRAPH in text
            restored += 1
        conn.commit()
        after = hashlib.sha256(b"".join(r[0] for r in conn.execute("SELECT vec FROM chunks ORDER BY id"))).hexdigest()
        conn.execute("VACUUM")
        conn.close()
        assert before == after, "a vector changed, which this tool must never do"

        manifest["revision"] = int(manifest.get("revision", 1)) + 1
        manifest["version"] = time.strftime("%Y-%m-%d")
        manifest["index"]["sha256"] = hashlib.sha256(open(index, "rb").read()).hexdigest()
        with open(os.path.join(tmp, "manifest.yml"), "w", encoding="utf-8") as fh:
            yaml.safe_dump(manifest, fh, allow_unicode=True, sort_keys=False)
        out_tmp = os.path.join(tmp, "out.ai2pack")
        with zipfile.ZipFile(out_tmp, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(os.path.join(tmp, "manifest.yml"), "manifest.yml")
            z.write(index, "index.sqlite")
        shutil.move(out_tmp, new_pack)

    print(f"{manifest['id']}: {restored} document(s) restored, {left} left as they were, "
          f"{broken_parts} part(s) now carry a paragraph break; every vector unchanged "
          f"(sha256 of all vectors {after[:12]}...). Revision {manifest['revision']}, "
          f"{os.path.getsize(new_pack)} bytes.")
    return 0 if left == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
