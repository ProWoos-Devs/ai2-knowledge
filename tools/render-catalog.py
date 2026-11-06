#!/usr/bin/env python3
"""Write the table of packs in README.md from catalog/community.yml, sorted by
subject, with subject names from catalog/categories.yml.

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


def subject(p: dict, names: dict[str, str]) -> str:
    """The pack's main category by name, with "for children" and its ages
    when that is who it is written for."""
    code = str((p.get("categories") or [""])[0])
    text = names.get(code, code)
    if p.get("audience") == "children":
        text += ", for children (" + ", ".join(AGES.get(a, a) for a in p.get("ages") or []) + ")"
    return text


# Short forms of the age ranges in catalog/categories.yml, for a table cell.
AGES = {"infant": "under 1", "toddler": "1 to 2", "preschool": "3 to 5", "school-age": "6 to 9", "preteen": "10 to 12"}


def table(packs: list[dict], names: dict[str, str]) -> str:
    rows = ["| Pack | Subject | What is in it | Made by | Language | Size | License | File |",
            "|---|---|---|---|---|---|---|---|"]
    for p in sorted(packs, key=lambda p: (str((p.get("categories") or [""])[0]), p["id"])):
        rows.append("| `{id}` | {subject} | {what} | {by} | {langs} | {size} | {lic} | [download]({url}) |".format(
            id=cell(p["id"]), subject=cell(subject(p, names)), what=cell(p.get("description") or p["title"]),
            by="[{0}](https://github.com/{0})".format(cell(p["contact"])),
            langs=cell(", ".join(p["languages"])), size=size(int(p["size_bytes"])),
            lic=cell(p["license"]), url=p["url"]))
    return "\n".join(rows)


def main() -> int:
    packs = (yaml.safe_load(open("catalog/community.yml", encoding="utf-8")) or {}).get("packs") or []
    cats = (yaml.safe_load(open("catalog/categories.yml", encoding="utf-8")) or {}).get("categories") or []
    names = {str(c["code"]): str(c["en"]) for c in cats}
    readme = open("README.md", encoding="utf-8").read()
    if readme.count(START) != 1 or readme.count(END) != 1:
        print(f"error: README.md needs exactly one {START} and one {END}")
        return 1
    head, rest = readme.split(START)
    _, tail = rest.split(END)
    wanted = f"{head}{START}\n{table(packs, names)}\n{END}{tail}"
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
