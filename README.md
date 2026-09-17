# AI-2 knowledge packs

A knowledge pack is a set of documents that an [AI-2](https://github.com/ProWoos-Devs/ai-2) machine can search and answer from, offline, with the source of every answer named. One file holds the documents and the search index, so the slow part, indexing, happens on a fast computer and an old laptop only has to read the result.

```
ai-2 knowledge list                      what is installed here
ai-2 knowledge install FILE.ai2pack      add one
ai-2 doc search "how do I find a big file?"   ask, and get passages with their source
```

This repository holds three things: the recipes that build the official packs, the catalog of packs that AI-2 can install by name, and the rules for contributing one of your own. To contribute a pack, follow [CONTRIBUTING.md](CONTRIBUTING.md) step by step.

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
   **Check which embedding model this used**, with `ai-2 doc list`. AI-2 picks it from the RAM of the machine doing the indexing, and a machine with enough memory picks the multilingual `nomic-embed-text-v2-moe`. A pack can only ever be searched with the model that built it, so a pack built that way makes everyone who installs it download 345 MB, while `nomic-embed-text-v1.5` is 85 MB and is already on every machine installed from an AI-2 ISO. For an English pack, build it with v1.5, which `ai-2` 0.18.1 and later take as an option:
   ```
   ai-2 doc index --in mypack --embedder nomic-embed-text-v1.5 /path/to/*.txt
   ```
   A collection keeps the model it was built with, so this is decided once, when the collection is new. On an older `ai-2`, index on a machine whose RAM puts it in the Tiny or Light tier instead; a virtual machine with 2 GB is enough.
3. **Write a manifest** with the descriptive fields (see `recipes/everyday/manifest.yml` for a complete one). It carries `revision`, a whole number, and **that is the one the code reads**: the catalog entry only repeats it. Leave it at 1 for a first release and raise it in the manifest, then in the catalog entry, for every rebuild you publish. CI compares the two and fails if they disagree.
4. **Export the pack.**
   ```
   ai-2 knowledge export mypack --manifest manifest.yml -o mypack.ai2pack
   ```
   The line it prints names the embedder it recorded. If that is not the one you meant, fix it before publishing, not after: a pack's embedder cannot be changed without indexing again.
5. **Try it** on another machine: `ai-2 knowledge install mypack.ai2pack`, then ask it the ten questions you most expect people to ask.

### What makes a pack answer well, measured

These are not style preferences. They come from measurements recorded in the AI-2 project (2026-09-15 and 2026-09-16), on Spanish legal prose, Python documentation, manual pages and Wikidata-derived facts.

- **Write for the question, not for the reference shelf.** Topics phrased as tasks ("How do I stop a program that has frozen?") answered 15 of 15 questions asked in everyday words. The Python documentation, which is written as reference, answered 6 of 14 of the equivalent questions. The same machinery, very different text.
- **Keep a part self-contained.** A part is about 110 words. If the answer only makes sense together with the heading three screens above it, it will be retrieved without that heading.
- **Say the thing, then explain it.** The first sentence of a part is what gets matched.
- **Spell out the names people type.** A part about the złoty should also contain "zloty", and one about a code should contain the code itself. Retrieval by meaning is weak exactly where an exact string is strong.
- **Do not prefix parts with their section headings.** It was tried and it made retrieval worse, because the heading takes over the match.

## Contributing a pack

**First time? [CONTRIBUTING.md](CONTRIBUTING.md) walks the whole way**, from a folder of text to a merged entry, including how to host the file yourself and what to do when CI complains. The rest of this section is the summary.

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
  revision: 1          # required; the number the code orders by, and the manifest's copy is the one that counts
  built_with: ai-2 0.17.0
  contact: your GitHub handle
```

Checked by CI on the pull request, with `tools/validate-catalog.py --install`:

- the entry is complete, the licence is one this catalog carries, and the `id` is not already taken by any other pack in either catalog (ids are global, so a community pack can never be installed in place of an official one)
- the file downloads over HTTPS and matches `size_bytes` and `sha256`, the download stopping the moment it outgrows the declared size
- **AI-2 itself installs the downloaded file** on a clean machine, at the pinned version the workflow names, and then the manifest inside the installed pack is compared with the catalog entry, id, title, version, revision, licence, languages, embedder, document and part counts. The hash only proves the bytes are the ones the entry described; this is what proves the description true
- the installed index really holds the number of parts the manifest claims
- the attribution the licence requires is in the manifest, which is where AI-2 reads it from when it prints an answer, and for Apache-2.0 and GFDL the licence text is inside the pack as a document, because those two require the recipient to receive the licence itself

Checked by a person:

- a rebuild of a pack already in the catalog raises its `revision`, because AI-2 orders packs by that number and refuses an older one (a `version` string is for people to read, not for code to compare)
- the pack is what it says it is (someone reads a few of its parts)
- a GFDL pack is read for the obligations the tooling cannot describe (invariant sections, history, a transparent copy); if the content is available under another licence on the list, that is the easier road

What is not checked: whether the contents are correct, and whether you have met your licence's obligations, which remain yours. A community pack carries no promise from this project beyond "the file is the one the entry describes". AI-2 says so where the pack is listed.

### Where the trust boundary is

Official and community packs are not treated the same by the tool, and the difference is deliberate.

- `ai-2 knowledge install ID` resolves a name **only** against the official catalog, a copy of which travels inside the signed `ai-2` package, so the SHA-256 it checks against is covered by the repository key. A community pack is never fetched by name.
- A community pack is installed from its file, which the person fetched themselves. AI-2 records where every installed pack came from and prints it in `ai-2 knowledge list`, so "this came from the official catalog" and "this came from a file" stay distinguishable on the machine long after the install.
- Nothing updates itself. `ai-2 knowledge available` says when a newer revision exists; installing it is a decision a person makes.
- Removing an entry from this catalog stops new installs. It does not reach onto anyone's machine: a pack already installed stays until its owner runs `ai-2 knowledge remove`. A distro that can delete a user's documents from a repository edit is not one we want to ship.

### Licences

Only content that may be redistributed, and **a licence being on the list is not the same as its obligations being met**. Public domain and CC0 are simplest; CC BY and CC BY-SA work with the attribution in the manifest, where AI-2 shows it with every answer. Apache-2.0 and GFDL require the recipient to receive the licence itself, so those packs carry its text as a document, and a GFDL pack is read by a person for the rest. MIT, PSF and OGL require their notice to be preserved, which for content that is not yours means carrying it in the pack. Non-commercial and no-derivatives licences cannot go in the catalog, and neither can anything you do not have the right to redistribute. Chunking and indexing count as modification, so a pack says so in its manifest. The per-licence detail is in [CONTRIBUTING.md](CONTRIBUTING.md#1-pick-content-you-are-allowed-to-redistribute).

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
