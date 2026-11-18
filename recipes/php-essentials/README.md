# php-essentials

Everyday PHP, written as the questions people ask when they write or fix a script: a blank page, an error message, a form, a database query, a password to store, a file to upload. Secure coding runs through it, because code that works but can be broken into is not working.

Written rather than extracted. The PHP Manual is the reference for every function named here, and nothing is copied from it. A manual answers "what does this function do", while these topics answer "what do I do now", which is what a person types into a search with no Internet.

## Rebuilding

```
ai-2 doc index --in php-essentials --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export php-essentials --manifest manifest.yml -o php-essentials.ai2pack
```

## Measured

Built on 2026-11-17 with ai-2 0.29.2: 23 documents, 75 parts. An outside question set, written by someone who had seen only the list of topic titles, searched with `ai-2 doc search` on the built Knowledge Pack. All 20 questions were kept and none was changed: top-1 17/20, top-3 19/20.

The three that did not come first: "safe way to save user pasword in database" found the passwords topic second, after keeping secrets out of code; "failed to open stream no such file or directory include header.php" found the include topic third; and "check if mbstring is enabled" did not find the version and extensions topic in the top three.

## House style

- One subject per file, roughly 150 to 250 words, first line the title.
- Open with the situation in the reader's words ("A blank page or a 500 error"), not with the function's name.
- Show the code to type, then say what it does and what can go wrong.
- Say the AI-2 truth where it differs from generic advice: PHP's configuration is `/etc/php/php.ini`, `pdo_mysql` and `mysqli` are switched off until enabled there, the web server user is `http`, and services are runit (`sv`), not systemd.
- Only long-standing core PHP, nothing tied to one minor release, so the text holds while the Knowledge Pack sits on a machine that cannot update.
- Security practice belongs in the topic where the risk is: escaping where output is printed, placeholders where queries are run.

## Checked against

The AI-2 facts were read from the Artix packages `php` 8.5.12, `php-fpm` and `php-fpm-runit` on 2026-11-17. Every code example was run on PHP 8.5.12. No outside PHP developer has reviewed the text yet.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
