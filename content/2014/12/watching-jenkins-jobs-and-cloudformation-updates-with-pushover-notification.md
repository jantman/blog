Title: Watching Jenkins Jobs and CloudFormation Updates with Pushover Notification
Date: 2014-12-14 19:22
Author: Jason Antman
Category: Tech HowTos
Tags: script, pushover, jenkins, hudson, aws, cloudformation
Slug: watching-jenkins-jobs-and-cloudformation-updates-with-pushover-notification
Summary: Some scripts to watch the status of Jenkins jobs and CloudFormation updates, and send Pushover notifications.

A few months ago I [posted](http://blog.jasonantman.com/2014/09/pushover-notifications-for-shell-command-completion-and-status/)
about a script I wrote to send [Pushover](https://pushover.net/) notifications for shell command completion.

I've been doing quite a bit of work lately both with testing some [Jenkins](http://jenkins-ci.org/) jobs, and spinning up
AWS stacks using [CloudFormation](https://aws.amazon.com/cloudformation/). Last week I wrote two python scripts to aid in this.

[watch_cloudformation.py](https://github.com/jantman/misc-scripts/blob/master/watch_cloudformation.py) uses the popular [boto](https://github.com/boto/boto)
Python AWS interface to list (and display) the events on a specified CloudFormation stack, and exit 0 or 1 when it finds a (CREATE|UPDATE)_(FAILED|COMPLETE) event.
It also optionally uses [python-pushover](https://pypi.python.org/pypi/python-pushover) to send the notification to your devices via Pushover.

[watch_jenkins.py](https://github.com/jantman/misc-scripts/blob/master/watch_jenkins.py) takes the URL to a Jenkins job or build, and uses
[python-jenkins](https://pypi.python.org/pypi/python-jenkins) to poll the status of the build (or the latest build, if given a Job url)
and display the result when the build finishes, also optionally using python-pushover to send notifications to your device.

They're really quick-and-dirty scripts and might not be suitable for everyone's use case, but I took the time to write them,
so hopefully they'll be useful to someone else.
