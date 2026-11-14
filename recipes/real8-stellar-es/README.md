# real8-stellar-es

REAL8 y Stellar, in Spanish, for beginners: what a wallet, a public address and a secret key are, keeping the key safe, how a Stellar payment works, trustlines, swaps, liquidity pools, changing cash for crypto and back through the wallet's MoneyGram option, mistakes that cannot be undone, and crypto scams. Every topic has a section on what works without a bank. Written by REAL8 about its own project, in its own wording, from its course "Introducción a la criptomoneda REAL8", the Stellar developer documentation, a Circle page and two FTC pages. The Stellar Development Foundation, MoneyGram, Circle and the FTC did not write or endorse it. It says nothing about what REAL8 or any other currency is worth, or whether to buy or sell.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in real8-stellar-es --embedder nomic-embed-text-v2-moe topics/*.txt
ai-2 knowledge export real8-stellar-es --manifest manifest.yml -o real8-stellar-es.ai2pack
```

The multilingual embedder is a 345 MB download the first time someone installs a Knowledge Pack built with it, against 85 MB for the English one. It is used here because it finds Spanish much better (see Measured).

## House style

The same as Finanzas básicas (real8-finanzas-es): one subject per file, the same eight sections, a source in square brackets on every instruction, a "Fuente" line defining every tag, and the gaps in the sources stated, not filled. Assets are identified by code and full issuer, never by name or logo. The wallet is described only at app.real8.org, where the course describes it.

## Sources and how they are cited

| In the topics | Source | Cited by |
|---|---|---|
| Curso M5 L3 | REAL8, Introducción a la criptomoneda REAL8, Spanish version, https://real8.org/es/courses/introduccion-a-la-criptomoneda-real8/ | module and lesson |
| Stellar glosario, cuentas, activos, lumens, transacciones, liquidez | Stellar developer documentation, Apache 2.0, https://developers.stellar.org/docs/learn/ (Glossary, Accounts, Assets, Lumens, Operations and Transactions, Liquidity on Stellar) | one page each |
| Circle USDC | Circle, USDC Contract Addresses, https://developers.circle.com/stablecoins/usdc-contract-addresses | the Stellar issuer row |
| FTC cripto | FTC, Lo que hay que saber sobre las criptomonedas y las estafas, https://consumidor.ftc.gov/articulos/lo-que-hay-que-saber-sobre-las-criptomonedas-y-las-estafas | one web page |
| FTC estafa | FTC, Cómo evitar una estafa, https://consumidor.ftc.gov/articulos/como-evitar-una-estafa | one web page |

No passage of the Stellar documentation is reproduced; the topics use its facts in REAL8's own words, MIT licensed.

## Measured

Built on 2026-11-14 with ai-2 0.29.2, 12 documents, 117 parts. An outside question set of 20, written by someone who had seen only the list of topic titles, searched with `ai-2 doc search` on the installed Knowledge Pack. No question was changed. With the English embedder nomic-embed-text-v1.5 it scored top-1 10/20, top-3 16/20; built with the multilingual embedder nomic-embed-text-v2-moe from the same topics it scores top-1 16/20, top-3 19/20, which is why this Knowledge Pack uses it.

One question ("me mandaron plata y no me aparece en la billetera") did not reach the trustlines topic in the top three. Of the three not ranked first, "cual es la diferencia entre la direccion publica y la clave secreta" found the wallet topic second, after keeping the secret key, "que dato le doy a alguien para que me pueda mandar cripto" found it third, and "un tipo por whatsapp me promete duplicar mis criptos si le mando primero" found the scams topic second, after cash.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
