# living-things

Plants, animals, cells, habitats, food webs, senses and the body's movement, circulation, breathing and digestion for children ages 6 to 12 (`school-age` and `preteen`), with parents and teachers helping. Written for study and reference on an AI-2 machine with no connection. Categories: `'11.09'` Biology; `'13.01'` Anatomy and physiology; `'07.05'` Primary and secondary education. Audience: `children`. Language: English. License: MIT for the original writing. Contact: ProWoos-Devs.

Written for AI-2. Directed to children, parents and teachers.

Original educational explanations written from the cited agency facts and educational guidance, with original paper examples. The sources are the U.S. National Park Service, U.S. Fish & Wildlife Service, U.S. Department of Agriculture, National Oceanic and Atmospheric Administration, and National Institutes of Health. These organizations and the United States Government did not write or endorse this Knowledge Pack. Source documents, photographs, illustrations, videos, logos and worksheets are not included.

A first reading against REVIEWING.md and the saved source passages has been completed, with corrections recorded in the working files. The independent second reading and content review have not taken place. No teacher or clinician has reviewed this Knowledge Pack.

There are no telephone numbers here, or in any Knowledge Packs.

## Rebuilding

```
ai-2 doc index --in living-things --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export living-things --manifest manifest.yml -o living-things.ai2pack
```

## House style

- One subject per plain text file: title, search terms and the exact children's audience line, then short sections.
- Fourteen subject topics of about 400 prose words, excluding citations, plus Start here and About. The longer About topic carries the complete source key for offline readers.
- Each section explains its terms before developing the idea. Examples use descriptions and paper drawings; each anatomy topic can be read on its own.
- Citations identify the factual basis by source code and section. `Web` means an unpaginated web page. Printed and PDF page numbers are distinguished. Sources were consulted on 2026-11-11.
- Search displays passages of about 110 words, so important qualifications belong beside the statement they qualify. A result can be relevant without answering the question.
- American spelling and metric units. The topics explain biology and anatomy, with no diagnosis, treatment, medicine doses or health experiments.

## Sources and how they are cited

The source codes and titles below also appear in the offline About topic. The manifest attaches a primary source to each subject document by its exact `.txt` filename; the topic citations identify additional sources and sections. The source register in the working files identifies the saved passages used for the first reading. Sources are references for independently written explanations, not redistributed source texts.

