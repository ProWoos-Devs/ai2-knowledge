# water-sanitation

Safe water and sanitation for a household or small group with no water supply, no sewage service, no connection and possibly no help on the way. Written in its own wording, mainly from the WHO/WEDC Technical Notes on Drinking-water, Sanitation and Hygiene in Emergencies (2013). WHO and the other sources did not write or endorse it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in water-sanitation --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export water-sanitation --manifest manifest.yml -o water-sanitation.ai2pack
```

## House style

The same as First Aid.

- One situation per file, first line the title, then the search terms people would type.
- Every topic says "Written from WHO sources. Not reviewed by a water or health specialist." Each instruction cites its source in square brackets, and independent readers compared the topics with the sources.
- WHO wins a conflict between sources, except on solar disinfection, where the SODIS manual is the more detailed source. The topic notes every difference. If no source covers a case, the topic says so and nothing is added.
- Every topic has a section for when help is delayed or cannot be reached.
- Search shows passages of about 110 words, so a passage can lack a warning from elsewhere in its topic. A number opens the whole topic.

## Sources and how they are cited

| In the topics | Source | Pages cited |
|---|---|---|
| TN 5.2 | WHO/WEDC, Technical Notes on Drinking-water, Sanitation and Hygiene in Emergencies, 2nd edition, 2013, https://wedc-knowledge.lboro.ac.uk/collections/tne/notes_emergencies.html | note and page, as printed |
| Boil | WHO, Boil Water, technical brief WHO/FWC/WSH/15.02, 2015, https://www.who.int/publications/i/item/WHO-FWC-WSH-15.02 | two pages, not numbered |
| DWQ p. 142 | WHO, Guidelines for Drinking-water Quality, 4th edition with the first and second addenda, 2022, https://www.who.int/publications/i/item/9789240045064 | PDF page |
| SAN p. 17 | WHO, Guidelines on Sanitation and Health, 2018, https://www.who.int/publications/i/item/9789241514705 | PDF page |
| SODIS p. 8 | Eawag, SODIS Manual: Guidance on Solar Water Disinfection, 2016, https://www.eawag.ch/fileadmin/Domain1/Abteilungen/sandec/publikationen/SWP/SODIS_manual_2016.pdf | PDF page |
| EPA | US EPA, Emergency Disinfection of Drinking Water, updated 2026-02-24, https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water | one web page |
| Sphere | The Sphere Handbook, 4th edition, 2018, https://spherestandards.org/handbook/ | PDF page |

Reuse: the WHO/WEDC notes and the Boil Water brief are "all rights reserved", the two WHO guidelines are CC BY-NC-SA 3.0 IGO, and Sphere allows free reproduction for education but not adaptation without permission. So the topics are in our own words, as with First Aid. The SODIS manual allows copying and adapting with acknowledgement.

## Measured

Not yet. An outside question set comes after the independent check.
