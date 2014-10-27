Title: Pushover Notifications for Shell Command Completion and Status
Date: 2014-09-27 21:20
Author: Jason Antman
Category: Tech HowTos
Tags: pushover, shell, notifications
Slug: pushover-notifications-for-shell-command-completion-and-status
Summary: How to get pushover notifications of shell command completion and status

Lately I've been doing a bunch of work with [packer](http://www.packer.io/) building [Vagrant](http://www.vagrantup.com/)
machine images, and using [serverspec](http://serverspec.org/) to run automated acceptance tests on the images. Unfortunately,
this ends up being a ~40-minute cycle time for the full image to provision and test. So, lots of watching text slowly scroll
down a screen, and finding something else to do. It's the weekend; I want to get this project finished, but I've got other
things to do.

So, I wrote a little bash wrapper around [jnwatts'](https://github.com/jnwatts)
[pushover.sh](https://raw.githubusercontent.com/jnwatts/pushover.sh/master/pushover.sh). Assuming wherever you put this
is in your path, simply prefix any command with ``pushover ``, and you'll get a handy [Pushover](https://pushover.net/)
notification when it completes, along with the exit status and some other useful information.

~~~~{.bash}
#!/bin/bash
#
# Notify command completion and exit status via pushover
# uses pushover.sh from https://raw.githubusercontent.com/jnwatts/pushover.sh/master/pushover.sh
#

APIKEY="Your Pushover API Key Here"
USERKEY="Your Pushover User Key Here"

stime=$(date '+%s')
$@
exitcode=$?
# timer
etime=$(date '+%s')
dt=$((etime - stime))
ds=$((dt % 60))
dm=$(((dt / 60) % 60))
dh=$((dt / 3600))
times=$(printf '%d:%02d:%02d' $dh $dm $ds)
# end timer
if [ "$exitcode" -eq 0 ]
then
    pushover.sh -p 0 -t "Command Succeeded" -T "$APIKEY" -U "$USERKEY" "succeeded in ${times} on $(hostname): $@ (in $(pwd))"
    echo "(sent pushover success notification)"
else
    pushover.sh -p 0 -s falling -t "Command Failed" -T "$APIKEY" -U "$USERKEY" "failed in ${times} (exit $exitcode) on $(hostname): $@ (in $(pwd))"
    echo "(sent pushover failure notification)"
fi

~~~~

So, for example, a failing spec test:

    jantman@phoenix:pts/4:~/CMG/git/puppet-cm (AUTO-415=)$ pushover bundle exec rake spec
	<lots of failing spec output that exits non-0 after 1 minute 10 seconds>
	(sent pushover failure notification)
	jantman@phoenix:pts/4:~/CMG/git/puppet-cm (AUTO-415=)$ 

Would send me a handy pushover message when it finishes:

    Command Failed
	failed in 0:01:10 (exit 1) on phoenix: bundle exec rake spec (in /home/jantman/CMG/git/puppet-cm)

Hopefully this is useful to someone else as well...
