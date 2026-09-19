# Contributing a knowledge pack, step by step

A knowledge pack is one file that an AI-2 machine installs and then searches offline, naming the source of every answer. This page walks the whole way from a folder of text to a merged catalog entry. Nothing here needs permission from us until the last step, and you keep hosting your own file.

The short version for people who have done it before is in the [README](README.md). This page is the long version, written for the first time.

---

## 0. What you need

**On an AI-2 machine:** nothing. `ai-2` and the engine are already there.

**On any other Linux machine**, Python 3.11 or newer, git, and a virtual environment. Do not install into the system Python: most current distributions refuse it (PEP 668, "externally managed environment"), and you do not want project tooling in there anyway.

```bash
python3 --version                     # 3.11 or newer
python3 -m venv ~/ai2-build
source ~/ai2-build/bin/activate
python -m pip install "ai2 @ git+https://github.com/ProWoos-Devs/ai-2@v0.18.3"
ai-2 --version                        # 0.18.3 or newer: 0.18.1 added --embedder
```

You also need [llama.cpp](https://github.com/ggml-org/llama.cpp), which is what actually computes the embeddings. **Build or download tag `b10398`**, the same one AI-2 pins.

```bash
mkdir -p ~/llama && cd ~/llama        # unpack b10398 here
ls ~/llama/llama-server ~/llama/llama-bench     # both must be there
```

AI-2 looks for those two programs in `$AI2_RUNTIME_DIR`, then `/usr/lib/ai2/runtimes/llama.cpp`, then `/opt/ai2/llama`, then `~/llama`, and takes the first directory that has them.

**Why a pinned version and not "whatever is current".** A pack stores vectors your llama.cpp produced; the question someone types later is turned into a vector by *their* AI-2's llama.cpp, and the two are compared. The manifest pins the embedding model's file by SHA-256, but nothing pins the implementation that runs it, and tokenisation or pooling changes between llama.cpp releases would degrade every answer quietly rather than failing loudly. Whether other versions are equivalent has not been measured. Until it has, build with AI-2's own runtime or with b10398, and if you deliberately use something else, say so in the manifest's `modified` line so a reviewer can weigh it.

The embedding model itself is downloaded for you the first time, with its checksum verified.

## 1. Pick content you are allowed to redistribute

This is the step that gets packs rejected, so settle it first, and read the next two paragraphs as one thought: **a license being allowed here is not the same as its obligations being met.**

**Allowed by the catalog:** public domain, CC0, CC BY, CC BY-SA, MIT, Apache-2.0, GFDL, PSF and OGL. Not allowed: non-commercial and no-derivatives licenses, and anything you do not have the right to redistribute, however freely it can be read.

**Obligations are yours, and the checks do not establish them.** CI verifies that the license is on the list above and that an attribution line exists where one is needed. That is all it can do. Real licenses ask for more, and the pack is a distribution, so the asks land on you:

- **A one-line attribution satisfies CC BY and CC BY-SA** for a pack, together with saying what was changed, which the `modified` field does.
- **Apache-2.0 and GFDL require the recipient to receive the license itself**, which no attribution line can do. So the pack must carry the license text as one of its documents, named `LICENSE`, `NOTICE` or `COPYING`, and CI now refuses these two licenses without it. For Apache-2.0, any NOTICE material from the original has to travel too.
- **GFDL asks for more still** (invariant sections, the history, a transparent copy). A GFDL pack is reviewed by a person before it is merged, and may be asked for changes the tooling cannot describe. If the content is available under any other license on the list, use that instead.
- **MIT, PSF and OGL** require their notice to be preserved. If the content is not yours, carry it in the pack the same way.

Indexing counts as modification, so your manifest says so. Attribution goes in the manifest, which is where AI-2 reads it from when it prints an answer, and it is shown with every result from your pack.

The AI-2 project's own packs avoid anything that goes stale: no prices, no populations, no security advice, no "who currently holds this office". A pack can sit on a machine for two years. Nobody holds your pack to that, but the same logic applies to your readers.

## 2. Write or collect the text

One plain text file or PDF per document. What they say matters far more than how many there are; the three packs the AI-2 project made are between 40 and 196 parts.

**A scanned PDF will not do.** AI-2 reads a PDF's text layer, and a page image has none, so the file is skipped with `no text found (a scanned PDF needs OCR: ai-2 workflow info documents)`. Run OCR first and index the text it produces.

Five things are measured, not preferences, and they are the difference between a pack that answers and one that does not. They are in the [README](README.md#what-makes-a-pack-answer-well-measured); the shortest form is **write for the question, not for the reference shelf**. Topics phrased as tasks answered 15 of 15 questions asked in everyday words, while reference documentation answered 6 of 14.

## 3. Index it

```bash
ai-2 doc index --in mypack --embedder nomic-embed-text-v1.5 /path/to/*.txt
```

`--embedder` matters more than it looks. A pack can only ever be searched with the model that built it, and without the flag AI-2 picks from your machine's RAM, which on a good computer means the 345 MB multilingual model. Everyone who installs your pack would then have to download it. `nomic-embed-text-v1.5` is 85 MB and is already on machines installed from the ISO of 2026-09-16 or later; an older AI-2 brought up to date still downloads it once, which is a great deal better than 345 MB. Use it for anything in English. (The flag needs `ai-2` 0.18.1 or newer.)

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
  - file: chapter-one.txt   # EXACTLY as ai-2 doc list shows it, extension included
    title: "Where this document came from"
    url: https://example.org/chapter-one
    retrieved: 2026-09-17
```

`file` is matched against the document name character for character, and the document name is the file's base name with its extension (`/home/you/text/chapter-one.txt` becomes `chapter-one.txt`). Write `chapter-one` and the source URL silently attaches to nothing: answers from that document will name the pack but never its source. Check your names with `ai-2 doc list` and copy them.

`revision` is the field people get wrong. It is the number AI-2 orders by, a `version` string cannot be compared reliably, and **the copy that counts is the one in this file**. The catalog entry repeats it, and CI fails if the two disagree.

## 5. Export the pack

```bash
ai-2 knowledge export mypack --manifest manifest.yml -o my-pack.ai2pack
```

The line it prints names the documents, the parts, the license and the embedder it recorded. Read it. If the embedder is not the one you meant, go back to step 3; it cannot be changed afterwards.

Your file paths are not in the pack. The documents' text and the search index are.

## 6. Try it as a stranger would

On another machine, or in a throwaway home directory on this one:

```bash
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
XDG_DATA_HOME="$tmp" ai-2 knowledge install my-pack.ai2pack
XDG_DATA_HOME="$tmp" ai-2 doc search --in my-pack "the question you most expect"
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

Fork this repository, branch, and add one entry to `catalog/community.yml`. It is the one catalog, for packs made by anyone, and the AI-2 project's own packs are in it too:

```yaml
- id: my-pack
  title: What it is, in a few words
  description: One sentence for the list of packs on the front page (optional)
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
  contact: your GitHub handle     # required: who made the pack and answers for it
```

Check it before you push, which takes seconds and saves a round trip:

```bash
python3 tools/validate-catalog.py                       # the entry itself
python3 tools/validate-catalog.py --install             # the full check, if you have ai2 installed
python3 tools/render-catalog.py                         # puts your pack in the table on the front page
```

Commit the README change that last command makes together with your entry. CI fails if the table and the catalog disagree.

**On versions, because the two numbers differ on purpose.** You build with 0.18.3 or newer, since 0.18.1 is what added `--embedder`. CI installs your pack with **v0.18.0**, the oldest released AI-2 that understands a pack's `revision`, so the pull request answers "does this artifact install on the oldest AI-2 that knows about packs as they are now", which is a stronger question than "does it install on the newest". If you run `--install` locally with a newer `ai2`, you are running the same checks against a newer baseline; a pass there and a fail in CI would mean your pack needs something an older AI-2 does not have, and that is worth knowing before people hit it.

## 10. Open the pull request

CI then does the whole thing for real: downloads your file, checks its size and SHA-256, **installs it with AI-2 itself**, and compares the manifest inside the installed pack against your entry, id, title, version, revision, license, languages, embedder, and the document and part counts. It also counts the rows in the installed index, requires the attribution your license asks for, and for Apache-2.0 and GFDL requires the license text to be inside the pack as a document.

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

We verify that your file is the one your entry describes, that it installs, that its license is one the catalog carries, and that the attribution and (for Apache-2.0 and GFDL) the license text are present. **We do not check whether its contents are correct, and we do not certify that you have met your license's obligations**, which remain yours. That is the same for every pack in the catalog, the project's own included. Who made a pack is in its entry, and that is what a person goes by.

Once merged, your pack is on the front page of this repository with its download link, and people install it from the file. Each `ai-2` release carries a copy of the catalog inside the signed package, and `ai-2 knowledge install ID` resolves a name only against that copy, so your pack is listed by `ai-2 knowledge available` and installs by name from the next `ai-2` release on. AI-2 records on every machine where an installed pack came from.

If we remove your entry, nothing reaches anyone's machine. A pack already installed stays until its owner removes it.
