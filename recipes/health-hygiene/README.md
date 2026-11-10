# health-hygiene

Routine hygiene, teeth, safe water and food, nutrition, sleep, activity and recognizing illness for children ages 6 to 12 (`school-age` and `preteen`), with parents and teachers helping. Written for study and reference on an AI-2 machine with no connection. Categories: `'13.13'` Water, sanitation and hygiene; `'13.14'` Nutrition; `'07.05'` Primary and secondary education. Audience: `children`. Language: English. License: MIT for the original writing. Contact: ProWoos-Devs.

Written in original wording from CDC, NIH and HHS agency health information. Source: Centers for Disease Control and Prevention; National Institutes of Health; U.S. Department of Health and Human Services. These agencies and the United States Government did not write or endorse this Knowledge Pack. Their original information is available online without charge. Agency logos, photographs, copied tables and source documents are not included.

Codex completed the author's first reading against REVIEWING.md and the sources; twelve corrections were recorded and applied. This is an AI-assisted reading. The independent second reading has not taken place. No teacher or clinician has reviewed this Knowledge Pack. It has not been built or measured.

There are no telephone numbers here, or in any Knowledge Packs.

## Rebuilding

```
ai-2 doc index --in health-hygiene --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export health-hygiene --manifest manifest.yml -o health-hygiene.ai2pack
```

## House style

- One subject per file, first line the title, then the search terms people would type.
- Every topic says "Written for AI-2. Directed to children, parents and teachers."
- Fourteen subject topics of about 400 words excluding references, plus Start here and About. The About topic carries the source key for offline readers.
- Every health instruction cites its source and section in square brackets. Most sources are unpaginated web pages: `web` in a citation means that, never an invented PDF page. ACTIVITY cites the printed pages of the HHS guidelines. The school guidance's numbered web pages are identified separately below. Sources consulted on 2026-11-10.
- Each short passage keeps the qualifications needed to understand it. Search shows passages of about 110 words, so a reader may not see a warning elsewhere in the topic.
- Metric units and American spelling. Converted temperatures are rounded and described as approximate; time limits retain the source's qualifications.
- Routine prevention, with the child and helping adult roles stated. No medicine doses, rehydration recipes, chemical-mixing instructions, latrine construction or independent medical treatment for children. Source gaps when supplies or help are missing are stated rather than filled from memory.
- Source differences are resolved explicitly, not mixed: the current NIH sleep recommendation is used instead of the older 2011 booklet's number. The activity target follows the cited CDC guidance; the text does not claim all agencies phrase it identically.

## Sources and how they are cited

The source key is also inside `topics/about-this-pack.txt`, so it remains available after offline installation. The manifest attaches a primary agency source URL to each of the fourteen subject documents, using its exact `.txt` filename; additional sources and precise sections are in the topic citations. The introductory texts are original AI-2 guidance.

