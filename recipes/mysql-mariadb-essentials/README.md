# mysql-mariadb-essentials

Everyday MySQL and MariaDB, written as the questions people ask when they set up or use a database: the server will not start, access denied, a slow query, a backup to make and restore, accents turned into question marks. Every topic covers both servers, and says so where they differ.

Written rather than extracted. The MariaDB documentation and the MySQL 8.4 Reference Manual are the reference, and nothing is copied from either. The MySQL manual's terms do not allow its text in another publication, so these topics state facts about the commands in their own words.

AI-2's repositories carry MariaDB, so the AI-2 steps (installing, starting, logging in as root) are written for MariaDB, with the MySQL equivalent beside them.

## Rebuilding

```
ai-2 doc index --in mysql-mariadb-essentials --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export mysql-mariadb-essentials --manifest manifest.yml -o mysql-mariadb-essentials.ai2pack
```

## House style

- One subject per file, roughly 150 to 250 words, first line the title.
- Open with the situation in the reader's words ("Cannot connect to the local server through socket"), not with the statement's name.
- Show the SQL or the command to type, then say what it does and what can go wrong.
- Say the AI-2 truth where it differs from generic advice: the server is started with runit (`sv`, `artix-service`), not systemd, the socket is `/run/mysqld/mysqld.sock`, and root logs in with `sudo mariadb`.
- Anything that destroys data (DELETE, TRUNCATE, ALTER, a restore) comes with the way to check first and the backup to take.

## Checked against

The AI-2 facts were read from the Artix packages `mariadb` 13.0.2, `mariadb-clients` and `mariadb-runit` on 2026-11-17. Every SQL statement and error message was run on MariaDB 13.0.2. The MySQL differences are stated from the MySQL 8.4 Reference Manual and were not run on a MySQL server. No outside database administrator has reviewed the text yet.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it.
