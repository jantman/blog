Title: rspec-puppet tips
Date: 2014-10-15 07:34
Author: Jason Antman
Category: Puppet
Tags: puppet, rspec, testing
Slug: rspec-puppet-tips
Summary: Some tips on using rspec-puppet
Status: draft

Executing Commands as Other Users
---------------------------------

https://github.com/jantman/puppet-reviewboard/blob/current_module/spec/spec_helper.rb#L6

Testing Undef Parameters
-------------------------

https://github.com/jantman/puppet-reviewboard/blob/current_module/spec/spec_helper.rb#L10
https://github.com/jantman/puppet-reviewboard/blob/current_module/spec/defines/site_spec.rb#L83

Common Facts
------------

https://github.com/jantman/puppet-reviewboard/blob/current_module/spec/spec_helper.rb#L16

Testing the Resource Collection ("spaceship") Operator
-------------------------------------------------------

https://github.com/jantman/puppet-reviewboard/blob/current_module/spec/classes/traclink_spec.rb#L31

Testing Includes
-----------------

https://github.com/jantman/puppet-reviewboard/blob/current_module/spec/classes/traclink_spec.rb#L27

Beaker
------

