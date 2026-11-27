# staying-warm-safely

Staying warm at home when the power, gas or heating has stopped, for a household with no connection and possibly no help on the way: carbon monoxide and what to do if you suspect it, what must never be burned or run indoors, generators, alarms, heaters, fireplaces and stoves, keeping the heat in, dressing for the cold, babies and older people, hypothermia and frostbite. Written in its own wording from United States government pages. None of the agencies wrote or endorsed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in staying-warm-safely --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export staying-warm-safely --manifest manifest.yml -o staying-warm-safely.ai2pack
```

## House style

The same as First Aid and Water and Sanitation.

- One situation per file, first line the title, then the search terms people would type.
- Every topic says "Written from CDC, U.S. Fire Administration and CPSC sources. Not reviewed by a fire safety or health specialist." and, on the next line, "Last reviewed:" with the date the topic was last checked against its sources. Each instruction cites its source in square brackets.
- Where sources differ, the topic says so. If no source covers a case, the topic says so and nothing is added.
- Meters and degrees Celsius come first. The sources give feet and Fahrenheit, so the conversions are ours: 20 feet is given as more than 6.1 meters, 3 feet as at least 1 meter, 95 °F as 35 °C.
- CPR is not taught here; the hypothermia topic points to the First Aid Knowledge Pack.
- Every topic has a section for when help is delayed or cannot be reached.
- Search shows passages of about 110 words, so a passage can lack a warning from elsewhere in its topic. A number opens the whole topic.

## Sources and how they are cited

| In the topics | Source | Read |
|---|---|---|
| CO | CDC, Carbon Monoxide (CO) Poisoning Basics, 2026-10-26, https://www.cdc.gov/carbon-monoxide/about/index.html | 2026-11-27 |
| Storm | CDC, Safety Guidelines: During & After a Winter Storm, 2026-08-25, https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html | 2026-11-27 |
| Prepare | CDC, Preparing for a Winter Storm, 2026-11-19, https://www.cdc.gov/winter-weather/safety/index.html | 2026-11-27 |
| Hypo | CDC, Preventing Hypothermia, 2026-08-25, https://www.cdc.gov/winter-weather/prevention/index.html | 2026-11-27 |
| Frost | CDC, Preventing Frostbite, 2026-08-25, https://www.cdc.gov/winter-weather/prevention/preventing-frostbite.html | 2026-11-27 |
| USFA | U.S. Fire Administration, Heating Fire Safety, last reviewed 2023-05-04, https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/ | 2026-11-27 |
| CPSC | U.S. Consumer Product Safety Commission, Carbon Monoxide, no date shown, https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center | 2026-11-27 |

Reuse: all are works of the United States government. The topics are in our own words and cite them, as with Looking After a Laptop.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