| In the topics | Source | Page or section convention |
| --- | --- | --- |
| HYG | CDC, [Hygiene Basics](https://www.cdc.gov/hygiene/about/index.html) | Named section; unpaginated web page. |
| GERM | CDC, [Appendix A: How Infections Spread](https://www.cdc.gov/children-and-school-preparedness/infection-prevention/appendix-a.html) | Web guidance page 8 of 10; section named in citation. |
| HAND | CDC, [About Handwashing](https://www.cdc.gov/clean-hands/about/) | Named section; unpaginated web page. |
| HANDFAQ | CDC, [Hand Hygiene Frequently Asked Questions](https://www.cdc.gov/clean-hands/faq/index.html) | Named section; unpaginated web page. |
| SCHOOLHAND | CDC, [About Hand Hygiene in Schools and Early Care and Education Settings](https://www.cdc.gov/clean-hands/prevention/about-hand-hygiene-in-schools-and-early-care-and-education-settings.html) | Named section; unpaginated web page. |
| HAIR | CDC, [Healthy Habits: Hair and Scalp Hygiene](https://www.cdc.gov/hygiene/about/hair-and-scalp-hygiene.html) | Named section; unpaginated web page. |
| FOOT | CDC, [Healthy Habits: Foot Hygiene](https://www.cdc.gov/hygiene/about/foot-hygiene.html) | Named section; unpaginated web page. |
| NAIL | CDC, [Healthy Habits: Nail Hygiene](https://www.cdc.gov/hygiene/about/nail-hygiene.html) | Named section; unpaginated web page. |
| PERIOD | CDC, [Healthy Habits: Menstrual Hygiene](https://www.cdc.gov/hygiene/about/menstrual-hygiene.html) | Named section; unpaginated web page. |
| WATER | CDC, [How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html) | Named section; unpaginated web page. |
| STORE | CDC, [How to Create an Emergency Water Supply](https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html) | Named section; unpaginated web page. |
| FOOD | CDC, [Preventing Food Poisoning](https://www.cdc.gov/food-safety/prevention/index.html) | Named section; unpaginated web page. |
| TEETH | NIH/NIDCR, [Oral Hygiene](https://www.nidcr.nih.gov/health-info/oral-hygiene) | Named section; unpaginated web page. |
| DECAY | NIH/NIDCR, [The Tooth Decay Process: How to Reverse It and Avoid a Cavity](https://www.nidcr.nih.gov/health-info/tooth-decay/more-info/tooth-decay-process) | Named section; unpaginated web page. |
| EAT | NIH/NIDDK, [Helping Your Child: Tips for Parents & Other Caregivers](https://www.niddk.nih.gov/health-information/weight-management/healthy-eating-physical-activity-for-life/helping-your-child-tips-for-parents) | Named section; unpaginated web page. |
| SLEEP | NIH/NHLBI, [How Much Sleep Is Enough?](https://www.nhlbi.nih.gov/health/sleep/how-much-sleep) | Named section; unpaginated web page. |
| SLEEPH | CDC, [About Sleep](https://www.cdc.gov/sleep/about/index.html) | Named section; unpaginated web page. |
| PLAY | CDC, [Child Activity: An Overview](https://www.cdc.gov/physical-activity-basics/guidelines/children.html) | Named section; unpaginated web page. |
| PLAYTYPES | CDC, [What Counts for Children and Teens](https://www.cdc.gov/physical-activity-basics/adding-children-adolescents/what-counts.html) | Named section; unpaginated web page. |
| COUGH | CDC, [Hygiene and Respiratory Viruses Prevention](https://www.cdc.gov/respiratory-viruses/prevention/hygiene.html) | Named section; unpaginated web page. |
| AIR | CDC, [Everyday Actions for Schools to Prevent and Control the Spread of Infections](https://www.cdc.gov/children-and-school-preparedness/infection-prevention/actions.html) | Web guidance page 2 of 10; section named in citation. |
| SICK | CDC, [When Students or Staff are Sick](https://www.cdc.gov/children-and-school-preparedness/infection-prevention/when-sick.html) | Web guidance page 3 of 10; section named in citation. |
| FLU | CDC, [Signs and Symptoms of Flu](https://www.cdc.gov/flu/signs-symptoms/index.html) | Named section; unpaginated web page. |
| SEIZURE | CDC, [Epilepsy Basics](https://www.cdc.gov/epilepsy/about/index.html) | Overview and Signs and symptoms; unpaginated web page. |
| ACTIVITY | HHS, [Physical Activity Guidelines for Americans, second edition (2018)](https://odphp.health.gov/sites/default/files/2019-09/Physical_Activity_Guidelines_2nd_edition.pdf) | Printed pp. 48 and 52–53. |
| MEDS | CDC, [Up and Away Campaign Resources](https://www.cdc.gov/medication-safety/php/toolkit/index.html) | Named section; unpaginated web page. |
| BLEACH | CDC, [Cleaning and Disinfecting with Bleach](https://www.cdc.gov/hygiene/about/cleaning-and-disinfecting-with-bleach.html) | Named section; unpaginated web page. |

## Source reuse

[CDC's agency-material policy](https://www.cdc.gov/other/agencymaterials.html) describes most agency text as public domain, with exceptions for third-party material and differing treatment outside the United States. It requires agency credit, no implied endorsement, no change to substantive content and a statement that the original is available free. This Knowledge Pack independently explains the cited factual guidance for children while preserving its meaning and qualifications; it does not reproduce agency artwork or third-party content.

[NIDCR's policy](https://www.nidcr.nih.gov/about-us/web-policies) permits use of its public-domain information with the publication title, URL, access date and agency credit. [NIDDK's policy](https://www.niddk.nih.gov/copyright) permits editing with no agency logos or implied endorsement; its source is used here for general nutrition education, not individualized treatment. [NHLBI's policy](https://www.nhlbi.nih.gov/about/contact/trademark-branding-and-logo) describes most information as public domain; this Knowledge Pack uses facts from the current web page and does not alter or distribute a formatted NHLBI publication.

The HHS physical activity guidelines are a federal agency publication; only their factual recommendations are independently explained, with the publication credited. Its photographs, tables and layout are not reproduced.

MIT applies to the original AI-2 educational writing, not a claim to relicense an agency document or own public-domain facts. A rights specialist has not reviewed this use. Restricted WHO and UNICEF publications are not copied or adapted as part of this recipe.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it. Reviewers should compare each health instruction with its cited section and read each topic as the only help available offline. In particular, check child versus adult roles, missing supplies, the distinction between school attendance and urgent medical help, and the age range of every numeric recommendation.

An AI-assisted first reading does not replace the required independent second reading, a teacher's reading or a clinician's reading. No teacher or clinician has reviewed this Knowledge Pack.