| Code | Source | Sections or pages |
| --- | --- | --- |
| S1 | [National Park Service, Alive in Dyke Marsh](https://www.nps.gov/teachers/classrooms/alive-in-dyke-marsh.htm) | Background; web, unpaginated. |
| S2 | [National Park Service, Plant Adaptations](https://www.nps.gov/teachers/classrooms/plant-adaptations.htm) | Background; Plant Structures and Functions; Cacti; Juniper; web, unpaginated. |
| S3 | [U.S. Fish & Wildlife Service, Attracting Pollinators to Your Garden (2011)](https://www.govinfo.gov/content/pkg/GOVPUB-I49-PURL-gpo58962/pdf/GOVPUB-I49-PURL-gpo58962.pdf) | PDF pp. 3–4, What is Pollination? and Meet the Pollinators; no printed numbers. |
| S4 | [National Park Service, Vertebrate Fossils](https://www.nps.gov/subjects/fossils/vertebrate-fossils.htm) | Introduction, for the backbone distinction; web, unpaginated. |
| S5 | [National Park Service, Monarch Butterfly, Featured Creature](https://www.nps.gov/articles/000/monarch-butterfly-featured-creature.htm) | Distribution and Habitat; Behavior and Diet; Life Cycle; web, unpaginated. |
| S6 | [NOAA, Aquatic food webs](https://www.noaa.gov/education/resource-collections/marine-life/aquatic-food-webs) | What is a food web?; diagram caption; Producers; Consumers; Who cleans up the leftovers?; Trophic cascades; web, unpaginated. |
| S7 | [NIH/NCI SEER, Cell Structure & Function](https://training.seer.cancer.gov/anatomy/cells_tissues_membranes/cells/) | Cell Structure & Function; web, unpaginated. |
| S7A | [NIH/NCI SEER, Cell Structure](https://training.seer.cancer.gov/anatomy/cells_tissues_membranes/cells/structure.html) | Cell membrane; Nucleus and Nucleolus; Cytoplasm; Cytoplasmic organelles; web, unpaginated. |
| S7B | [NIH/NCI SEER, Cell Function](https://training.seer.cancer.gov/anatomy/cells_tissues_membranes/cells/function.html) | Cell Function; movement across membranes; Cell division; DNA replication and protein synthesis; web, unpaginated. |
| S8 | [NIH/NCI SEER, Introduction to the Skeletal System](https://training.seer.cancer.gov/anatomy/skeletal/) | Support/protection, living bone and marrow; web, unpaginated. |
| S8A | [NIH/NCI SEER, Articulations](https://training.seer.cancer.gov/anatomy/skeletal/articulations.html) | Articulations; Synarthroses; Amphiarthroses; Diarthroses; web, unpaginated. |
| S9 | [NIH/NCI SEER, Introduction to the Muscular System](https://training.seer.cancer.gov/anatomy/muscular/) | Movement, posture and joint stability; web, unpaginated. |
| S9A | [NIH/NCI SEER, Structure of Skeletal Muscle](https://training.seer.cancer.gov/anatomy/muscular/structure.html) | Structure of Skeletal Muscle; web, unpaginated. |
| S9B | [NIH/NCI SEER, Muscle Types](https://training.seer.cancer.gov/anatomy/muscular/types.html) | Skeletal, Smooth and Cardiac Muscle; web, unpaginated. |
| S10 | [NIH/NCI SEER, Introduction to the Nervous System](https://training.seer.cancer.gov/anatomy/nervous/) | Sensory input, integration and motor output; web, unpaginated. |
| S10A | [NIH/NCI SEER, The Central Nervous System](https://training.seer.cancer.gov/anatomy/nervous/organization/cns.html) | Opening explanation; Spinal Cord; web, unpaginated. |
| S10B | [NIH/NCI SEER, The Peripheral Nervous System](https://training.seer.cancer.gov/anatomy/nervous/organization/pns.html) | Opening explanation; Structure of a Nerve; Autonomic Nervous System; web, unpaginated. |
| S11 | [NIH/NHLBI, How the Heart Works, The Heart](https://www.nhlbi.nih.gov/health/heart) | The Heart; web, unpaginated. |
| S11A | [NIH/NHLBI, How Blood Flows through the Heart](https://www.nhlbi.nih.gov/health/heart/blood-flow) | Opening explanation; Heart valves; Adding oxygen to blood; Supplying oxygen to the heart's muscle; web, unpaginated. |
| S12 | [NIH/NHLBI, How the Lungs Work, The Lungs](https://www.nhlbi.nih.gov/health/lungs) | The Lungs; web, unpaginated. |
| S12A | [NIH/NHLBI, What Breathing Does for the Body](https://www.nhlbi.nih.gov/health/lungs/breathing-benefits) | Breathing in; Gas exchange; Breathing out; web, unpaginated. |
| S12B | [NIH/NHLBI, The Respiratory System](https://www.nhlbi.nih.gov/health/lungs/respiratory-system) | Opening explanation; Airways; Air comes into your body; web, unpaginated. |
| S13 | [NIH/NIDDK, Your Digestive System & How it Works](https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works) | Named sections on the tract, digestive movements/juices, absorption, Large intestine and Rectum; web, unpaginated. |
| S14 | [National Park Service, Mammals of the Everglades](https://www.nps.gov/ever/learn/kidsyouth/mammals-of-the-everglades.htm) | Opening mammal requirements and examples; web, unpaginated. |
| S15 | [National Park Service, Birds of the Everglades](https://www.nps.gov/ever/learn/kidsyouth/birds-of-the-everglades.htm) | Opening flight discussion, including flightless birds; web, unpaginated. |
| S16 | [National Park Service, Reptiles of the Everglades](https://www.nps.gov/ever/learn/kidsyouth/reptiles-of-the-everglades.htm) | Reptile examples and hatching; web, unpaginated. |
| S17 | [National Park Service, Amphibians of the Everglades](https://www.nps.gov/ever/learn/kidsyouth/amphibians-of-the-everglades.htm) | Skin and life-cycle discussion; web, unpaginated. |
| S18 | [National Park Service, Types of Fish](https://www.nps.gov/subjects/fishing/typesoffish.htm) | Opening fish physical features; web, unpaginated. |
| S19 | [National Park Service, Insects, Spiders, Centipedes, Millipedes, Everglades](https://www.nps.gov/ever/learn/nature/insects.htm) | Insects and Arachnids; web, unpaginated. |
| S20 | [NIH/NEI, How the Eyes Work](https://www.nei.nih.gov/eye-health-information/healthy-vision/how-eyes-work) | How the Eyes Work; web, unpaginated. |
| S21 | [NIH/NIDCD, How Do We Hear?](https://www.nidcd.nih.gov/health/how-do-we-hear) | Hearing steps 1–6; web, unpaginated. |
| S22 | [NIH/NIDCD, Smell Disorders](https://www.nidcd.nih.gov/health/smell-disorders) | How does your sense of smell work?; web, unpaginated. |
| S23 | [NIH/NIDCD, Taste Disorders](https://www.nidcd.nih.gov/health/taste-disorders) | How does your sense of taste work?; web, unpaginated. |
| S24 | [NIH, Sharon Reynolds, Characterizing what human sensory nerves can sense](https://www.nih.gov/news-events/nih-research-matters/characterizing-what-human-sensory-nerves-can-sense) | General sensory explanation and human sensory-neuron findings; web, unpaginated. |
| S26 | [NOAA Ocean Exploration, What is the difference between photosynthesis and chemosynthesis?](https://oceanexplorer.noaa.gov/ocean-fact/photochemo/) | Photosynthesis explanation; web, unpaginated. |
| S27 | [NIH/NLM MeSH, Germination](https://www.ncbi.nlm.nih.gov/mesh/68018525) | Germination, MeSH D018525, retrieved 2026-11-11; web, unpaginated. |
| S28 | [NIH/NIDCD, Balance Disorders](https://www.nidcd.nih.gov/health/balance-disorders) | How does my body keep its balance?; web, unpaginated. |
| S29 | [USDA NRCS, Seedbed Preparation and Seed to Soil Contact, Technical Note 6 (2005)](https://www.nrcs.usda.gov/plantmaterials/wapmctn6330.pdf) | PDF p. 1, Section 6.1 Seed to Soil Contact; no printed page number. |
| S30 | [National Park Service, Home Sweet Home, third-grade activity guide](https://www.nps.gov/common/uploads/teachers/lessonplans/Home%20Sweet%20Home%20Activity%20Guide.pdf) | Printed pp. 1 and 5, Background and Everything Is Connected. |
| S31 | [National Park Service, Adaptations](https://www.nps.gov/teachers/classrooms/adaptations.htm) | Background and Vocabulary; web, unpaginated. |
| S32 | [NIH/NLM MeSH, Plant Stems](https://www.ncbi.nlm.nih.gov/mesh/68018547) | Plant Stems, MeSH D018547, retrieved 2026-11-11; web, unpaginated. |
| S33 | [National Park Service, Blue in the Face: Breathing Underwater](https://www.nps.gov/articles/blue-in-the-face-breathing-underwater.htm) | So, how do gills work?; web, unpaginated. |
| S34 | [National Park Service, Trees: The Inside Story](https://www.nps.gov/teachers/classrooms/trees-the-inside-story.htm) | Roots; Leaves; Trunks; web, unpaginated. |
| S35 | [National Park Service, Birds, Cabrillo National Monument](https://www.nps.gov/cabr/learn/nature/birds.htm) | All About Birds; Physical Characteristics; web, unpaginated. |

## Source reuse

The [National Park Service's Ownership policy](https://www.nps.gov/aboutus/disclaimer.htm) describes agency-created material as generally public domain, while retaining exceptions for outside contributions and protected marks. The [Department of the Interior's policy](https://www.doi.gov/copyright) makes the same distinction for its agencies, including the U.S. Fish & Wildlife Service. No claim to original U.S. Government works. Credit is given by agency, publication title and source link; no agency artwork or marks are reproduced.

[NOAA's content-use guidance](https://www.noaa.gov/office-education/outreach-communication/faq) permits use of most agency material with source credit, attention to outside credits, no implied endorsement and clear identification of changes. These explanations are original writing for AI-2 from the cited facts, not official NOAA text. The [USDA policy](https://www.usda.gov/about-usda/policies-and-links), Digital Rights and Copyright, describes most agency information as public domain with exceptions. The NRCS seed-development passage is used for its factual explanation, with agency credit; its diagram and other source material are not reproduced.

[NCI's reuse policy](https://www.cancer.gov/policies/copyright-reuse) describes its text as copyright free unless otherwise indicated and asks for source credit and the original title/link. The SEER material supplies anatomical facts for these original explanations; its formatted lessons, clinical material, graphics and logos are not reproduced.

[NHLBI's policy](https://www.nhlbi.nih.gov/about/contact/trademark-branding-and-logo) describes most information as public domain, while asking that formatted publications and multimedia not be changed and that endorsement not be implied. Only agency-written factual explanations are used here, independently stated; no animations or other formatted products are copied. Source: National Heart, Lung, and Blood Institute; National Institutes of Health; U.S. Department of Health and Human Services. Third-party medical animations and illustrations on those pages are excluded.

[NIDDK's policy](https://www.niddk.nih.gov/copyright) permits use of most text, with exceptions for outside material, no logos or endorsement, and limits on using edited content for specific medical advice or referrals. The use here explains digestion. [NEI's policy](https://www.nei.nih.gov/web-policies/copyright-policy) permits use of most agency text with credit. Courtesy: National Eye Institute, National Institutes of Health (NEI/NIH). [NIDCD's policy](https://www.nidcd.nih.gov/policies), Copyright Policy, similarly describes most text as public domain, with outside-material exceptions. The NIH touch explanation is used for its general sensory facts under the [NIH copyright guidance](https://www.nih.gov/about-nih/frequently-asked-questions), not for treatment advice or reproducing its licensed photograph.

The [NLM MeSH terms](https://www.nlm.nih.gov/databases/download/terms_and_conditions_mesh.html) permit use with clear source credit and no implied endorsement, and require a version or currency statement for redistributed information. The facts cited here use NLM MeSH entries Germination (D018525) and Plant Stems (D018547), as retrieved on 2026-11-11. This offline writing does not reflect later changes to those entries. Their credited dictionary wording is not copied; the underlying facts are explained independently. No rights over NLM data or its source dictionary are claimed.

MIT applies to the original educational writing. The source publications keep their own rights or public-domain status. A rights specialist has not reviewed this use.

## Reviewing

Follow [REVIEWING.md](../../REVIEWING.md) for every reading. Compare factual statements with their cited sections, including the saved copies when a source site cannot be opened. Check exceptions to simple rules, child-level definitions, organism versus life-stage distinctions, food-web arrow direction and the separate paths of air, blood and food. The independent second reading must take place before the separate content review and recipe pull request.

No teacher or clinician has reviewed this Knowledge Pack. No search measurement has been made.
