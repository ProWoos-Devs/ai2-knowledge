# historia-hispanica-mitos-es

Mitos y hechos de la historia hispánica, in Spanish, for the general reader: forty questions people ask about the history of Spain and of the Hispanic world, each answered from the articles of Hispanopedia. The Leyenda Negra, the conquests of Mexico and Peru, what the Indians died of, the laws that protected them, encomienda and mita, slavery, colonies or viceroyalties, the Inquisition and its figures, witches, mestizaje, universities, the smallpox vaccine expedition, the first voyage round the world, the Manila Galleon, the real de a ocho, the Reconquista, Lepanto, the Armada of 1588, the English expedition of 1589, Blas de Lezo, Bernardo de Gálvez and others. Every topic opens with the common myths on its question and the fact beside each one. It also states the facts that do not favor Spain when the article gives them.

Written by Hispanopedia from its own encyclopedia, https://es.hispanopedia.com/ , in its own wording. No historian outside Hispanopedia has reviewed it.

There is no present-day politics here, and no telephone numbers, as in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in historia-hispanica-mitos-es --embedder nomic-embed-text-v2-moe topics/*.txt
ai-2 knowledge export historia-hispanica-mitos-es --manifest manifest.yml -o historia-hispanica-mitos-es-r1.ai2pack
```

The multilingual embedder is a 345 MB download the first time someone installs a Knowledge Pack built with it, against 85 MB for the English one. It is used here because the text is Spanish. On an Acer ES1-522 (AMD, two threads) indexing the 42 files took about an hour and a quarter.

## House style

One question per file, the same sections in the same order: `Términos de búsqueda`, the source line, `Para` and `No para`, MITOS, RESPUESTA CORTA, LOS HECHOS (ten to twenty numbered facts, one thing each), DONDE LA FUENTE NO DICE NADA, QUEDA FUERA DE ESTE TEMA, PARA SABER MÁS and a `Fuente` line. Every fact carries a tag in square brackets naming the Hispanopedia article and the section the datum is in, and the `Fuente` line defines every tag. The gaps in the sources are stated, not filled.

The works under PARA SABER MÁS are the ones each article lists in its own bibliography or references. The topics were not checked against them, and each topic says so.

Hispanopedia's own conventions hold: offices and institutions are capitalized (Rey, Virrey, Cabildo), the Spanish territories of America and the Philippines are called virreinatos, reinos and provincias, and the war of 1808 to 1814 is the Invasión Napoleónica de España.

## Sources and how they are cited

Every topic comes from one to three articles of Hispanopedia, published under CC BY-SA 4.0, read on 15 November 2026. Part of Hispanopedia's articles derive from Spanish Wikipedia under the same license. `manifest.yml` gives the first article of each topic, and the topic's own `Fuente` line gives all of them with their addresses. A tag reads `[HP short name, section]`.

No passage of an article is reproduced beyond short quotations the articles themselves quote, such as clause XI of the codicil of Isabel la Católica. The topics restate the articles' facts in plainer words.

## How it was checked

Each topic was written only from the saved text of its articles. A second reading, by a reader who had not written the topic, then compared every claim, figure, date, name and tag with the article and corrected what did not match. Corrections were needed in 39 of the 40 topics, most often a phrase that said slightly more than the article does.

That reading establishes that a topic says what its article says. It does not establish that the article is right. Where an article contradicted itself or gave two figures for the same thing, the topic leaves the datum out. The contradictions found were noted so the articles can be corrected.

## Measured

Built on 2026-11-16 with ai-2 0.29.2, 42 documents, 937 parts, 2,992,966 bytes. An outside question set of 20, written by a reader who had seen only the list of topic titles, searched with `ai-2 doc search` on the Knowledge Pack installed in a clean directory. No question was changed. It scored top-1 16/20 and top-3 18/20.

Two questions did not reach their topic in the top three: "quien se invento lo de que los españoles eran unos salvajes" (the Leyenda Negra topic) and "el almirante cojo, manco y tuerto que derroto a los ingleses" (the Blas de Lezo topic, although those words are among its search terms). Two reached it second or third: "xq en latinoamerica hay tanta mezcla de razas y en estados unidos no" found the mestizaje topic third, and "a la armada invencible la hundieron los ingleses o las tormentas" found the Armada topic second, after the English expedition of 1589.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it. An error that comes from the Hispanopedia article can also be corrected there.
