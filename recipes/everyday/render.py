#!/usr/bin/env python3
"""Turn the Wikidata rows into short entries, one file per country, by the
rules decided in ai2-knowledge#1, and write the list of entries a person
should read before the pack is published.

  python3 render.py [countries.json]

The query has already dropped statements that have an end date, are
deprecated, or carry "applies to part" (P518), which is what separates a
country-wide fact from a regional one. Here: keep preferred-rank values when
a country has any, list every remaining official language rather than
choosing between them, keep multi-currency wording neutral rather than
inventing a main currency, drop values that are not currencies (by type, plus
a small deny-list for the ones Wikidata types wrongly), fall back to the
inverse capital property only when exactly one city claims it, and check the
invariants that catch a bad snapshot.
"""
import collections
import json
import os
import re
import sys
import urllib.parse
import urllib.request

# Values Wikidata types as a currency that are not one. Each carries a reason,
# so the next person can check whether it is still true.
DENY_CURRENCY = {
    "Q134397947": "Ghana Pesewa is a denomination of the cedi, not a currency",
    "Q572213": "East Timor centavo coins are coins issued alongside the US dollar",
    "Q1573250": "Unidad de Fomento is an inflation-indexed unit of account, not money",
}
# Labels missing from Wikidata in English. Each carries a reason and is
# flagged on every run, so a fix upstream is noticed rather than shadowed.
LABEL_FIX = {
    "Q4916": ("euro", "the euro's English label is missing from Wikidata (207 other languages have one), checked 2026-09-16"),
    "Q36262": ("Saint John's", "the English label of Antigua and Barbuda's capital is missing from Wikidata "
                               "(116 other languages have one, its English description reads \"capital and largest "
                               "city of Antigua and Barbuda\"), checked 2026-09-16"),
}
# Countries where every value of a property carries "applies to part" and the
# parts together are the country, so dropping them would leave the entry
# silent about a fact everyone knows. Each carries a reason.
INCLUDE_PART = {
    ("Q31", "langs"): "Belgium's three official languages are modelled per language community, and the "
                      "communities together are the country",
    ("Q865", "curs"): "Taiwan's currency statement is qualified by part, and it is the only one",
}
# Country names that take "the" in a sentence.
THE = {"United States", "United Kingdom", "Netherlands", "Kingdom of the Netherlands", "Bahamas",
       "Gambia", "Philippines", "Czech Republic", "Democratic Republic of the Congo",
       "Republic of the Congo", "Comoros", "Maldives", "Marshall Islands", "Solomon Islands",
       "United Arab Emirates", "Central African Republic", "Dominican Republic", "Seychelles",
       "Vatican City", "Ivory Coast"}
QID = re.compile(r"^Q\d+$")
PREFERRED = "http://wikiba.se/ontology#PreferredRank"


def the(name: str) -> str:
    return f"the {name}" if name in THE else name


def The(name: str) -> str:
    return f"The {name}" if name in THE else name


def stop(text: str) -> str:
    """One full stop, even after "Washington, D.C."."""
    return text if text.endswith(".") else text + "."


