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
- WHO wins a conflict between sources, with two exceptions: solar disinfection, where the SODIS manual is the more detailed source, and the latrine distance, where Sphere's 30 meters is used because the soil cannot be tested at home (accepted by Rafael, 2026-11-06). The household bleach dose is given from both WHO and the EPA, pending Rafael's choice. The topic notes every difference. If no source covers a case, the topic says so and nothing is added.
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
| YB | CDC Yellow Book, Water Disinfection for Travelers, Heat section, read 2026-11-10, https://www.cdc.gov/yellow-book/hcp/preparing-international-travelers/water-disinfection-for-travelers.html | one web page, used only in Boiling water for the difference between small bubbles and a rolling boil |
| Sphere | The Sphere Handbook, 4th edition, 2018, https://spherestandards.org/handbook/ | PDF page |

Reuse: the WHO/WEDC notes and the Boil Water brief are "all rights reserved", the two WHO guidelines are CC BY-NC-SA 3.0 IGO, and Sphere allows free reproduction for education but not adaptation without permission. So the topics are in our own words, as with First Aid. The SODIS manual allows copying and adapting with acknowledgement.

## Measured

Two outside question sets, each written by a separate reader who had seen only the list of topic titles, searched with `ai-2 doc search` on the built Knowledge Pack (2026-11-06):

- Set 2, 22 questions, untouched: top-1 17/22, top-3 21/22, the same after the round 3 corrections. The one miss ("how to keep clean when theres hardly any water, tippy tap") has no answer in the sources read.
- Set 1, 20 questions: top-1 17/20 and top-3 20/20 on the first build. After the second round of corrections it was 17/20 and 18/20, and three search lines were then given everyday words its misses used (gasoline, use the sun, which bucket). It is no longer an outside measure: 19/20 and 19/20.
- Revision 3 (2026-11-11, the boiling topic rewritten to the WHO rule in plain words, no question changed): Set 2 top-1 17/22 and top-3 21/22, the same as before, with the same one miss. Set 1 top-1 18/20 and top-3 20/20.

Independent checks of every topic against its sources: round 1 found 0 high, 11 medium and 14 low; round 2, on the corrected text, 0 high, 7 medium and 19 low; round 3, 1 high (a round 2 fix had dropped the emptying of a seawater-flooded well after its chlorine dose), 5 medium and 21 low. All were corrected, and the well steps were rewritten whole. Round 4, on the rewritten passages: 1 high (iodine had no warnings although the WHO guidelines give them), 4 medium, 13 low, all corrected; it also found WHO gives its own household bleach dose, now stated beside the EPA one. Round 5, on the latest changes: 0 high, 8 medium, 9 low, all corrected; the well topic was rewritten as two explicit paths, ordinary and seawater. Round 6, well topic only: 0 high, 5 medium, 8 low; all three reader paths complete with no loop and no unsafe drinking; corrected where the sources allow. Two dead ends are gaps in the sources and stay stated as such: whether to chlorinate when the coin test shows under 10 but WHO needs under 5, and when people may use the well again without a chlorine test kit.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
