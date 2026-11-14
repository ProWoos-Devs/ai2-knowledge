# real8-finanzas-es

Finanzas básicas, in Spanish: ordering household money when it does not stretch, a simple budget, saving little by little, how a debt grows with interest, the full cost of sending money to another country, and how to recognize a scam. Every topic has a section on what works without a bank. Written by REAL8 in its own wording from public-domain sources of four United States agencies, mainly the CFPB's toolkit "Su dinero, sus metas". The CFPB, the FTC, the OCC and the FBI did not write or endorse it. It recommends no bank, company or product. Digital currencies are in the separate Knowledge Pack REAL8 y Stellar.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in real8-finanzas-es --embedder nomic-embed-text-v2-moe topics/*.txt
ai-2 knowledge export real8-finanzas-es --manifest manifest.yml -o real8-finanzas-es.ai2pack
```

The multilingual embedder is a 345 MB download the first time someone installs a Knowledge Pack built with it, against 85 MB for the English one. It is used here because it finds Spanish much better (see Measured).

## House style

- One subject per file, first line the title, then the search terms people would type, then who wrote it from what and that no financial adviser reviewed it, then who it is for and not for.
- Eight sections in every subject topic, in this order: USA ESTE TEMA CUANDO, QUÉ HACER, NO HAGAS, SI LAS COSAS CAMBIAN, SIN BANCO, LO QUE NO TIENE SUSTITUTO, DONDE LAS FUENTES NO DICEN NADA, QUEDA FUERA DE ESTE TEMA. SIN BANCO holds what works without a bank and what no bank will do for you.
- Each instruction cites its source in square brackets, and a "Fuente" line at the end defines every tag. Where the sources say nothing, the topic says so and nothing is added. United States figures, programs and agencies to report to are left out.
- Neutral Spanish. No prices, rates or limits, which go stale.

## Sources and how they are cited

| In the topics | Source | Cited by |
|---|---|---|
| SDSM p. 124 | CFPB, Su dinero, sus metas, Spanish edition dated October 2015, PDF published March 2016, https://files.consumerfinance.gov/f/201603_cfpb_your-money-your-goals_toolkit_spanish.pdf | PDF page |
| CFPB envíos | CFPB, Problems sending money to another country?, https://www.consumerfinance.gov/consumer-tools/sending-money/ | one web page |
| CFPB recibido menos | CFPB, I sent money to someone in a foreign country, but the amount received was less than what I sent, https://www.consumerfinance.gov/ask-cfpb/i-sent-money-to-someone-in-a-foreign-country-but-the-amount-received-was-less-than-what-i-sent-what-can-i-do-en-1745/ | one web page |
| CFPB datos | CFPB, I sent money to someone and they couldn't get the money because the information didn't match, https://www.consumerfinance.gov/ask-cfpb/i-sent-money-to-someone-and-they-couldnt-get-the-money-because-the-information-didnt-match-what-i-provided-what-can-i-do-en-1739/ | one web page |
| FTC estafa | FTC, Cómo evitar una estafa, https://consumidor.ftc.gov/articulos/como-evitar-una-estafa | one web page |
| OCC phishing | OCC, Phishing Attack Prevention, https://www.occ.treas.gov/topics/consumers-and-communities/consumer-protection/fraud-resources/phishing-attack-prevention.html | one web page |
| FBI https | FBI IC3, Cyber Actors Exploit 'Secure' Websites In Phishing Campaigns, https://www.ic3.gov/PSA/2019/PSA190610 | one web page |

All are works of the United States government and in the public domain. The topics are in REAL8's own words and MIT licensed.

## Measured

Built on 2026-11-14 with ai-2 0.29.2, 7 documents, 80 parts. An outside question set of 20, written by someone who had seen only the list of topic titles, searched with `ai-2 doc search` on the installed Knowledge Pack. No question was changed. With the English embedder nomic-embed-text-v1.5 it scored top-1 11/20, top-3 18/20; built with the multilingual embedder nomic-embed-text-v2-moe from the same topics it scores top-1 17/20, top-3 20/20, which is why this Knowledge Pack uses it.

The three not ranked first had the right topic second, behind the budget topic: "quiero juntar un dinerito para emergencias sin tener cuenta en el banco" and "consejos para guardar unos pesos cada semana" (saving), and "que es el interes compuesto en una deuda" (borrowing).

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
