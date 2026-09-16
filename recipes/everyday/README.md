# everyday

Countries and the facts about them that do not change from one year to the next: capital, currency, official languages, country codes, calling code, and which part of the world they are in.

## Rebuilding

```
curl -s -G https://query.wikidata.org/sparql \
  --data-urlencode query@countries.rq \
  -H "Accept: application/sparql-results+json" \
  -H "User-Agent: ai2-knowledge-pack-builder/0.1 (https://github.com/ProWoos-Devs/ai-2; your email)" \
  -o countries.json
python3 render.py countries.json        # writes entries/ and flags.txt
ai-2 doc index --in everyday entries/*.txt
ai-2 knowledge export everyday --manifest manifest.yml -o everyday.ai2pack
```

The query asks only for statements that are not deprecated and have no end date, which is the difference between "Zimbabwe uses the euro" and something publishable.

## The rules (ai2-knowledge#1)

Statements are filtered in the query: current (no end date) and not deprecated. "Applies to part" (P518) travels with the row, and the renderer drops those values, which is what separates a country-wide fact from a regional one. Spain keeps Spanish and drops Galician, Basque, Catalan and Occitan; the United States, whose only official-language statements are those of its territories, ends with no language line, which is right.

Two countries would be left silent by that rule and carry an override with a reason: Belgium, whose three official languages are modelled per language community, and Taiwan, whose only currency statement is part-qualified. Both are re-flagged on every run.

Where a country has several values after filtering, all of them are listed (South Africa's 12 official languages, Taiwan's 22) rather than choosing between them, and multi-currency wording stays neutral, "Several currencies are in use in X, including ...", because P38 does not say which one people use daily.

Values that are not currencies are dropped by type, plus a small deny-list for the ones Wikidata types wrongly (Ghana Pesewa, East Timor centavo coins, Unidad de Fomento), each with its reason. Labels missing from Wikidata in English get an override with a reason and a flag (the euro and Saint John's both had none on 2026-09-16).

The capital comes from P36; when a country has none of its own, the inverse property P1376 is used, and a country with several capitals gets them all named (South Africa, Bolivia, Sri Lanka).

## What to check before publishing

`render.py` writes every entry that needs a human to `flags.txt`. On the 2026-09-16 snapshot that was 22 of 196, all of them real: seven countries with several currencies in circulation, seven with more than one capital, the two label overrides, the two part-qualified overrides, two entities that are not countries for our purpose, the United States with no official language, and the Kingdom of the Netherlands with no currency of its own in the data (its facts sit on the constituent country).

Sanity rules that should hold on any rebuild:

- between 190 and 210 countries
- every entry has a name and an ISO 3166-1 alpha-2 code, and no code appears twice
- no entry contains an unresolved Wikidata id (a bare `Q` followed by digits)
- the number of entries has not moved by more than a few since the last release

A change such as a country's capital moving is a reason to stop and look, not to publish.

## Measured

196 entries, 9,733 words, a 580 KB pack. An outside question set of 20 (written by someone who had not read the entries) was answered 20 times out of 20 with the right entry first, 17 direct questions and 3 reverse ones. An earlier in-house set of 10 reverse questions scored 8 of 10 by meaning alone and 9 of 10 by keyword search, failing different ones, which is why a facts pack wants both.
