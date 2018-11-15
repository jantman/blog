Title: Handling mailto links on another computer
Date: 2010-11-16 11:34
Author: admin
Category: Software
Tags: firefox, Thunderbird
Slug: handling-mailto-links-on-another-computer

At work, I use [synergy](http://synergy-foss.org/) to control two
computers with the same mouse and keyboard. My main desktop (skynet) has
two monitors - generally one for Firefox and one for my terminals - and
my secondary machine (mithrandir), a third monitor on my desk, handles
email and IM. The only real problem I've had with this is mailto: links,
which obviously don't work since my browser and mail client are on
different computers.

Getting cross-machine mailto links to work isn't all that difficult, at
least with thunderbird which accepts a "-compose" command line argument.
First, get passwordless pubkey SSH authentication setup from the web
browser machine to the mail client machine. Then set your mailto
handler/mail client to a shell script in your path. Finally, fill the
script in with something like:

~~~~{.bash}
#!/bin/bash
ssh mithrandir "export DISPLAY=:0.0 && thunderbird -compose '$@'"
~~~~

This first sets the DISPLAY environment variable so thunderbird can open
a window in the already-running X session, then invokes thunderbird
passing it the mailto: link as an argument to -compose. Note the single
quotes which prevent spaces in the link from breaking things.
