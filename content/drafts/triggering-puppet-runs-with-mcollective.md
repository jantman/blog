Title: Triggering puppet runs with mcollective
Date: 2013-12-31 12:59
Author: admin
Category: Uncategorized
Slug: triggering-puppet-runs-with-mcollective
Status: draft

I've been running puppet in daemon mode for years, mainly due to my
desire to be able to use `puppet kick` to trigger immediate runs. With
puppet3, kick is deprecated, so I transitioned to mcollective. This
works fine for just getting Puppet to run, but in order to do a one-time
run with different parameters (like a different environment, with the
run triggered by a Jenkins job), that fails as the new puppet-agent
mcollective plugin just sends a SIGUSR1 if the daemon is already
running.

So, I needed to find an alternate method of achieving my goal - having
puppet run every 30 minutes on my nodes, but still being able to trigger
an immediate run with arbitrary arguments (environment, tags, etc).
[puppetcommander](https://projects.puppetlabs.com/projects/mcollective-plugins/wiki/ToolPuppetcommander)
looked like what I wanted, but unfortunately it doesn't support Puppet3
and the new puppetagent plugin. I posted a [thread to
puppet-users](https://groups.google.com/forum/#!topic/puppet-users/4SFwA42QJB8)
and got a very helpful response from [R. I.
Pienaar](http://www.devco.net/).
