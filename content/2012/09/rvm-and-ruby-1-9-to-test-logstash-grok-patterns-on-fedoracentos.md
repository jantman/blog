Title: RVM and Ruby 1.9 to test logstash grok patterns on Fedora/CentOS
Date: 2012-09-03 08:37
Author: admin
Category: Tech HowTos
Tags: grok, grokparsefailure, jruby, kibana, logstash, ruby, rvm
Slug: rvm-and-ruby-1-9-to-test-logstash-grok-patterns-on-fedoracentos

I've been working on a personal project with [Logstash][] lately, and it
relies relatively heavily on [grok][] filters for matching text and
extracting matched parts. Today, I've been parsing syslog from
[Puppet][] to extract various metrics and timings, which will then be
passed on from Logstash to [Etsy's statsd][] and then to [graphite][]
for display. Unfortunately, a few of my patterns are showing the
"\_grokparsefailure" tag and I just can't seem to find the problem.

The logstash wiki provides a page on [Testing your Grok patterns][], as
does Sean Laurent on his blog: [Testing Logstash grok filters][].
Unfortunately, I work in a CentOS/RHEL shop, and we're decidedly *not* a
Ruby shop. Our Logstash install is using the monolithic/standalone Java
JAR. We run Puppet, which is currently under ruby 1.8.7, and the
[jls-grok rubygem][] requires ruby 1.9. There's no way I'd feel safe
installing 1.9 on any of our machines, as they all run (and require)
Puppet. So, I found out about [RVM][], the Ruby Version Manager, which
allows you to run and switch between multiple ruby versions, and all of
it is installed on a per-user basis. So, I created a new user on my
Fedora 16 desktop called "rvmtest" and went about the process of setting
up what's needed to test grok patterns in the user's local environment.
I imagine this would work similarly under CentOS or RHEL, but the
following is only tested on Fedora 16. If you have any issues, you
should probably refer back to the RVM documentation.

1.  Create the isolated user, just to be extra careful. Login as that
    user.
2.  As per [Installing RVM][]:
    `curl https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer | bash -s stable`
3.  edit your `~/.bashrc` and add:

~~~~{.bash}
[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
[[ -r $rvm_path/scripts/completion ]] && . $rvm_path/scripts/completion
~~~~

    <p>
    The first line sets up RVM for your sessions, and the second sources
    in tab-completion for the `rvm` command.

4.  `source .bashrc`
5.  If you're interested, you can see a list of all known rubies with:
    `rvm list known`
6.  Install Ruby (MRI) 1.9.2: `rvm install 1.9.2`
7.  "switch" to that ruby: `rvm use 1.9.2` and confirm it by running
    `ruby -v`
8.  Make it the default ruby for us: `rvm use 1.9.2 --default`
9.  Create a "gemset" (set of rubygems for our environment):
    `rvm gemset create groktest`
10. Use it, and set it as default: `rvm use 1.9.2@groktest --default`
11. for grok testing, `gem install jls-grok`
12. check that it's there: `gem list`
13. Download Logstash's default grok patterns [from github][]
14. You should now be ready to test some grok patterns.

While the two howto's linked above use `irb` to interactively test the
patterns, I prefer something easier to move to production, more
reliable, and more repeatable. The following quick little ruby script
takes test to match against on STDIN (log files, messages, etc.) and
prints the matches to STDOUT. The script is based on [test.rb][] from
[jordansissel's ruby-grok][]. Note one important thing here, I couldn't
get the shebang (`#!`) to work with anything other than the explicit
path to my RVM ruby install (`which ruby`) so you'll need to manually
update this yourself.

~~~~{.ruby}
#!.rvm/rubies/ruby-1.9.2-320bin/ruby

require 'rubygems'
require 'grok-pure'
require 'pp'

grok = Grok.new
grok.add_patterns_from_file("grok-patterns")

pattern = 'your_grok_pattern_here'
grok.compile(pattern)
puts "PATTERN: #{pattern}"

while a = gets
  puts "IN: #{a}"
  match = grok.match(a)
  if match
    puts "MATCH:"
    pp match.captures
  else
    puts "No Match."
  end
end
~~~~

Here's an example using a pattern to capture information from custom
syslog messages triggered by updating puppet configs. Here's some sample
messages:

~~~~{.text}
[rvmtest@jantmanwork ~]$ cat puppet.log
Updated 2 files in puppet svn (environment prod) to revision 754
Updated 3 files in puppet svn (environment prod) to revision 756
Updated 1 files in puppet svn (environment prod) to revision 757
~~~~

And the pattern that I use:

~~~~{.text}
Updated%{SPACE}%{NUMBER:puppet_svn_num_files}%{SPACE}files%{SPACE}in%{SPACE}puppet%{SPACE}svn%{SPACE}\(environment%{SPACE}%{WORD:puppet_svn_env}\)%{SPACE}to%{SPACE}revision%{SPACE}%{NUMBER:puppet_svn_revision}
~~~~

And the output of the script:

~~~~{.text}
[rvmtest@jantmanwork ~]$ cat puppet.log | ./puppet-update-test.rb 
PATTERN: Updated%{SPACE}%{NUMBER:puppet_svn_num_files}%{SPACE}files%{SPACE}in%{SPACE}puppet%{SPACE}svn%{SPACE}\(environment%{SPACE}%{WORD:puppet_svn_env}\)%{SPACE}to%{SPACE}revision%{SPACE}%{NUMBER:puppet_svn_revision}
IN: Updated 2 files in puppet svn (environment prod) to revision 754
MATCH:
{"SPACE"=>[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
 "NUMBER:puppet_svn_num_files"=>["2"],
 "BASE10NUM"=>["2", "754"],
 "WORD:puppet_svn_env"=>["prod"],
 "NUMBER:puppet_svn_revision"=>["754"]}
IN: Updated 3 files in puppet svn (environment prod) to revision 756
MATCH:
{"SPACE"=>[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
 "NUMBER:puppet_svn_num_files"=>["3"],
 "BASE10NUM"=>["3", "756"],
 "WORD:puppet_svn_env"=>["prod"],
 "NUMBER:puppet_svn_revision"=>["756"]}
IN: Updated 1 files in puppet svn (environment prod) to revision 757
MATCH:
{"SPACE"=>[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
 "NUMBER:puppet_svn_num_files"=>["1"],
 "BASE10NUM"=>["1", "757"],
 "WORD:puppet_svn_env"=>["prod"],
 "NUMBER:puppet_svn_revision"=>["757"]}
~~~~

Hopefully this will make the process a bit simpler for someone else...

  [Logstash]: http://logstash.net/
  [grok]: https://github.com/jordansissel/grok
  [Puppet]: http://puppetlabs.com/puppet/puppet-open-source/
  [Etsy's statsd]: https://github.com/etsy/statsd
  [graphite]: http://graphite.wikidot.com/
  [Testing your Grok patterns]: https://github.com/logstash/logstash/wiki/Testing-your-Grok-patterns-(--logstash-1.1.0-and-above-)
  [Testing Logstash grok filters]: http://blog.bealetech.com/content/testing-logstash-grok-filters
  [jls-grok rubygem]: http://rubygems.org/gems/jls-grok
  [RVM]: https://rvm.io/
  [Installing RVM]: https://rvm.io/rvm/install/
  [from github]: https://raw.github.com/logstash/logstash/master/patterns/grok-patterns
  [test.rb]: https://github.com/jordansissel/ruby-grok/blob/master/examples/test.rb
  [jordansissel's ruby-grok]: https://github.com/jordansissel/ruby-grok
