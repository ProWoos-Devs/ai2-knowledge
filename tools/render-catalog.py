#!/usr/bin/env python3
"""Write the table of packs in README.md from catalog/community.yml.

The README is the page people land on when AI-2 says "get packs here", so the
list there has to be the catalog, not somebody's memory of it. The table sits
between two marker comments and this script rewrites what is between them.

  python3 tools/render-catalog.py           rewrite the table
  python3 tools/render-catalog.py --check   fail if the table is out of date (CI)
"""
import sys

import yaml

START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"


def size(n: int) -> str:
    return f"{n / 1_048_576:.1f} MB" if n >= 1_048_576 else f"{max(1, n // 1024)} KB"


def cell(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def table(packs: list[dict]) -> str:
    rows = ["| Pack | What is in it | Made by | Language | Size | License | File |",
            "|---|---|---|---|---|---|---|"]
    for p in sorted(packs, key=lambda p: p["id"]):
        rows.append("| `{id}` | {what} | {by} | {langs} | {size} | {lic} | [download]({url}) |".format(
            id=cell(p["id"]), what=cell(p.get("description") or p["title"]),
            by="[{0}](https://github.com/{0})".format(cell(p["contact"])),
            langs=cell(", ".join(p["languages"])), size=size(int(p["size_bytes"])),
            lic=cell(p["license"]), url=p["url"]))
    return "\n".join(rows)


def main() -> int:
    packs = (yaml.safe_load(open("catalog/community.yml", encoding="utf-8")) or {}).get("packs") or []
    readme = open("README.md", encoding="utf-8").read()
    if readme.count(START) != 1 or readme.count(END) != 1:
        print(f"error: README.md needs exactly one {START} and one {END}")
        return 1
    head, rest = readme.split(START)
    _, tail = rest.split(END)
    wanted = f"{head}{START}\n{table(packs)}\n{END}{tail}"
    if wanted == readme:
        print(f"README.md lists the catalog's {len(packs)} pack(s)")
        return 0
    if "--check" in sys.argv:
        print("error: the table in README.md is not the catalog. Run  python3 tools/render-catalog.py  and commit.")
        return 1
    open("README.md", "w", encoding="utf-8").write(wanted)
    print(f"README.md rewritten with {len(packs)} pack(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
