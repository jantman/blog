Title: Puppet facter fact for last applied configuration version
Date: 2012-08-21 08:55
Author: admin
Category: Software
Tags: config_version, fact, facter, puppet
Slug: puppet-facter-fact-for-last-applied-configuration-version

For anyone else who sets the Puppet `config_version` paramater to return
the current SVN or Git version of your configuration, here's a fact that
grabs that version (by parsing the cached YAML catalog) and sets it as a
fact called "catalog\_config\_version". It can then be used for
sanity-checking your nodes, looking up via the Inventory Service, or you
can display it in the Dashboard using my patch: [Patch to Puppet
Dashboard 1.2.10 to show arbitrary facts in the main node
table](http://blog.jasonantman.com/2012/08/patch-to-puppet-dashboard-1-2-10-to-show-arbitrary-facts-in-the-main-node-table/).

~~~~{.ruby}
#
# facter fact for last applied config version, skeleton from /var/lib/puppet/client_yaml/catalog/fqdn.yaml
#

require 'puppet'
require 'yaml'
require 'facter'

localconfig = ARGV[0] || "#{Puppet[:clientyamldir]}/catalog/#{ Facter.fqdn }.yaml"

unless File.exist?(localconfig)
  puts("Can't find #{ Facter.fqdn }.yaml")
  exit 1
end

lc = File.read(localconfig)

begin
  pup = Marshal.load(lc)
rescue TypeError
  pup = YAML.load(lc)
rescue Exception => e
  raise
end

if pup.class == Puppet::Resource::Catalog
        Facter.add("catalog_config_version") do
                setcode do
                        pup.version
                end
        end
else
        Facter.add("catalog_config_version") do
                setcode do
                        "unknown"
                end
        end
end
~~~~

All of my facts are now available in a GitHub repository:
[https://github.com/jantman/puppet-facter-facts](https://github.com/jantman/puppet-facter-facts).
