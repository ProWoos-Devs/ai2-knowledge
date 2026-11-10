# basic-physics

Forces, gravity, friction, energy, simple machines, states of matter, heat, light, sound, electricity, magnets and floating for children ages 6 to 12 (`school-age` and `preteen`), written for study and reference on an AI-2 machine with no connection.

Written rather than extracted, and not from any one source or school program. Every topic was read twice, the second time by an independent reader who had not seen the first corrections, and then went through a content review (https://github.com/ProWoos-Devs/ai2-knowledge/issues/11). No teacher or physicist has reviewed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in basic-physics --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export basic-physics --manifest manifest.yml -o basic-physics.ai2pack
```

## Measured

An outside question set of 20, written by someone who had seen only the list of topic titles, searched with `ai-2 doc search` on the built Knowledge Pack (2026-11-10): top-1 19/20, top-3 20/20. One question ("where does a wound up toy car get its power from") missed on the first build, and a wind-up toy example and search terms were added because of it, so it is no longer an untouched question. Without it: top-1 18/19, top-3 19/19. The one not ranked first ("classroom examples of a push and a pull for year 2") had the right topic second, behind Start here.

## House style

- One subject per file, first line the title, then the search terms people would type.
- Every topic says "Written for AI-2. Directed to children, parents and teachers."
- Each section says the thing first in plain words, then shows it with something a child can see or try with paper, string, magnets, water or a flashlight.
- Search shows passages of about 110 words, so each section is written to be understood without the ones before it. A number opens the whole topic.
- Metric units only (meters, kilograms, newtons, joules, degrees Celsius).
- The only electricity a topic invites a child to handle is a 1.5 volt battery. Wall sockets are named as dangerous and never part of an experiment.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