def resolve(ids: set[str]) -> dict[str, str]:
    """English labels for the few ids the query's label service left raw."""
    out: dict[str, str] = {}
    ordered = sorted(ids)
    for i in range(0, len(ordered), 50):
        url = ("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=labels"
               "&languages=en&ids=" + urllib.parse.quote("|".join(ordered[i:i + 50])))
        req = urllib.request.Request(url, headers={
            "User-Agent": "ai2-knowledge-pack-builder/0.1 (https://github.com/ProWoos-Devs/ai-2)"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
        for qid, entity in (data.get("entities") or {}).items():
            label = (entity.get("labels") or {}).get("en", {}).get("value")
            if label:
                out[qid] = label
    return out


def group(rows: list[dict]) -> dict:
    """Per country: the plain fields, and per value its ranks and extras."""
    out = collections.defaultdict(lambda: {
        "name": None, "caps": set(), "capOf": set(), "iso2": set(), "iso3": set(),
        "cont": set(), "call": set(),
        "langs": collections.defaultdict(lambda: {"label": None, "ranks": set()}),
        "curs": collections.defaultdict(lambda: {"label": None, "ranks": set(), "codes": set(), "types": set()}),
    })
    for r in rows:
        val = lambda key: r[key]["value"] if key in r else None       # noqa: E731
        c = out[r["c"]["value"].rsplit("/", 1)[1]]
        c["name"] = c["name"] or val("cLabel")
        for key, field in (("capLabel", "caps"), ("capOfLabel", "capOf"), ("iso2", "iso2"),
                           ("iso3", "iso3"), ("contLabel", "cont"), ("callCode", "call")):
            if val(key):
                c[field].add(val(key))
        if val("lang"):
            lang = c["langs"][val("lang").rsplit("/", 1)[1]]
            lang["label"] = lang["label"] or val("langLabel")
            lang["ranks"].add(val("langRank"))
            lang["part"] = lang.get("part", True) and bool(val("langPart"))
        if val("cur"):
            cur = c["curs"][val("cur").rsplit("/", 1)[1]]
            cur["label"] = cur["label"] or val("curLabel")
            cur["ranks"].add(val("curRank"))
            cur["part"] = cur.get("part", True) and bool(val("curPart"))
            if val("curCode"):
                cur["codes"].add(val("curCode"))
            if val("curTypeLabel"):
                cur["types"].add(val("curTypeLabel"))
    return out


def national(values: dict, qid: str, field: str, flags: list[str], name: str) -> list[tuple[str, dict]]:
    """The values that hold for the whole country: those without an "applies
    to part" qualifier, then the preferred-rank ones when there are any. A
    country in INCLUDE_PART keeps its part-qualified values, with the reason
    recorded on every run."""
    items = [(k, v) for k, v in values.items() if not v.get("part")]
    if not items and values and (qid, field) in INCLUDE_PART:
        items = list(values.items())
        flags.append(f"{qid} {name}: every value is qualified by part, kept because "
                     f"{INCLUDE_PART[(qid, field)]} - recheck")
    preferred = [(k, v) for k, v in items if PREFERRED in v["ranks"]]
    return preferred or items


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else "countries.json"
    rows = json.load(open(path, encoding="utf-8"))["results"]["bindings"]
    countries = group(rows)

    raw = {v for c in countries.values()
           for v in list(c["caps"]) + list(c["capOf"])
           + [x["label"] for x in c["langs"].values() if x["label"]]
           + [x["label"] for x in c["curs"].values() if x["label"]]
           if v and QID.match(v)}
    labels = resolve(raw) if raw else {}
    flags: list[str] = []
    for qid in sorted(raw):
        if qid not in labels and qid in LABEL_FIX:
            labels[qid] = LABEL_FIX[qid][0]
            flags.append(f"{qid}: written as {LABEL_FIX[qid][0]!r} because {LABEL_FIX[qid][1]} - recheck")
        elif qid not in labels:
            flags.append(f"{qid}: no English label in Wikidata and no override, the id is in the text - fix")
    label_of = lambda v: labels.get(v, v) if v and QID.match(v) else v      # noqa: E731

    os.makedirs("entries", exist_ok=True)
    written = 0
    iso_seen: dict[str, str] = {}
    for qid, c in sorted(countries.items(), key=lambda kv: kv[1]["name"] or ""):
        name = label_of(c["name"])
        iso2, iso3 = sorted(c["iso2"]), sorted(c["iso3"])
        if not name or QID.match(name) or not iso2:
            flags.append(f"{qid} {name or '?'}: no name or no ISO 3166-1 code, left out")
            continue
        for code in [iso2[0]] + ([iso3[0]] if iso3 else []):
            if code in iso_seen:
                flags.append(f"{qid} {name}: ISO code {code} is also claimed by {iso_seen[code]} - check")
            else:
                iso_seen[code] = name

        lines = [name, ""]
        caps = sorted(label_of(x) for x in c["caps"])
        if not caps:
            inverse = sorted(label_of(x) for x in c["capOf"])
            if len(inverse) == 1:
                caps = inverse
            elif inverse:
                # Naming them beats saying nothing: these countries really do
                # have more than one capital, and the flag keeps it reviewed.
                caps = inverse
                flags.append(f"{qid} {name}: no single capital; {len(inverse)} cities claim to be one "
                             f"({', '.join(inverse)}), written as several - check")
            else:
                flags.append(f"{qid} {name}: no capital in the data - check")
        if len(caps) == 1:
            lines.append(stop(f"The capital of {the(name)} is {caps[0]}"))
        elif caps:
            lines.append(stop(f"{The(name)} has more than one capital: {', '.join(caps)}"))

        curs = []
        for cid, cur in national(c["curs"], qid, "curs", flags, name):
            if cid in DENY_CURRENCY:
                continue
            if cur["types"] and not any("currency" in t.lower() for t in cur["types"]):
                continue
            curs.append((label_of(cur["label"]), sorted(cur["codes"])))
        curs.sort()
        if len(curs) == 1:
            code = f" ({curs[0][1][0]})" if curs[0][1] else ""
            lines.append(stop(f"The currency used in {the(name)} is the {curs[0][0]}{code}"))
        elif curs:
            lines.append(stop(f"Several currencies are in use in {the(name)}, including "
                              + ", ".join(n for n, _ in curs)))
            flags.append(f"{qid} {name}: {len(curs)} currencies in circulation "
                         f"({', '.join(n for n, _ in curs)}) - check")

        langs = sorted(label_of(lang["label"]) for _, lang in national(c["langs"], qid, "langs", flags, name)
                       if lang["label"])
        if len(langs) == 1:
            lines.append(stop(f"The official language of {the(name)} is {langs[0]}"))
        elif langs:
            lines.append(stop(f"{The(name)} has {len(langs)} official languages: " + ", ".join(langs)))

        if not curs:
            flags.append(f"{qid} {name}: no country-wide currency in the data, the entry says nothing "
                         "about money - check")
        if not langs and c["langs"]:
            flags.append(f"{qid} {name}: every official language in the data is region-specific, the entry "
                         "says nothing about language - check")
        conts = sorted(label_of(x) for x in c["cont"])
        if len(conts) == 1:
            lines.append(stop(f"{The(name)} is in {conts[0]}"))
        elif conts:
            lines.append(stop(f"{The(name)} lies in more than one part of the world: " + ", ".join(conts)))
        lines.append(f"Its country code is {iso2[0]} (two letters) or {iso3[0]} (three letters)."
                     if iso3 else f"Its country code is {iso2[0]}.")
        if c["call"]:
            lines.append(f"To telephone {the(name)} from abroad, dial {sorted(c['call'])[0]}.")

        fn = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()
        open(os.path.join("entries", fn + ".txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
        written += 1

    if not 190 <= written <= 210:
        flags.append(f"INVARIANT: {written} countries written, expected between 190 and 210")
    open("flags.txt", "w", encoding="utf-8").write("\n".join(flags) + "\n")
    words = sum(len(open("entries/" + f, encoding="utf-8").read().split()) for f in os.listdir("entries"))
    print(f"{written} entries written, {words} words")
    print(f"{len(flags)} flagged for review, written to flags.txt:")
    for f in flags:
        print("  ", f)
    return 0


if __name__ == "__main__":
    sys.exit(main())
