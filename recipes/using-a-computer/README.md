# using-a-computer

The mouse and touchpad, the keyboard, typing, windows, programs, files and folders, saving, keyboard shortcuts, what to do when something goes wrong, looking after the computer, passwords and staying safe, and asking AI-2 a question, for children ages 6 to 12 (`school-age` and `preteen`) using a computer for the first time, written for study and reference on an AI-2 machine with no connection.

Written rather than extracted, and not from any one source or school program. The AI-2 parts were checked against the AI-2 manual and a computer running AI-2 0.29.2, and again on AI-2 0.29.3 with the USB stick topic, 0.29.3 being the first version that opens a USB stick in the File Manager. Three topics follow named sources, in their own words: the password advice follows CISA's "Use strong passwords" (https://www.cisa.gov/secure-our-world/use-strong-passwords), and the advice on strangers and personal details follows the U.S. Federal Trade Commission ("Do You Know Who Your Kids Are Talking To?", 2006, https://www.ftc.gov/news-events/news/press-releases/2006/05/do-you-know-who-your-kids-are-talking ; "COPPA: A few tips to keep your child safe online", 2019, https://consumer.ftc.gov/node/76733 ; and the 2026 consumer alert on deepfakes and the Take It Down Act, https://consumer.ftc.gov/consumer-alerts/2026/09/talking-parents-and-kids-about-deepfakes-online-safety-and-take-it-down-act), and the warning about found USB sticks follows CISA's "The Risks of Using Portable Devices" (https://www.cisa.gov/sites/default/files/publications/RisksOfPortableDevices.pdf). No teacher has reviewed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in using-a-computer --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export using-a-computer --manifest manifest.yml -o using-a-computer.ai2pack
```

## Measured

Built on 2026-11-18 with ai-2 0.29.3: 17 documents, 99 parts. An outside question set, written by someone who had seen only the list of topic titles, searched with `ai-2 doc search` on the built Knowledge Pack. All 20 questions were kept and none was changed: top-1 15/20, top-3 17/20.

The five that did not come first: "how do i make the arrow move" found the mouse and touchpad topic second, after windows on the screen; "can i ask the computer a question like talking to a robot" found the asking topic second, after Start here; and "where are the games", "what should we read first" and "what is this help for and what age is it for" did not find the topic wanted (finding a program, Start here, About) in the top three.

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
