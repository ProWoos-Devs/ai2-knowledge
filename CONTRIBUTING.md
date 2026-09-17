# Contributing a knowledge pack, step by step

A knowledge pack is one file that an AI-2 machine installs and then searches offline, naming the source of every answer. This page walks the whole way from a folder of text to a merged catalog entry. Nothing here needs permission from us until the last step, and you keep hosting your own file.

The short version for people who have done it before is in the [README](README.md). This page is the long version, written for the first time.

---

## 0. What you need

**On an AI-2 machine:** nothing. `ai-2` and the engine are already there.

**On any other Linux machine**, three things:

```bash
python3 --version                     # 3.11 or newer
pip install "ai2 @ git+https://github.com/ProWoos-Devs/ai-2@v0.18.3"
```

and a build of [llama.cpp](https://github.com/ggml-org/llama.cpp), which does the embedding. AI-2 looks for `llama-bench` and `llama-server` in `$AI2_RUNTIME_DIR`, then `/usr/lib/ai2/runtimes/llama.cpp`, then `/opt/ai2/llama`, then `~/llama`. Unpack an upstream release into `~/llama` and you are done:

```bash
ls ~/llama/llama-server ~/llama/llama-bench     # both must be there
```

The embedding model is downloaded for you the first time, with its checksum verified.

## 1. Pick content you are allowed to redistribute

This is the step that gets packs rejected, so settle it first. The catalog carries public domain, CC0, CC BY, CC BY-SA, MIT, Apache-2.0, GFDL, PSF and OGL. It cannot carry non-commercial or no-derivatives licences, and it cannot carry anything you do not have the right to redistribute, however freely it is available to read.

Indexing counts as modification, so your manifest says so. If the licence asks for attribution, it goes in the manifest, which is where AI-2 reads it from when it prints an answer.

Official packs also avoid anything that goes stale: no prices, no populations, no security advice, no "who currently holds this office". A pack can sit on a machine for two years. Community packs are not held to that, but the same logic applies to your readers.

## 2. Write or collect the text

One plain text file or PDF per document. What they say matters far more than how many there are; the three official packs are between 40 and 196 parts.

Five things are measured, not preferences, and they are the difference between a pack that answers and one that does not. They are in the [README](README.md#what-makes-a-pack-answer-well-measured); the shortest form is **write for the question, not for the reference shelf**. Topics phrased as tasks answered 15 of 15 questions asked in everyday words, while reference documentation answered 6 of 14.

## 3. Index it

```bash
ai-2 doc index --in mypack --embedder nomic-embed-text-v1.5 /path/to/*.txt
```

`--embedder` matters more than it looks. A pack can only ever be searched with the model that built it, and without the flag AI-2 picks from your machine's RAM, which on a good computer means the 345 MB multilingual model. Everyone who installs your pack would then have to download it. `nomic-embed-text-v1.5` is 85 MB and is already on every machine installed from an AI-2 ISO. Use it for anything in English. (The flag needs `ai-2` 0.18.1 or newer.)

Check what was recorded:

```bash
ai-2 doc list
```

A collection keeps the model it was built with for good, so if this is wrong, start a new collection rather than trying to change it.

## 4. Write the manifest

A YAML file with what a person should know before installing. Everything the store already knows (model, counts, checksums) is filled in for you.

```yaml
id: my-pack                 # lower-case; becomes the collection name; must be unique across both catalogs
title: What it is, in a few words
version: "2026-09-17"       # for people to read
revision: 1                 # for code to compare; raise it for every rebuild you publish
languages: [en]
license: CC-BY-4.0
attribution: "Text from ..., by ..., used under CC BY 4.0."
modified: "Split into parts of about 110 words and embedded for search by AI-2."
sources:
  - file: chapter-one       # the document name as ai-2 doc list shows it
    title: "Where this document came from"
    url: https://example.org/chapter-one
    retrieved: 2026-09-17
```

`revision` is the field people get wrong. It is the number AI-2 orders by, a `version` string cannot be compared reliably, and **the copy that counts is the one in this file**. The catalog entry repeats it, and CI fails if the two disagree.

## 5. Export the pack

```bash
ai-2 knowledge export mypack --manifest manifest.yml -o my-pack.ai2pack
```

The line it prints names the documents, the parts, the licence and the embedder it recorded. Read it. If the embedder is not the one you meant, go back to step 3; it cannot be changed afterwards.

Your file paths are not in the pack. The documents' text and the search index are.

## 6. Try it as a stranger would

On another machine, or in a throwaway home directory on this one:

```bash
XDG_DATA_HOME=$(mktemp -d) ai-2 knowledge install my-pack.ai2pack
XDG_DATA_HOME=... ai-2 doc search "the question you most expect"
```

Ask it the ten questions you expect people to ask. If the answers are poor, the fix is almost always the text, not the settings, and step 2 says how.

## 7. Host the file yourself

This repository holds the catalog, not the bytes. Any stable HTTPS URL works: a GitHub release of your own, a Hugging Face dataset, the Internet Archive. With the `gh` CLI:

```bash
gh repo create my-knowledge-pack --public
gh release create v1 --repo YOURNAME/my-knowledge-pack --title "my-pack v1" my-pack.ai2pack
gh release view v1 --repo YOURNAME/my-knowledge-pack --json assets --jq '.assets[].url'
```

Through the website instead: create a repository, Releases, Draft a new release, attach the `.ai2pack`, publish, then copy the link from the asset.

Whichever you use, the URL must serve the file itself over HTTPS, not a landing page, and it must keep working. AI-2 refuses a URL that is not HTTPS and refuses a redirect that leaves HTTPS.

## 8. Measure the file

```bash
stat -c%s my-pack.ai2pack        # size_bytes
sha256sum my-pack.ai2pack        # sha256
```

Both go in the entry, and both are checked on every download, on your pull request and on every machine that installs it.

## 9. Add your entry

Fork this repository, branch, and add one entry to `catalog/community.yml`:

```yaml
- id: my-pack
  title: What it is, in a few words
  version: "2026-09-17"
  revision: 1
  languages: [en]
  license: CC-BY-4.0
  attribution: "Text from ..., by ..., used under CC BY 4.0."
  embedder: nomic-embed-text-v1.5
  url: https://github.com/YOURNAME/my-knowledge-pack/releases/download/v1/my-pack.ai2pack
  size_bytes: 1234567
  sha256: <64 hex characters>
  documents: 120
  parts: 480
  built_with: ai-2 0.18.3
  contact: your GitHub handle
```

Check it before you push, which takes seconds and saves a round trip:

```bash
python3 tools/validate-catalog.py                       # the entry itself
python3 tools/validate-catalog.py --install             # what CI will do, if you have ai2 installed
```

## 10. Open the pull request

CI then does the whole thing for real: downloads your file, checks its size and SHA-256, **installs it with AI-2 itself**, and compares the manifest inside the installed pack against your entry, id, title, version, revision, licence, languages, embedder, and the document and part counts. It also counts the rows in the installed index and requires the attribution your licence asks for.

If it fails, the message names the field and both values. The two common ones:

- *"the catalog says revision=2, the pack says 1"*, you raised it in the entry but not in the manifest, so rebuild the pack from step 4.
- *"the catalog says embedder=... the pack was built with ..."*, step 3, and the pack has to be rebuilt.

A person then reads a few of your parts and merges it.

## Publishing a new version later

1. Raise `revision` in the manifest (and `version`, for people to read).
2. Rebuild and re-export.
3. Upload it as a new release asset; do not overwrite the old file, machines may still be fetching it.
4. Update your catalog entry: `version`, `revision`, `url`, `size_bytes`, `sha256`, and the counts if they changed.

AI-2 installs a pack whose revision is the same or higher and refuses an older one, so raising the number is what makes the update reach people.

## What this project does and does not promise

We verify that your file is the one your entry describes, that it installs, that its licence allows redistribution and that its attribution is present. **We do not check whether its contents are correct**, and AI-2 says so where community packs are listed.

Your pack is never fetched by name: `ai-2 knowledge install ID` resolves only against the official catalog that travels inside the signed `ai-2` package. People install yours from its file, and AI-2 records on their machine that it came from a file rather than from us.

If we remove your entry, nothing reaches anyone's machine. A pack already installed stays until its owner removes it.
