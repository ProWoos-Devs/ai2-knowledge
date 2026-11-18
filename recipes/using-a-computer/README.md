# using-a-computer

The mouse and touchpad, the keyboard, typing, windows, programs, files and folders, saving, keyboard shortcuts, what to do when something goes wrong, looking after the computer, passwords and staying safe, and asking AI-2 a question, for children ages 6 to 12 (`school-age` and `preteen`) using a computer for the first time, written for study and reference on an AI-2 machine with no connection.

Written rather than extracted, and not from any one source or school program. The AI-2 parts were checked against the AI-2 manual and a computer running AI-2 0.29.2. Two topics follow named sources, in their own words: the password advice follows CISA's "Use strong passwords" (https://www.cisa.gov/secure-our-world/use-strong-passwords), and the advice on strangers and personal details follows the U.S. Federal Trade Commission ("Do You Know Who Your Kids Are Talking To?", 2006, https://www.ftc.gov/news-events/news/press-releases/2006/05/do-you-know-who-your-kids-are-talking ; "COPPA: A few tips to keep your child safe online", 2019, https://consumer.ftc.gov/node/76733 ; and the 2026 consumer alert on deepfakes and the Take It Down Act, https://consumer.ftc.gov/consumer-alerts/2026/09/talking-parents-and-kids-about-deepfakes-online-safety-and-take-it-down-act). No teacher has reviewed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in using-a-computer --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export using-a-computer --manifest manifest.yml -o using-a-computer.ai2pack
```

## House style

- One subject per file, first line the title, then the search terms people would type.
- Every topic says "Written for AI-2. Directed to children, parents and teachers."
- Search shows passages of about 110 words, so each section is written to be understood without the ones before it. A number opens the whole topic.
- Only what has stayed the same for many years on any laptop or desktop computer. No brand names, models, program versions, screenshots or screen positions. Buttons and menus are described by what they do.
- Keys are named as printed on an English keyboard, with a line saying that other keyboards differ.
- The AI-2 parts (logging in, the Applications menu, Search Knowledge, AI-2 Chat) name the menu entries, which AI-2 keeps, and not today's layout. When AI-2 changes them, the topics get a new revision.
- Wall sockets are for grown-ups. No topic asks a child to plug anything into one, open a computer or clean it with liquid.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it. Check especially the steps for AI-2 against a computer running it, anything that is true on one kind of computer and not another, and the advice on passwords and strangers against its sources.

No teacher has reviewed this Knowledge Pack.
