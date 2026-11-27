# food-without-power

Keeping food safe when the refrigerator and freezer have no power, for a household with no connection and possibly no help on the way: before the power goes, the hours while it is off, a cool box, what to keep and what to throw out from the refrigerator and the freezer, food that keeps without a refrigerator, judging food with no thermometer, floods, fires, baby formula and cleaning a refrigerator. Written in its own wording from United States government food safety pages. None of the agencies wrote or endorsed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in food-without-power --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export food-without-power --manifest manifest.yml -o food-without-power.ai2pack
```

## House style

The same as First Aid and Water and Sanitation.

- One situation per file, first line the title, then the search terms people would type.
- Every topic says "Written from USDA, FoodSafety.gov and CDC sources. Not reviewed by a food safety specialist." and, on the next line, "Last reviewed:" with the date the topic was last checked against its sources. Each instruction cites its source in square brackets.
- The FoodSafety.gov chart (reviewed 2024) wins a conflict with the older USDA page (2013), and the topic notes the difference. The USDA and CDC bleach solutions differ by about three times in strength; both are given as their source states them. If no source covers a case, the topic says so and nothing is added.
- Metric figures come first. Where the source gives only US units, the conversion is ours and the topic says so.
- Every topic has a section for when help is delayed or cannot be reached.
- Search shows passages of about 110 words, so a passage can lack a warning from elsewhere in its topic. A number opens the whole topic.

## Sources and how they are cited

| In the topics | Source | Read |
|---|---|---|
| USDA | USDA Food Safety and Inspection Service, Keep Your Food Safe During Emergencies: Power Outages, Floods & Fires, last updated 2013-08-07, https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/emergencies/keep-your-food-safe-during-emergencies | 2026-11-27 |
| Chart | FoodSafety.gov, Food Safety During Power Outage (refrigerated and frozen food charts), reviewed 2024-08-08, https://www.foodsafety.gov/food-safety-charts/food-safety-during-power-outage | 2026-11-27 |
| CDC | Centers for Disease Control and Prevention, Keep Food Safe After a Disaster or Emergency, 2025-11-24, https://www.cdc.gov/food-safety/foods/keep-food-safe-after-emergency.html | 2026-11-27 |

Reuse: all three are works of the United States government. The topics are in our own words and cite them, as with Looking After a Laptop.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
