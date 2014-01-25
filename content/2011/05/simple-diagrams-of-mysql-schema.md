Title: Simple Diagrams of MySQL Schema
Date: 2011-05-04 08:47
Author: admin
Category: Tech HowTos
Tags: database, db, diagram, mysql, sql
Slug: simple-diagrams-of-mysql-schema

Jess Robinson's
[SQL-Translator](http://search.cpan.org/~jrobinson/SQL-Translator/) CPAN
module translates and parses SQL statements. The
[SQLfairy](http://sqlfairy.sourceforge.net/) project has some nice
binaries that, among other things, use GraphViz or GD to draw pseudo-ER
diagrams from SQL CREATE statements. Drawing a diagram of an SQL schema
is as easy as
`sqlt-diagram --db=MySQL -o schema.png -i png -t "title" --color --gutter 100 -c 2 schema-erd.sql`.
There are a few minor issues - the program seems to choke on the LOCK
TABLES statements in `mysqldump` output. But overall, the results are
quite nice. The script can take (as easy as putting it in a Makefile)
mysqldump output and generate a diagram like the one below, including
foreign key constraints. I also found a simple intro and example in a
post on [Neil
Saunders](http://nsaunders.wordpress.com/2009/01/11/easy-visualisation-of-database-schemas-using-sqlfairy/)'
blog.

![sqlfairy output](/GFX/sqlfairy.png)
