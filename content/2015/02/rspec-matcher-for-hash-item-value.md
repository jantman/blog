Title: RSpec Matcher For Hash Item Value
Date: 2015-02-21 10:33
Author: Jason Antman
Category: Software
Tags: ruby, rspec, spec, testing
Slug: rspec-matcher-for-hash-item-value
Summary: An RSpec matcher for hash item value regex

__Update:__ Well, this is embarassing. _After_ I posted this, I received a
[comment](http://blog.jasonantman.com/2015/02/rspec-matcher-for-hash-item-value/#comment-1868422853)
within a few hours from [@myronmarston](https://twitter.com/myronmarston). I'd originally
written this matcher for RSpec2, and then had to convert my project to use
RSpec3. I just blindly converted this matcher over. Myron pointed out that with
RSpec3's [composable matchers](http://rspec.info/blog/2014/01/new-in-rspec-3-composable-matchers/),
the functionality of this gem is built-in. It can be done as simply as:

~~~~{.ruby}
its(:headers) { should include('server' => /nginx\/1\./) }
~~~~

__As such, I've yanked them gem and am leaving the code and blog post here just for posterity.__
This should probably not be used.

I've been working on a project to move my [Linode](http://linode.com) VM to an
Amazon EC2 instance; the entire instance is a "baked" AMI built by Puppet. Since
I'd like to be able to rebuild this quickly, I'm using [ServerSpec](http://serverspec.org/)
(which I have some non-technical issues with, but that's a long story) to run full
integration tests of the whole system - check that packages are installed, services
are running, and even make live HTTP requests agsinst it.

One part of this was making live HTTP requests (from inside ServerSpec / [rspec](http://rspec.info/))
and checking HTTP response headers. Unfortunately, RSpec doesn't have a nice, clean way to make
assertions about a hash item.

So, I wrote a little Ruby Gem to do this, [rspec-matcher-hash-item](https://github.com/jantman/rspec-matcher-hash-item). At the moment it just
has one matcher, ``have_hash_item_matching``. This operates on a hash, and takes two arguments,
a key and a regex for the value. It allows me to do simple but useful things like:

~~~~{.ruby}
  describe http_get(80, 'testapp1.jasonantman.com', '/testapp1234') do
    its(:headers) { should have_hash_item_matching('server', /nginx\/1\./) }
  end
~~~~

(The ``http_get`` serverspec matcher is coming in a future gem and blog post)

Among other things, it prints diffs on failure:

~~~~
  2) privatepuppet::ec2::vhosts::testapp1 Http_get "" headers should include key 'server' matching /badvalue/
     On host `54.149.198.147'
     Failure/Error: its(:headers) { should have_hash_item_matching('server', /badvalue/) }
       expected that hash[server] would match /badvalue/
       Diff:
       @@ -1,2 +1,6 @@
       -["server", /badvalue/]
       +"connection" => "close",
       +"content-type" => "text/plain",
       +"date" => "Sat, 21 Feb 2015 16:07:42 GMT",
       +"server" => "nginx/1.6.2",
       +"transfer-encoding" => "chunked",
~~~~

Using the gem is as simple as including it in your ``Gemfile``:

    gem "rspec-matcher-hash-item"

And adding a line to your ``spec_helper.rb``:

    require 'rspec_matcher_hash_item'

Note that the gem is written for RSpec3.

This is available at [rubygems.org](https://rubygems.org/gems/rspec-matcher-hash-item) or from
[GitHub](https://github.com/jantman/rspec-matcher-hash-item). See GitHub for the documentation.
