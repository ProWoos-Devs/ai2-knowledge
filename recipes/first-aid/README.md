# first-aid

Eleven first-aid cards for people with no training, one document per card, for a person with no connection and no help on the way. Written in its own wording from the IFRC International First Aid, Resuscitation and Education Guidelines 2025, and checked against them. IFRC did not write or endorse it.

**This is a draft, and every card says so.** It has not been reviewed by a clinician. Search shows passages of about 110 words, so open the whole card by typing its number.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
python3 render-cards.py        # checks cards/*.yml and writes documents/
ai-2 doc index --in first-aid --embedder nomic-embed-text-v1.5 documents/*.txt
ai-2 knowledge export first-aid --manifest manifest.yml -o first-aid.ai2pack
```

`render-cards.py` says a card is complete, not that it is correct.
