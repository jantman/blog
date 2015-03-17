Title: Some Additional Serverspec Types
Date: 2015-03-14 11:58
Author: Jason Antman
Category: Projects
Tags: serverspec, specinfra, testing, beaker, ruby, rspec, gem
Slug: some-additional-serverspec-types
Summary: Some additional types that I wrote for Serverspec

[Serverspec](http://serverspec.org/) is an rspec-based framework for testing live machines,
and making assertions about things like the output of commands, installed packages, running
services, file content, etc. However, it has a relatively limited and basic set of
[Resource Types](http://serverspec.org/resource_types.html) that it can test for.

Before Serverspec completely disabled their GitHub issue tracker (they now seem to have no
issue tracker at all), I'd suggested some improvements for more advanced resource types,
such as one that can perform an HTTP GET against an application and check the status code
and/or output. I was told in no uncertain terms that this is a task for application integration
testing, and that it's "not what Serverspec is for."

I humbly disagree. I've begun migrating my [Linode](https://www.linode.com/) to an EC2 machine,
using some technology that I've been using at my day job; specifically, Puppet to configure the
machine and [Packer](https://packer.io/) to build an AMI. Instead of using [Cloudformation](http://aws.amazon.com/cloudformation/)
to spin up an entire stack, I just use a Rakefile to spin up a new EC2 instance, test it, and
swap an [Elastic IP](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
if all the tests pass. Of course, this requires that I have relatively complete automated testing
of the EC2 instance. Stock Serverspec can handle 95% of what I want to test, but there are a few
other, more complex, things that it can't. So, I wrote some code to fix that.

I'll admit right off the bat that this code doesn't really work the way Serverspec is intended to,
but it works and it's relatively simple. This largely breaks the abstraction of serverspec using
[specinfra](https://github.com/serverspec/specinfra) under the hood, but I'm not sure if that's even
a concern (since specinfra seems to be all about testing a running machine via some local command
execution mechanism, and two of the types that I wrote use network IO instead).

For the time being, I've written three additional [types](http://www.rubydoc.info/gems/serverspec-extended-types/#Types)
that solve some specific use cases for me:

* A [bitlbee](http://www.rubydoc.info/gems/serverspec-extended-types/#bitlbee)
type that connects to a [Bitlbee](http://www.bitlbee.org/) IRC gateway, authenticates,
and checks the running bitlbee version. It has matchers to check whether or not the connection and
authentication was successful, whether or not it timed out, and the bitlbee version. Parameters for
the type include login nick and password, bitlbee port, and whether or not to connect with SSL.
* A [http_get](http://www.rubydoc.info/gems/serverspec-extended-types/#http_get)
type which connects to the system under test (with a specified port) and issues a
HTTP GET request for a specified path, with a specified ``Host`` header and a timeout (default
10 seconds). Matchers are provided for the response content body (string), response headers
(hash), HTTP status code, and whether or not the request timed out (which also sets a status of 0).
* A [virtualenv](http://www.rubydoc.info/gems/serverspec-extended-types/#virtualenv) type for testing
python [virtualenv](https://virtualenv.pypa.io/en/latest/)s. It takes the absolute path to the venv
on the filesystem, and uses serverspec's built-in file and command execution features to ensure that
the path "looks like" a virtualenv, and has matchers for the pip and python versions used in the venv
as well as the ``pip freeze`` output as a hash of requirements and their versions.

Hopefully this will be of use to someone else as well. As I continue using serverspec, I plan on
adding to the types.

The code for serverspec-extended-types is on [GitHub](https://github.com/jantman/serverspec-extended-types/tree/master)
(pull requests and issues welcome) and it's packaged and hosted as a [ruby gem](https://rubygems.org/gems/serverspec-extended-types).
[Installation](http://www.rubydoc.info/gems/serverspec-extended-types/0.0.2#Installation) and usage is as simple
as adding it to your Gemfile and [spec_helper](http://www.rubydoc.info/gems/serverspec-extended-types/0.0.2#Usage)
and then using the types and matchers in your specs.
