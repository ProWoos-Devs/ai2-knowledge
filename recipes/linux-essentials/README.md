# linux-essentials

The everyday trouble of running a Linux machine, written as the questions people actually ask: a full disk, a frozen program, permission denied, no internet, an archive that will not open.

Written rather than extracted. Extracting GNU manuals would mean carrying the GFDL's modified-version obligations, and it would retrieve worse: manual pages answered 11 of 15 plain-language questions in testing, and text written as tasks answered 15 of 15.

## Rebuilding

```
ai-2 doc index --in linux-essentials topics/*.txt
ai-2 knowledge export linux-essentials --manifest manifest.yml -o linux-essentials.ai2pack
```

## House style

- One subject per file, roughly 150 to 250 words, first line the title.
- Open with the situation in the reader's words ("The disk is full, or nearly full"), not with the command's name.
- Name the command and show the form to type, then say what the output means.
- Say the AI-2 truth where it differs from generic Linux advice: this system runs runit, so `systemctl` does not exist here.
- One idea per file. "Making a script executable" started inside the permissions topic and was missed by a question that said "executable" rather than "runnable"; as its own topic it is found first.

## Measured

An outside question set of 20, written by someone who had not read the topics: top-1 19/20, top-3 20/20. The first run, before three subjects were written, scored 17/20.
