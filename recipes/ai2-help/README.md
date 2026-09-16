# ai2-help

AI-2's own documentation as a knowledge pack, so a machine with no working network can still answer "how do I get the WiFi working?".

## What goes in

- the wiki pages, as published (`000/wiki/*.md` in the AI-2 workspace, or the public wiki)
- the project README
- the task topics in `topics/`, which cover what the wiki states only as a row in a command table

That last part is the lesson from the first measurement. Two questions, "how can I make AI-2 use a stronger computer on my home network?" and "how do I stop the AI when I want the memory back?", both failed against the wiki alone: the answers existed only as table rows, and a row inside a 110-word part does not stand out to a question asked in plain words. Written as topics, both are found first.

## Rebuilding

Convert the wiki pages to plain text (strip the markup, keep the words), then:

```
ai-2 doc index --in ai2-help pages/*.txt topics/*.txt
ai-2 knowledge export ai2-help --manifest manifest.yml -o ai2-help.ai2pack
```

## Measured

An outside question set of 20: top-1 18/20, top-3 20/20, against 17/20 and 18/20 with the wiki pages alone.
