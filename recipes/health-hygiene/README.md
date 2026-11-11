# health-hygiene

Routine hygiene, teeth, safe water and food, nutrition, sleep, activity and recognizing illness for children ages 6 to 12 (`school-age` and `preteen`), with parents and teachers helping. Written for study and reference on an AI-2 machine with no connection. Categories: `'13.13'` Water, sanitation and hygiene; `'13.14'` Nutrition; `'07.05'` Primary and secondary education. Audience: `children`. Language: English. License: MIT for the original writing. Contact: ProWoos-Devs.

Written in original wording from agency health information and professional factual recommendations, with the boiling instruction from WHO's guidance. Sources: Centers for Disease Control and Prevention; National Institutes of Health; U.S. Department of Health and Human Services; U.S. Food and Drug Administration; World Health Organization; American Dental Association. These organizations and the United States Government did not write or endorse this Knowledge Pack. Their original information is available online without charge. Source logos, photographs, copied tables and source documents are not included.

A first reading against REVIEWING.md and the sources recorded twelve corrections, which were applied. An independent second reading reported 26 omissions or comprehension issues. Nineteen were corrected; seven source gaps were accepted by the project maintainer, with a partial correction to one using an existing source. A further [content review](https://github.com/ProWoos-Devs/ai2-knowledge/issues/18) reported eight findings; all eight were checked against their sources and applied, including urgent help for diarrhea lasting more than a day. School attendance and return criteria now have their own topic. No teacher or clinician has reviewed this Knowledge Pack.

There are no telephone numbers here, or in any Knowledge Packs.

## Rebuilding

```
ai-2 doc index --in health-hygiene --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export health-hygiene --manifest manifest.yml -o health-hygiene.ai2pack
```

## Measured

Built on 2026-11-10 with ai-2 0.29.0: 17 documents, 107 parts. An outside question set of 20, written by someone who had seen only the list of the 15 subject topic titles, searched with `ai-2 doc search` on the built Knowledge Pack: top-1 19/20, top-3 20/20. No question was changed. The one that did not come first ("We have no soap at school this week. What can the children use to clean their hands before eating?") found the hand washing topic second, after the toilet topic.

## House style

- One subject per file, first line the title, then the search terms people would type.
- Every topic says "Written for AI-2. Directed to children, parents and teachers."
- Fifteen subject topics of about 400 words excluding references, plus Start here and About: 17 topics in total. Urgent illness advice and school attendance are separate topics, each understandable on its own. The About topic carries the source key for offline readers.
- Every health instruction cites its source and section in square brackets. Most sources are unpaginated web pages: `web` in a citation means that, never an invented PDF page. ACTIVITY cites the printed pages of the HHS guidelines; ASTHMA cites printed pp. 13–14 of the NHLBI school guide; BOIL cites page 1 of WHO's two-page brief. The school guidance's numbered web pages are identified separately below. Sources consulted on 2026-11-10.
- Each short passage keeps the qualifications needed to understand it. Search shows passages of about 110 words, so a reader may not see a warning elsewhere in the topic.
- Metric units and American spelling. Converted temperatures are rounded and described as approximate; time limits retain the source's qualifications.
- Routine prevention, with the child and helping adult roles stated. No medicine doses, rehydration recipes, chemical-mixing instructions, latrine construction or independent medical treatment for children. Source gaps when supplies or help are missing are stated rather than filled from memory.
- The adult boiling instruction follows WHO's rule, the same one used in Water and Sanitation: heat the water until it is bubbling hard, then take it off the heat. CDC's emergency page adds 1 minute of boiling, 3 minutes at high elevation, which its Yellow Book describes as a margin of safety; this recipe does not use the timed rule. The current NIH sleep recommendation is used instead of the older 2011 booklet's number. The activity target follows the cited CDC guidance.

## Sources and how they are cited

The source key is also inside `topics/about-this-pack.txt`, so it remains available after offline installation. The manifest attaches a primary agency source URL to each of the fifteen subject documents, using its exact `.txt` filename; additional sources and precise sections are in the topic citations. The introductory texts are original AI-2 guidance.

| In the topics | Source | Page or section convention |
| --- | --- | --- |
| HYG | CDC, [Hygiene Basics](https://www.cdc.gov/hygiene/about/index.html) | Named section; unpaginated web page. |
| GERM | CDC, [Appendix A: How Infections Spread](https://www.cdc.gov/children-and-school-preparedness/infection-prevention/appendix-a.html) | Web guidance page 8 of 10; section named in citation. |
| HAND | CDC, [About Handwashing](https://www.cdc.gov/clean-hands/about/) | Named section; unpaginated web page. |
| HANDFAQ | CDC, [Hand Hygiene Frequently Asked Questions](https://www.cdc.gov/clean-hands/faq/index.html) | Named section; unpaginated web page. |
| SANITIZER | CDC, [Hand Sanitizer Guidelines and Recommendations](https://www.cdc.gov/clean-hands/about/hand-sanitizer.html) | How it works; Dos; Don'ts; unpaginated web page. |
| SCHOOLHAND | CDC, [About Hand Hygiene in Schools and Early Care and Education Settings](https://www.cdc.gov/clean-hands/prevention/about-hand-hygiene-in-schools-and-early-care-and-education-settings.html) | Named section; unpaginated web page. |
| HAIR | CDC, [Healthy Habits: Hair and Scalp Hygiene](https://www.cdc.gov/hygiene/about/hair-and-scalp-hygiene.html) | Named section; unpaginated web page. |
| FOOT | CDC, [Healthy Habits: Foot Hygiene](https://www.cdc.gov/hygiene/about/foot-hygiene.html) | Named section; unpaginated web page. |
| NAIL | CDC, [Healthy Habits: Nail Hygiene](https://www.cdc.gov/hygiene/about/nail-hygiene.html) | Named section; unpaginated web page. |
| PERIOD | CDC, [Healthy Habits: Menstrual Hygiene](https://www.cdc.gov/hygiene/about/menstrual-hygiene.html) | Named section; unpaginated web page. |
| WATER | CDC, [How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html) | Named section; unpaginated web page. |
| YELLOW | CDC Yellow Book, [Water Disinfection for Travelers](https://www.cdc.gov/yellow-book/hcp/preparing-international-travelers/water-disinfection-for-travelers.html), 2026 edition | Heat; unpaginated web page. |
| BOIL | WHO, [Boil water, technical brief WHO/FWC/WSH/15.02 (2015)](https://www.who.int/publications/i/item/WHO-FWC-WSH-15.02) | PDF p. 1, Introduction and Conclusions. |
| STORE | CDC, [How to Create an Emergency Water Supply](https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html) | Named section; unpaginated web page. |
| FOOD | CDC, [Preventing Food Poisoning](https://www.cdc.gov/food-safety/prevention/index.html) | Named section; unpaginated web page. |
| MILK | CDC, [Raw Milk](https://www.cdc.gov/food-safety/foods/raw-milk.html) | Overview; unpaginated web page. |
| TEETH | NIH/NIDCR, [Oral Hygiene](https://www.nidcr.nih.gov/health-info/oral-hygiene) | Named section; unpaginated web page. |
| BRUSH | American Dental Association, [Toothbrushes](https://www.ada.org/resources/ada-library/oral-health-topics/toothbrushes), updated August 2026 | Key Points; Toothbrushing Methods; Toothbrush Care; unpaginated web page. Factual recommendations only, in our own words. |
| DECAY | NIH/NIDCR, [The Tooth Decay Process: How to Reverse It and Avoid a Cavity](https://www.nidcr.nih.gov/health-info/tooth-decay/more-info/tooth-decay-process) | Named section; unpaginated web page. |
| EAT | NIH/NIDDK, [Helping Your Child: Tips for Parents & Other Caregivers](https://www.niddk.nih.gov/health-information/weight-management/healthy-eating-physical-activity-for-life/helping-your-child-tips-for-parents) | Named section; unpaginated web page. |
| SLEEP | NIH/NHLBI, [How Much Sleep Is Enough?](https://www.nhlbi.nih.gov/health/sleep/how-much-sleep) | Named section; unpaginated web page. |
| ASTHMA | NIH/NHLBI, [Managing Asthma: A Guide for Schools](https://www.nhlbi.nih.gov/sites/default/files/publications/14-2650%20NACI_ManagingAsthma-508%20FINAL.pdf), revised December 2014 | Printed pp. 13–14, access to prescribed medicines and authorized self-administration under the child's plan. |
| SLEEPH | CDC, [About Sleep](https://www.cdc.gov/sleep/about/index.html) | Named section; unpaginated web page. |
| PLAY | CDC, [Child Activity: An Overview](https://www.cdc.gov/physical-activity-basics/guidelines/children.html) | Named section; unpaginated web page. |
| PLAYTYPES | CDC, [What Counts for Children and Teens](https://www.cdc.gov/physical-activity-basics/adding-children-adolescents/what-counts.html) | Named section; unpaginated web page. |
| COUGH | CDC, [Hygiene and Respiratory Viruses Prevention](https://www.cdc.gov/respiratory-viruses/prevention/hygiene.html) | Named section; unpaginated web page. |
| AIR | CDC, [Everyday Actions for Schools to Prevent and Control the Spread of Infections](https://www.cdc.gov/children-and-school-preparedness/infection-prevention/actions.html) | Web guidance page 2 of 10; section named in citation. |
| SICK | CDC, [When Students or Staff are Sick](https://www.cdc.gov/children-and-school-preparedness/infection-prevention/when-sick.html) | Web guidance page 3 of 10; section named in citation. |
| FLU | CDC, [Signs and Symptoms of Flu](https://www.cdc.gov/flu/signs-symptoms/index.html) | Named section; unpaginated web page. |
| DIARRHEA | CDC, [What You Can Do to Prevent Diarrheal Illness After a Disaster](https://www.cdc.gov/water-emergency/safety/index.html) | What to do if you or your family are ill with diarrhea; unpaginated web page. |
| NORO | CDC, [About Norovirus](https://www.cdc.gov/norovirus/about/index.html) | Signs and symptoms; Drink plenty of liquids; unpaginated web page. |
| GASTRO | NIH/NIDDK, [Symptoms & Causes of Viral Gastroenteritis (“Stomach Flu”)](https://www.niddk.nih.gov/health-information/digestive-diseases/viral-gastroenteritis/symptoms-causes), with the linked NIDDK Dictionary definitions of [rectum](https://www.niddk.nih.gov/Dictionary/R/rectum) and [pus](https://www.niddk.nih.gov/Dictionary/P/pus) | What are the symptoms of dehydration?; Seek care right away, Infants and children; Dictionary definitions of rectum and pus. Unpaginated web pages. |
| TAMPON | FDA, [The Facts on Tampons and Tampon Safety](https://www.fda.gov/consumers/consumer-updates/facts-tampons-and-tampon-safety) | Can tampons cause toxic shock syndrome (TSS)?; Tampon Safety Tips, especially tips 5 and 7; unpaginated web page. |
| SEIZURE | CDC, [Epilepsy Basics](https://www.cdc.gov/epilepsy/about/index.html) | Overview and Signs and symptoms; unpaginated web page. |
| ACTIVITY | HHS, [Physical Activity Guidelines for Americans, second edition (2018)](https://odphp.health.gov/sites/default/files/2019-09/Physical_Activity_Guidelines_2nd_edition.pdf) | Printed pp. 48 and 52–53. |
| MEDS | CDC, [Up and Away Campaign Resources](https://www.cdc.gov/medication-safety/php/toolkit/index.html) | Named section; unpaginated web page. |
| BLEACH | CDC, [Cleaning and Disinfecting with Bleach](https://www.cdc.gov/hygiene/about/cleaning-and-disinfecting-with-bleach.html) | Named section; unpaginated web page. |

## Source reuse

[CDC's agency-material policy](https://www.cdc.gov/other/agencymaterials.html) describes most agency text as public domain, with exceptions for third-party material and differing treatment outside the United States. It requires agency credit, no implied endorsement, no change to substantive content and a statement that the original is available free. This Knowledge Pack independently explains the cited factual guidance for children while preserving its meaning and qualifications; it does not reproduce agency artwork or third-party content.

[NIDCR's policy](https://www.nidcr.nih.gov/about-us/web-policies) permits use of its public-domain information with the publication title, URL, access date and agency credit. The advice to continue brushing without toothpaste is a practical inference from its explanation of brushing removing plaque and fluoride providing additional protection; it is not a quoted NIDCR fallback instruction. [NIDDK's policy](https://www.niddk.nih.gov/copyright) permits editing with no agency logos or implied endorsement; its sources are used here for general nutrition education and recognizing warning signs, not individualized diagnosis or treatment. [NHLBI's policy](https://www.nhlbi.nih.gov/about/contact/trademark-branding-and-logo) describes most information as public domain; this Knowledge Pack independently states facts from its sleep page and school asthma guide, and does not alter or distribute a formatted NHLBI publication.

[FDA's website policy](https://www.fda.gov/about-fda/about-website/website-policies), “Linking to or Copying Information on the FDA Website,” says its website content is public domain unless otherwise noted. It recommends giving the source link and copying date. The agency text of the cited tampon page was checked for exceptions; no restrictive notice applies to the factual guidance used here. The source is credited and dated above; no logos, images, linked third-party content or implied endorsement are included.

The American Dental Association's Toothbrushes page is copyright © 2026 American Dental Association, with no reuse statement on the page. Only its factual recommendations are stated here in our own words; none of its text or images is reproduced. The source page is not included or relicensed under MIT.

The HHS physical activity guidelines are a federal agency publication; only their factual recommendations are independently explained, with the publication credited. Its photographs, tables and layout are not reproduced.

WHO's Boil water brief is copyright WHO 2015, with no open license stated. Its conclusion is the basis of the adult boiling instruction, stated in our own words, as in the Water and Sanitation Knowledge Pack; no protected source prose, table, figure or layout is reproduced or adapted, and no MIT relicensing of the brief is claimed. The Yellow Book's Heat section is used for two facts, that the first small bubbles rising from the bottom are simmering and not boiling, and that CDC's extra minute is a margin of safety; its third-party figure is excluded. “Bubbling hard, with large bubbles breaking all over the surface” is our wording for the ordinary meaning of “rolling boil”.

MIT applies to the original AI-2 educational writing, not a claim to relicense an agency document or own public-domain facts. A rights specialist has not reviewed this use. No UNICEF publication is used.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it. Reviewers should compare each health instruction with its cited section and read each topic as the only help available offline. In particular, check child versus adult roles, missing supplies, the distinction between school attendance and urgent medical help, and the age range of every numeric recommendation.

The first reading, independent second reading and content review do not replace a teacher's reading or a clinician's reading. No teacher or clinician has reviewed this Knowledge Pack.
