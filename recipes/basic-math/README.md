# basic-math

The building blocks of arithmetic, fractions, decimals, negative numbers, shapes and measurement for children ages 6 to 12 (`school-age` and `preteen`), written for study and reference on an AI-2 machine with no connection.

Written rather than extracted, and not from any one source or school program. Every topic was read twice, the second time by an independent reader who had not seen the first corrections, and then went through an AI-assisted content review (https://github.com/ProWoos-Devs/ai2-knowledge/issues/11). No teacher has reviewed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in basic-math --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export basic-math --manifest manifest.yml -o basic-math.ai2pack
```

## Measured

An outside question set of 20, written by someone who had seen only the list of topic titles, searched with `ai-2 doc search` on the built Knowledge Pack (2026-11-10): top-1 18/20, top-3 20/20. The two not ranked first ("what is the tens place and the ones place" and "what does the dot in 3.5 mean") had the right topic second and third.

## House style

- One subject per file, first line the title, then the search terms people would type.
- Every topic says "Written for AI-2. Directed to children, parents and teachers."
- Each section says the thing first in plain words, then shows it with a worked example from everyday life (sharing fruit, folding paper, measuring a room).
- Search shows passages of about 110 words, so each section is written to be understood without the ones before it. A number opens the whole topic.
- Metric units only. Decimals are written with a point and thousands with a comma, and the About topic says that many countries do it the other way round.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
