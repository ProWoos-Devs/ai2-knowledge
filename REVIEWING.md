# Reviewing a Knowledge Pack

A Knowledge Pack is a set of short texts that an AI-2 computer searches with no Internet connection. Once it is on a machine it cannot correct itself, so a mistake stays there until a new revision is installed. That is why a second pair of eyes matters, and why anyone who knows the subject is welcome to check one.

You do not need to install anything, and you do not need to know how AI-2 works. You read the texts and tell us what is wrong.

## What to read

The texts of a Knowledge Pack made in this repository are in `recipes/<name>/topics/`, one plain text file per topic, usually a few hundred words each. The one exception is Everyday Reference, whose entries are generated from Wikidata, so its recipe holds the query and the rules, and its README says what to check. Start from the list at https://github.com/ProWoos-Devs/ai2-knowledge/tree/main/recipes , open a Knowledge Pack, then its `topics` folder, and click a file name to read it. No account is needed for reading.

The `README.md` beside the topics says who the Knowledge Pack is written for, what it was written from, and who has reviewed it so far.

You can review a whole Knowledge Pack or a few topics. Even one topic read carefully helps.

## What to look for

1. **Anything that is wrong.** A definition, a rule, a number, a dose, a worked example whose arithmetic does not come out, a unit conversion, a date.
2. **Anything stated as always true that has an exception the reader will meet.** Simplifying is fine. Teaching something that later has to be undone is not.
3. **Anything the intended reader would misunderstand.** A word used before it is explained, an example that does not match its rule, a sentence that can be read two ways. The README says who the reader is, and for a children's Knowledge Pack it gives the ages.
4. **Anything the reader is told or invited to do that is not safe**, and any safety advice that is missing or too absolute.
5. **Anything that does not match its source.** Some Knowledge Packs, such as First Aid and Water and Sanitation, cite a source and page for each instruction. If you have the source, check the instruction against it.
6. **Anything important that is missing** from a topic.

Read each topic as if it were the only help the reader has, with no way to look anything up, because for some readers it will be.

## What not to spend time on

Writing style and matters of taste. The texts use American spelling and metric units on purpose. The line "Search terms" near the top of a topic is a list of words for the search and is not meant to read as a sentence. Telephone numbers are left out of every Knowledge Pack on purpose.

## How to report

For each point, give four things:

- the Knowledge Pack and the file name, for example `basic-math`, `fractions-parts-of-a-whole.txt`
- the sentence, copied
- what is wrong
- how you would say it instead, and for a Knowledge Pack written from sources, the source and page that support the change

If a topic has nothing wrong, a line saying so is useful too, because it tells us the topic was read.

Send the list as one issue at https://github.com/ProWoos-Devs/ai2-knowledge/issues (this needs a free GitHub account). If you prefer to make the corrections yourself, [CONTRIBUTING.md](CONTRIBUTING.md#improving-an-existing-pack) says how to open a pull request.

## Being named

Each Knowledge Pack says in its own text who has reviewed it, for example "No teacher has reviewed it" or "Not reviewed by a clinician". If you are a teacher, a clinician or otherwise work in the subject and are willing to be named as a reviewer, say in your report how you would like to be credited. If you prefer not to be named, that is fine, and the text will say only that an independent reader checked it.

## Reviews by an AI assistant

A review may be done with an AI assistant, following this same page, and the report should say so. It is recorded as an AI-assisted review and does not replace a reading by a person who knows the subject. An example is https://github.com/ProWoos-Devs/ai2-knowledge/issues/11 .

## What happens next

Every point is checked and answered in the issue. Corrections are made by pull request and reach people's machines when the next revision of the Knowledge Pack is published.
