Title: Puppet facter fact for all applied classes, returned as a CSV list
Date: 2012-08-22 07:05
Author: admin
Category: Software
Tags: classes, csv, fact, facter, node, puppet
Slug: puppet-facter-fact-for-all-applied-classes-returned-as-a-csv-list

I'm unfortunatey stuck, at least for the time being, using flat-file
manifests to configure my puppet nodes. Without an ENC, it's pretty
difficult to get a good ovewview of what classes are used on each node,
and what nodes use a given class. I know I could write up a simple web
tool to do this (unfortunately, given my limited Ruby knowledge, it
would have to be in PHP or Perl, not a real modification to Dashboard in
Ruby). But where to get the data from?

After some research, I found a [puppet fact for puppet
classes](http://sjoeboo.github.com/blog/2012/07/31/updated-puppet-facts-for-puppet-classes/)
on [Matthew Nicholson's Coffee & Beer blog](http://sjoeboo.github.com/).
It parses `/var/lib/puppet/classes.txt` and returns the list of classes
found as a JSON array. Great base, but I wanted something easier, that
would be more easily parsed from its direct storage in MySQL. My
modification to his code is onlty a few characters; I dropped out the
JSON require, and return the classes as a CSV list. This lets me to easy
`LIKE '%,classname,%'` SELECTs in MySQL, and also gives me the fact
value stored in the puppet DB, so I can build a separate tool around
that data. Thanks, Matt.

~~~~{.ruby}
#
# facter fact for puppet classes on node, pulled from /var/lib/puppet/classes.txt
# from 
#

require 'facter'
begin
        Facter.hostname
        Facter.fqdn
rescue
        Facter.loadfacts()
end
hostname = Facter.value('hostname')
fqdn = Facter.value('fqdn')

classes_txt = "/var/lib/puppet/classes.txt"

if File.exists?(classes_txt) then
        f = File.new(classes_txt)
        classes = Array.new()
        f.readlines.each do |line|
                line = line.chomp.to_s
                line = line.sub(" ","_")
                classes.push(line)
        end
        classes.delete("settings")
        classes.delete("#{hostname}")
        classes.delete("#{fqdn}")
        Facter.add("puppet_classes_csv") do
                setcode do
                        classes.join(",")
                end
        end
end
~~~~

All of my facts are now available in a GitHub repository:
[https://github.com/jantman/puppet-facter-facts](https://github.com/jantman/puppet-facter-facts).
