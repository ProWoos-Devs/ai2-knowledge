#!/usr/bin/env python3
"""Render the Wikidata country rows as short prose entries, one file per
country, with rules rather than a template, and flag what a human should read
before publishing."""
import collections, json, os, re, sys

rows = json.load(open("countries2.json"))["results"]["bindings"]
by = collections.defaultdict(lambda: collections.defaultdict(set))
for r in rows:
    qid = r["c"]["value"].rsplit("/", 1)[1]
    for k, v in r.items():
        if k != "c":
            by[qid][k].add(v["value"])

def clean(values):
    """Drop unresolved ids (a label the query service did not resolve)."""
    return sorted(v for v in values if not re.fullmatch(r"Q\d+", v))

out = "entries"
os.makedirs(out, exist_ok=True)
flags = []
written = 0
for qid, f in sorted(by.items(), key=lambda kv: sorted(kv[1].get("cLabel", {"?"}))[0]):
    name = (clean(f.get("cLabel", [])) or ["?"])[0]
    caps, curs, codes = clean(f.get("capLabel", [])), clean(f.get("curLabel", [])), sorted(f.get("curCode", []))
    langs, conts = clean(f.get("langLabel", [])), clean(f.get("contLabel", []))
    iso2, iso3 = sorted(f.get("iso2", [])), sorted(f.get("iso3", []))
    call = sorted(f.get("callCode", []))
    if name == "?" or not iso2:
        flags.append(f"{qid} {name}: no name or no ISO code, skipped")
        continue
    lines = [name, ""]
    if caps:
        lines.append(f"The capital of {name} is {caps[0]}." if len(caps) == 1
                     else f"{name} has more than one capital: {', '.join(caps)}.")
    if curs:
        money = f"{curs[0]}" + (f" ({codes[0]})" if len(codes) == 1 else "")
        lines.append(f"The currency of {name} is the {money}." if len(curs) == 1 else
                     f"Several currencies are in use in {name}, among them {', '.join(curs[:4])}.")
    if langs:
        lines.append(f"The official language of {name} is {langs[0]}." if len(langs) == 1 else
                     f"{name} has more than one official language, among them {', '.join(langs[:4])}.")
    if conts:
        lines.append(f"{name} is in {conts[0]}." if len(conts) == 1 else
                     f"{name} lies in more than one part of the world: {', '.join(conts)}.")
    if iso2 and iso3:
        lines.append(f"Its country code is {iso2[0]} (two letters) or {iso3[0]} (three letters).")
    if call:
        lines.append(f"To telephone {name} from abroad, dial {call[0]}.")
    if len(langs) > 4:
        flags.append(f"{qid} {name}: {len(langs)} official languages listed ({', '.join(langs[:6])}) - check")
    if len(curs) > 1:
        flags.append(f"{qid} {name}: {len(curs)} currencies listed ({', '.join(curs[:6])}) - check")
    if not caps:
        flags.append(f"{qid} {name}: no capital in the data - check")
    fn = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()
    open(os.path.join(out, fn + ".txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    written += 1
print(f"{written} entries written,", sum(len(open(f'{out}/{f}').read().split()) for f in os.listdir(out)), "words")
open("flags.txt", "w", encoding="utf-8").write("\n".join(flags) + "\n")
print(f"{len(flags)} flagged for review, written to flags.txt:")
for f in flags:
    print("  ", f)
