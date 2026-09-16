# everyday

Countries and the facts about them that do not change from one year to the next: capital, currency, official languages, country codes, calling code, and which part of the world they are in.

## Rebuilding

```
curl -s -G https://query.wikidata.org/sparql \
  --data-urlencode query@countries.rq \
  -H "Accept: application/sparql-results+json" \
  -H "User-Agent: ai2-knowledge-pack-builder/0.1 (https://github.com/ProWoos-Devs/ai-2; your email)" \
  -o countries.json
python3 render.py                       # writes entries/ and prints what to check
ai-2 doc index --in everyday entries/*.txt
ai-2 knowledge export everyday --manifest manifest.yml -o everyday.ai2pack
```

The query asks only for statements that are not deprecated and have no end date, which is the difference between "Zimbabwe uses the euro" and something publishable.

## What to check before publishing

`render.py` prints every entry that needs a human. On the 2026-09-16 snapshot that was 28 of 196: countries with more than one currency in circulation, countries whose official languages in Wikidata are those of their territories, and a few with no capital in the data.

Sanity rules that should hold on any rebuild:

- between 190 and 210 countries
- every entry has a name and an ISO 3166-1 alpha-2 code, and no code appears twice
- no entry contains an unresolved Wikidata id (a bare `Q` followed by digits)
- the number of entries has not moved by more than a few since the last release

A change such as a country's capital moving is a reason to stop and look, not to publish.

## Measured

196 entries, 9,733 words, a 580 KB pack. Questions that name the country ("What money do they use in Japan?") were answered 15 times out of 15, the right entry first, even with 2,400 parts of unrelated documentation in the same search. Questions that do not name it ("Which country uses the yen?") were answered 8 times out of 10 by meaning alone and 9 times out of 10 by keyword search, failing different ones, which is why a facts pack wants both.
