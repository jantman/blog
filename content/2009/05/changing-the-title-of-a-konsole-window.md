Title: Changing the title of a Konsole window
Date: 2009-05-19 15:10
Author: admin
Category: Tech HowTos
Tags: kde, knosone
Slug: changing-the-title-of-a-konsole-window

For those of you who use KDE and Konsole, you can easily change the
title of the Konsole window with the command:

~~~~{.bash}
dcop $KONSOLE_DCOP_SESSION renameSession 'NewSessionName'
~~~~

this is pretty handy if, like me, you end up having a bunch of screen
sessions running in different Konsole windows.
