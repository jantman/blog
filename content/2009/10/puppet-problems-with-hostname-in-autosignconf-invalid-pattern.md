Title: Puppet problems with hostname in autosign.conf - Invalid pattern
Date: 2009-10-14 14:45
Author: admin
Category: Puppet
Tags: autosign.conf, hostname, puppet
Slug: puppet-problems-with-hostname-in-autosignconf-invalid-pattern

In playing with Puppet (0.24.8 on clients and server) today (well,
building a new host) I came by a strange error when I ran puppet on the
client:

~~~~{.text only}
err: Could not request certificate: Certificate retrieval failed: Invalid pattern css-storemanager
~~~~

The thing that was so strange is that "css-storemanager" is the name of
a host at my site, controlled by Puppet, but it has nothing to do with
the host I was building. They're different boxes, on different subnets,
in different rooms. One is a SunFire and the other is an HP desktop.

Google turned up nothing. Running puppetmasterd with `--debug --trace`
yielded:

~~~~{.text only}
info: Listening on port 8140
notice: Starting Puppet server version 0.24.8
notice: Allowing unauthenticated client ccf-hill019-12.example.edu(172.x.x.x) access to puppetca.getcert
/usr/lib/ruby/site_ruby/1.8/puppet/network/authstore.rb:289:in `parse'
/usr/lib/ruby/site_ruby/1.8/puppet/network/authstore.rb:170:in `pattern='
/usr/lib/ruby/site_ruby/1.8/puppet/network/authstore.rb:151:in `initialize'
/usr/lib/ruby/site_ruby/1.8/puppet/network/authstore.rb:80:in `new'
/usr/lib/ruby/site_ruby/1.8/puppet/network/authstore.rb:80:in `store'
/usr/lib/ruby/site_ruby/1.8/puppet/network/authstore.rb:20:in `allow'
/usr/lib/ruby/site_ruby/1.8/puppet/network/handler/ca.rb:54:in `autosign?'
/usr/lib/ruby/site_ruby/1.8/puppet/network/handler/ca.rb:51:in `each'
/usr/lib/ruby/site_ruby/1.8/puppet/network/handler/ca.rb:51:in `autosign?'
/usr/lib/ruby/site_ruby/1.8/puppet/network/handler/ca.rb:50:in `open'
/usr/lib/ruby/site_ruby/1.8/puppet/network/handler/ca.rb:50:in `autosign?'
/usr/lib/ruby/site_ruby/1.8/puppet/network/handler/ca.rb:112:in `getcert'
/usr/lib/ruby/site_ruby/1.8/rubygems/custom_require.rb:31:in `to_proc'
/usr/lib/ruby/site_ruby/1.8/puppet/network/xmlrpc/processor.rb:52:in `call'
/usr/lib/ruby/site_ruby/1.8/puppet/network/xmlrpc/processor.rb:52:in `protect_service'
/usr/lib/ruby/site_ruby/1.8/puppet/network/xmlrpc/processor.rb:85:in `setup_processor'
/usr/lib/ruby/1.8/xmlrpc/server.rb:336:in `call'
/usr/lib/ruby/1.8/xmlrpc/server.rb:336:in `dispatch'
/usr/lib/ruby/1.8/xmlrpc/server.rb:323:in `each'
/usr/lib/ruby/1.8/xmlrpc/server.rb:323:in `dispatch'
/usr/lib/ruby/1.8/xmlrpc/server.rb:366:in `call_method'
/usr/lib/ruby/1.8/xmlrpc/server.rb:378:in `handle'
/usr/lib/ruby/site_ruby/1.8/puppet/network/xmlrpc/processor.rb:44:in `process'
/usr/lib/ruby/site_ruby/1.8/puppet/network/xmlrpc/webrick_servlet.rb:68:in `service'
/usr/lib/ruby/1.8/webrick/httpserver.rb:104:in `service'
/usr/lib/ruby/1.8/webrick/httpserver.rb:65:in `run'
/usr/lib/ruby/1.8/webrick/server.rb:173:in `start_thread'
/usr/lib/ruby/1.8/webrick/server.rb:162:in `start'
/usr/lib/ruby/1.8/webrick/server.rb:162:in `start_thread'
/usr/lib/ruby/1.8/webrick/server.rb:95:in `start'
/usr/lib/ruby/1.8/webrick/server.rb:92:in `each'
/usr/lib/ruby/1.8/webrick/server.rb:92:in `start'
/usr/lib/ruby/1.8/webrick/server.rb:23:in `start'
/usr/lib/ruby/1.8/webrick/server.rb:82:in `start'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:293:in `start'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:144:in `newthread'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:143:in `initialize'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:143:in `new'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:143:in `newthread'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:291:in `start'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:290:in `each'
/usr/lib/ruby/site_ruby/1.8/puppet.rb:290:in `start'
/usr/sbin/puppetmasterd:285
err: Invalid pattern css-storemanager
~~~~

After a bit of investigation into that trace, I found the following code
in `/usr/lib/ruby/site_ruby/1.8/puppet/network/authstore.rb` starting on
line 242:

~~~~ {lang="ruby" line="242"}
            # Parse our input pattern and figure out what kind of allowal
            # statement it is.  The output of this is used for later matching.
            def parse(value)
                case value
                when /^(\d+\.){1,3}\*$/: # an ip address with a '*' at the end
                    @name = :ip
                    match = $1
                    match.sub!(".", '')
                    ary = value.split(".")

                    mask = case ary.index(match)
                    when 0: 8
                    when 1: 16
                    when 2: 24
                    else
                        raise AuthStoreError, "Invalid IP pattern %s" % value
                    end

                    @length = mask

                    ary.pop
                    while ary.length < 4
                        ary.push("0")
                    end

                    begin
                        @pattern = IPAddr.new(ary.join(".") + "/" + mask.to_s)
                    rescue ArgumentError => detail
                        raise AuthStoreError, "Invalid IP address pattern %s" % value
                    end
                when /^([a-zA-Z][-\w]*\.)+[-\w]+$/: # a full hostname
                    @name = :domain
                    @pattern = munge_name(value)
                when /^\*(\.([a-zA-Z][-\w]*)){1,}$/: # *.domain.com
                    @name = :domain
                    @pattern = munge_name(value)
                    @pattern.pop # take off the '*'
                    @length = @pattern.length
                else
                    # Else, use the IPAddr class to determine if we've got a
                    # valid IP address.
                    if value =~ /\/(\d+)$/
                        @length = Integer($1)
                    end
                    begin
                        @pattern = IPAddr.new(value)
                    rescue ArgumentError => detail
                        raise AuthStoreError, "Invalid pattern %s" % value
                    end
                    @name = :ip
                end
~~~~

Following the trace back, I took a look at
`/usr/lib/ruby/site_ruby/1.8/puppet/network/handler/ca.rb` starting at
line 50:

~~~~ {lang="ruby" line="50"}
            auth = Puppet::Network::AuthStore.new
            File.open(autosign) { |f|
                f.each { |line|
                    next if line =~ /^\s*#/
                    next if line =~ /^\s*$/
                    auth.allow(line.chomp)
                }
            }
~~~~

After looking at this, it clicked that it must be what evaluates
autosign.conf. Taking a look at mine, one line stood out: a line
containing only "css-storemanager", not a FQDN like all the rest. The
parse() function in authstore.rb only accepts IP addresses and FQDNs (or
IP addresses ending in a wildcard, or wildcard FQDNs). It appears to
choke on hostnames (a string that doesn't match an FQDN or IP).
Interestingly, it also evaluates in order, and stops evaluating
autosign.conf once it finds a match. So, if you're a Bad Person like me,
and left autosign turned on for all of your hosts, you wouldn't notice
this until you try and build a new box.

To solve this, just remove any offending lines from autosign.conf.

I've filed a bug report on the Puppet Trac: [Issue
2723](http://projects.reductivelabs.com/issues/2723).
