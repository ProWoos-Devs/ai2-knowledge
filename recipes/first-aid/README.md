# first-aid

What to do in a medical emergency, for a person with no training, no connection and possibly no help on the way. Written in its own wording from the IFRC International First Aid, Resuscitation and Education Guidelines 2025. IFRC did not write or endorse it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in first-aid --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export first-aid --manifest manifest.yml -o first-aid.ai2pack
```

## House style

- One situation per file, first line the title, then the search terms people would type.
- Every topic says "Written from IFRC 2025. Not reviewed by a clinician." No clinician reviewed these. Each instruction cites a printed page of the IFRC guidelines in square brackets, and independent readers compared the topics with the guidelines.
- IFRC wins a conflict between sources, and the topic notes the difference. If no source covers a case, the topic says so and nothing is added.
- Every topic has a section for when help is delayed or cannot be reached.
- Search shows passages of about 110 words, so a passage can lack a warning from elsewhere in its topic. A number opens the whole topic.

## Measured

An outside question set of 20, written by someone who had seen only the list of topic titles: top-1 14/20, top-3 19/20. The misses are mostly ones where a topic for another age or Drowning came first, and one question ("found my mum on the floor, she's snoring and breathing ok but i can't wake her") did not reach the right topic in the top three.
