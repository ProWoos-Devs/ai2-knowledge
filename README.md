# AI-2 knowledge packs

A knowledge pack is a set of documents that an [AI-2](https://github.com/ProWoos-Devs/ai-2) machine can search and answer from, offline, with the source of every answer named. One file holds the documents and the search index, so the slow part, indexing, happens on a fast computer and an old laptop only has to read the result.

```
ai-2 knowledge list                      what is installed here
ai-2 knowledge install FILE.ai2pack      add one
ai-2 doc search "how do I find a big file?"   ask, and get passages with their source
```

This repository holds three things: the recipes that build the official packs, the catalog of packs that AI-2 can install by name, and the rules for contributing one of your own.

## What is inside a pack

A `.ai2pack` file is a zip with exactly two members.

- `index.sqlite`, the documents cut into parts of about 110 words, each part stored with its text, its page or position, and the vector that makes it findable.
- `manifest.yml`, which says what the pack is: id, version, title, languages, licence, attribution, what was changed from the original, the sources with their URLs, the embedding model with the SHA-256 of its file, and the SHA-256 of the index.

The embedding model matters. Vectors only compare with vectors made by the same model, so a pack names the model it was built with, and AI-2 refuses a pack built with anything it does not have in its catalog.

## Building a pack

You need AI-2 (or the `ai-2` tool from its repository) and enough patience for the indexing, which runs at a few parts per second on an old machine and much faster on a recent one.

1. **Collect the text.** Plain text files, one per document, or PDFs. What the documents say matters more than how many there are.
2. **Index them into a collection.**
   ```
   ai-2 doc index --in mypack /path/to/*.txt
   ```
3. **Write a manifest** with the descriptive fields (see `recipes/everyday/manifest.yml` for a complete one).
4. **Export the pack.**
   ```
   ai-2 knowledge export mypack --manifest manifest.yml -o mypack.ai2pack
   ```
5. **Try it** on another machine: `ai-2 knowledge install mypack.ai2pack`, then ask it the ten questions you most expect people to ask.

### What makes a pack answer well, measured

These are not style preferences. They come from measurements recorded in the AI-2 project (2026-09-15 and 2026-09-16), on Spanish legal prose, Python documentation, manual pages and Wikidata-derived facts.

- **Write for the question, not for the reference shelf.** Topics phrased as tasks ("How do I stop a program that has frozen?") answered 15 of 15 questions asked in everyday words. The Python documentation, which is written as reference, answered 6 of 14 of the equivalent questions. The same machinery, very different text.
- **Keep a part self-contained.** A part is about 110 words. If the answer only makes sense together with the heading three screens above it, it will be retrieved without that heading.
- **Say the thing, then explain it.** The first sentence of a part is what gets matched.
- **Spell out the names people type.** A part about the złoty should also contain "zloty", and one about a code should contain the code itself. Retrieval by meaning is weak exactly where an exact string is strong.
- **Do not prefix parts with their section headings.** It was tried and it made retrieval worse, because the heading takes over the match.

## Contributing a pack

Open a pull request that adds one entry to `catalog/community.yml`. **You host the file** (a GitHub release of your own, a Hugging Face dataset, any stable HTTPS URL); this repository holds the catalog, not the bytes.

An entry looks like this:

```yaml
- id: my-pack
  title: What it is, in a few words
  version: "2026-09-16"
  languages: [en]
  license: CC-BY-4.0
  attribution: "Text from ..., used under CC BY 4.0."
  embedder: nomic-embed-text-v1.5
  url: https://example.org/my-pack.ai2pack
  size_bytes: 1234567
  sha256: <64 hex characters>
  documents: 120
  parts: 480
  revision: 1          # a whole number; raise it for every published rebuild
  built_with: ai-2 0.17.0
  contact: your GitHub handle
```

What is checked before it is merged:

- the file downloads, matches `size_bytes` and `sha256`, and installs on a clean AI-2
- a rebuild of a pack already in the catalog raises its `revision`, because AI-2 orders packs by that number and refuses an older one (a `version` string is for people to read, not for code to compare)
- the manifest inside the pack agrees with the catalog entry
- the licence allows redistribution, and the attribution the licence requires is in the manifest
- the pack is what it says it is (someone reads a few of its parts)

What is not checked: whether the contents are correct. A community pack carries no promise from this project beyond "the file is the one the entry describes". AI-2 says so where the pack is listed.

### Licences

Only content that may be redistributed. Public domain and CC0 are simplest; CC BY and CC BY-SA work if the attribution is in the manifest, where AI-2 shows it with every answer. Content under a non-commercial or no-derivatives licence cannot go in the catalog, and neither can anything you do not have the right to redistribute. Chunking and indexing count as modification, so a pack says so in its manifest.

## Official packs

Three, published as the release [packs-2026-09-16](https://github.com/ProWoos-Devs/ai2-knowledge/releases/tag/packs-2026-09-16) and listed in `catalog/official.yml`, which the signed `ai-2` package carries a copy of, so `ai-2 knowledge install ai2-help` fetches one by name. An AI-2 installed from the ISO of 2026-09-16 or later already has all three, and the embedding model they need, on the machine.

| Pack | Recipe | What is in it | Size | Licence |
|---|---|---|---|---|
| `ai2-help` | `recipes/ai2-help` | AI-2's own documentation, wiki pages plus topics written for what the wiki says only in a command table | 337 KB | MIT |
| `linux-essentials` | `recipes/linux-essentials` | Twenty everyday tasks on a Linux machine, written for AI-2 (runit, not systemd) | 125 KB | MIT |
| `everyday` | `recipes/everyday` | 196 countries with their capitals, currencies, official languages, country codes and calling codes, from [Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing) (CC0, no attribution required) | 579 KB | CC0 |

Each recipe holds what built it (a query or a topic set), the renderer where there is one, the rules and the manifest, so anyone can rebuild a pack and compare it with what was published. Measured with question sets written by someone who had not read the packs, 20 questions each, right answer first: everyday 20/20, linux-essentials 19/20, ai2-help 18/20.

Wikidata is collaboratively edited, so a rebuild of `everyday` is never published without reading the diff. Its renderer writes everything a person should check to `flags.txt`: 22 entries of 196 on the 2026-09-16 snapshot, all of them real (seven countries with several currencies in circulation, six with more than one capital, two labels Wikidata has no English word for, two part-qualified overrides, two entities that are not countries for this purpose, the United States with no federal official language, and the Kingdom of the Netherlands with no currency of its own in the data). The statement rules behind those numbers are in `recipes/everyday/README.md` and were settled in #1.

Facts that change with the world (populations, prices, who holds an office, security advice) do not go in an official pack. They are wrong the moment they are stale, and a pack shipped on an ISO can sit on a machine for years.
