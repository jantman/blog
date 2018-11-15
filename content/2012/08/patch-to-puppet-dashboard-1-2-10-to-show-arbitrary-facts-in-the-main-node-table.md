Title: Patch to Puppet Dashboard 1.2.10 to show arbitrary facts in the main node table
Date: 2012-08-11 10:34
Author: admin
Category: Software
Tags: dashboard, facts, puppet, ruby, sysadmin
Slug: patch-to-puppet-dashboard-1-2-10-to-show-arbitrary-facts-in-the-main-node-table

We use [Puppet
Dashboard](http://puppetlabs.com/puppet/related-projects/dashboard/) at
work to view the status of our puppet nodes. While it's very handy,
there's one feature I really wanted: the ability to show the value of
arbitrary puppet facts in the main node table on the home page.
Specifically, the facts we use for environment (we have eng/dev, qa,
prod, and test puppet environments), zone (physical location) and last
applied configuration version. I'm not terribly experience with Ruby,
but I managed to muddle my way through a working patch to do this, along
with options in the settings file to enable it and configure the facts.
You'll need to restart dashboard (or your web server) to change the
facts, of course. The commit is currently [available on
github](https://github.com/jantman/puppet-dashboard/commit/5364e2b0188d18ae62c355279e58c7ce6d7db654),
but it doesn't strictly follow the [puppet-dashboard contributing
checklist](https://github.com/puppetlabs/puppet-dashboard/blob/master/CONTRIBUTING.md)
so I may have to redo it.

Here's a screenshot:

[![Dashboard screenshot after
patch](/GFX/dashboard_after_patch_sm.png)](/GFX/dashboard_after_patch.png)

And here's that the configuration section added to settings.yml looks
like:

~~~~{.yaml}
# Enables display of arbitrary node facts in "home" page node table, between node name and latest report time
enable_home_facts: true

# If enable_home_facts is true, the fact names and column headings to display. Simply repeat the following two line pairs
# as needed:
#- name: 'factname'
#  heading: 'heading text'
home_facts: 
- name: 'environment'
  heading: 'Env'
- name: 'zone'
  heading: 'Zone'
- name: 'catalog_config_version'
  heading: 'Cfg Ver'
~~~~

If I feel really adventurous, I'd like to implement my other big wish,
some sort of pop-up list of links, based on arbitrary facts (mainly
hostname and fqdn) for each node - something where I can mouse over the
node name/table cell, and see links (static URLs with node
name/fqdn/other facts plugged in) to things like Nagios/Icinga, our
backup system, etc.
