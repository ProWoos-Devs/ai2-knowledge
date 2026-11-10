# basic-physics

Forces, gravity, friction, energy, simple machines, states of matter, heat, light, sound, electricity, magnets and floating for children ages 6 to 12 (`school-age` and `preteen`), written for study and reference on an AI-2 machine with no connection.

Written rather than extracted, and not from any one source or school program. Every topic was read twice, the second time by an independent reader who had not seen the first corrections. No teacher or physicist has reviewed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in basic-physics --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export basic-physics --manifest manifest.yml -o basic-physics.ai2pack
```

## House style

- One subject per file, first line the title, then the search terms people would type.
- Every topic says "Written for AI-2. Directed to children, parents and teachers."
- Each section says the thing first in plain words, then shows it with something a child can see or try with paper, string, magnets, water or a flashlight.
- Search shows passages of about 110 words, so each section is written to be understood without the ones before it. A number opens the whole topic.
- Metric units only (meters, kilograms, newtons, joules, degrees Celsius).
- The only electricity a topic invites a child to handle is a 1.5 volt battery. Wall sockets are named as dangerous and never part of an experiment.
