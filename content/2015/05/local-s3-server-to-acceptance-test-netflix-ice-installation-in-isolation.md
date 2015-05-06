Title: Local S3 Server to Acceptance Test Netflix Ice Installation In Isolation
Date: 2015-05-05 06:45
Author: Jason Antman
Category: Tech HowTos
Tags: netflix, ice, puppet, beaker, acceptance testing, aws, s3, fakes3, testing
Slug: local-s3-server-to-acceptance-test-netflix-ice-installation-in-isolation
Summary: How I wrote isolated acceptance tests for Netflix Ice Puppet installation using a locally-backed S3 API server.
Status: draft

At work, we recently started using [Netflix OSS](http://netflix.github.io/)'s [Ice](https://github.com/Netflix/ice) AWS cost analysis tool.
It provides a Java daemon to read and parse AWS' [detailed billing reports](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/detailed-billing-reports.html)
and a web interface to the data ([screenshots](https://github.com/Netflix/ice/blob/master/README.md#screenshots)). The single biggest feature for us
is the ability to do cost breakdowns (by hour/day/week/month) based on Cost Allocation tags in the detailed billing reports. We tag every billable AWS
resource with the Application Name, Service Class (environment; dev/test/prod) and Responsible Party. Ice lets us configure "Application Groups"
based on applications as seen from a business/budgetary standpoint and allow up-to-the-hour data on that available to anyone who needs it.

We spun up the development install of Ice for a few weeks to give it a spin, but once people started complaining that my screen session died and took
Ice with it, it was clear we needed a real, permanent installation. While there is [chef](https://github.com/mdsol/ice_cookbook) and [ansible](https://github.com/Answers4AWS/netflixoss-ansible)
code to install and configure Ice, we're a Puppet shop, and there wasn't anything available that I could find for Puppet. So, I set about writing a
module to install and configure Ice, running in Tomcat behind an Nginx proxy. Like any good modern module, I wanted not only [rspec-puppet](http://rspec-puppet.com/)
unit tests but also [beaker](https://github.com/puppetlabs/beaker) acceptance tests. For those unfamiliar, Beaker is an acceptance testing framework for Puppet
that's similar to Test Kitchen; it spins up Vagrant machines, runs some code in them, and then uses [serverspec](http://serverspec.org/) to make assertions about
the state of the system (file contents, running processes, command output, etc.) (side note: if you used Beaker prior to the
[2.0 release](https://github.com/puppetlabs/beaker/blob/master/HISTORY.md#beaker2.0.0) in December 2014, you should really try it again; they've made some great
improvements).

The Problem
------------

This posed a bit of a challenge, as Ice (in addition to being pretty poorly documented) is really designed to run in AWS. Firstly, the very reason we started running Ice was
to get a handle on our fast-growing AWS spend; as a result, we're trying hard not to use AWS for small-scale projects that could use existing resources. Second, while our
company very unfortunately doesn't have an open source policy and isn't releasing anything (hopefully this may be changing soon), we try hard to write generic, forge-quality
modules.

As a result, I wanted to use the default Vagrant/VirtualBox provider for Beaker. To make matters worse, in keeping with the spirit of a community module, I didn't
want the acceptance tests to require anything specific to my company, such as an S3 bucket preseeded with our billing data. Ice both reads the detailed billing reports
(one of its three inputs; EC2 pricing data and your accounts' reservation pricing/capacity being the others) and writes state from and to S3. So, this was a bit difficult.
As we don't plan on upgrading Ice terribly often, and we wanted to install from the [cloudbees master builds](https://netflixoss.ci.cloudbees.com/job/ice-master/), we wanted
acceptance testing of not just the provisioning tooling, but also some basic smoke tests for the application itself.

The Solution
-------------

I managed to come up with a working, albeit somewhat Rube Goldberg, method of getting isolated acceptance tests to work. What follows is the gist of how I got Ice
working in complete isolation. The majority of this happens in ``spec/acceptance/0prerequisite_spec.rb`` which runs first and both does the prerequisite setup
and validates that everything is setup right and working for the tests. The following solution is based on the amazingly helpful [fakes3](https://github.com/jubos/fake-s3)
Ruby gem, the [Pound](http://www.apsis.ch/pound/) reverse proxy, and some SSL certificate trickery. While my code was specific to Beaker, this should be generic
enough to use with any system acceptance testing tool.

Prerequisites
--------------

First, we obtain or create some files that we'll need on the test instance:

1. Grab a relatively recent Detailed Billing With Resources and Tags zipped CSV report from an AWS account of yours (the filename is in the format
   ``<ACCOUNT NUMBER>-aws-billing-detailed-line-items-with-resources-and-tags-<YYYY>-<MM>.csv``). Manually trim it down to a sufficient sample of data;
   I took a few hours' worth of data from one day and trimmed it down to just that referencing a few randomly chosen RDS instances, ELBs, on-demand EC2
   instances and reserved EC2 instances. I then anonymized the account number, resource IDs, tag values, and anything else identifying. Ice needs billing
   data in order to do anything, so this will serve as our test data.
2. When Ice runs, it attempts to retrieve reserved instance pricing. It appears (I've lost the mailing list or GitHub issue reference) that it's typical for
   the first Ice run on an empty S3 work directory to die because these files are missing. As a result, grab the ``reservation_prices.oneyear.*`` files from
   the S3 work bucket of a running/working Ice installation. This will prevent a time-consuming shutdown of Ice on the first run.
3. Generate a self-signed SSL key and certificate for ``fakebucket.s3.amazonaws.com``. Package them together in a PEM file suitable for use in web servers.
   (Note that most modern S3 API clients accept a full URL to a bucket, as there are now third parties that implement the S3 API. Ice does not; it connects
   to https://BUCKETNAME.s3amazonaws.com. As a result, this SSL foolery is required.)

Setup
------

1. Install the [fakes3](https://rubygems.org/gems/fakes3) rubygem; this provides an s3-compliant API backed by local filesystem storage.
   Configure it to run during your tests (I set it up as a systemd service, but there are certainly other ways to do this). Note that
   while fakes3 stores the uploaded data on the local filesystem, it maintains a mapping of known objects in memory; as such, the process
   always starts completely empty, regardless of what's in the backing directory on the filesystem. fakes3 allows all IAM credentials,
   so fake ones are fine. It also automatically creates buckets the first time they're accessed.
2. Install the [pound](http://www.apsis.ch/pound/) reverse proxy and configure it to listen on port 443 with the PEM file you generated
   earlier, and proxy to fakes3 (which listens by default on port 10000). The ``ListenHTTPS``section of ``pound.cfg`` will need the
   ``xHTTP 1`` directive in order to enable HTTP verbs other than GET.
3. Setup a local hosts file entry pointing ``fakebucket.s3.amazonaws.com`` at ``127.0.0.1``.
4. After fakes3 starts, upload your sample billing data file and your reserved instance pricing files to the appropriate paths under a
   bucket called "fakebucket". You can use a tool such as [s3cmd](http://s3tools.org/s3cmd) to manipulate its contents, and other
   supported tools are listed in [the documentation](https://github.com/jubos/fake-s3/wiki/Supported-Clients). This step also serves
   to validate your Pound configuration, which should pass HTTPS port 443 traffic through to fakes3 and allow you to store and
   retrieve objects.
5. Figure out the path to the trusted keystore for the version of Java that you're running Ice under. On CentOS 7 with OpenJDK 1.7.0,
   this was (after a lot of symlinks) ``/usr/lib/jvm/jre/lib/security/cacerts``.
6. Import your self-signed certificate into the Java keystore as a trusted certificate. This will allow SSL verification to succeed even
   with a self-signed certificate:
   ``/bin/keytool -importcert -alias fakebucket -file fakebucket.s3.amazonaws.com.crt -keystore /usr/lib/jvm/jre/lib/security/cacerts -storepass changeit -trustcacerts -noprompt``
7. Configure ``ice.properties`` for the above. The important and unintuitive parts that I found are:

   1. Going by the above examples, your billing and work S3 bucket names should both be "fakebucket".
   2. Unless you want to mock out bigger parts of the AWS metadata service, run Ice with
   ``-Dice.s3AccessKeyId=NotAValidAccessKeyId -Dice.s3SecretKey=NotAValidAwsSecretKeyXxxxxxxxxxxxxxxxxxx``
   in the ``JAVA_OPTS``. If Ice can't retrieve an instance's IAM role from the metadata service
   (http://169.254.169.254/latest/meta-data/iam/security-credentials/) and doesn't have the
   access and secret keys defined, it won't run. Also note that while the documentation is __very__
   unclear on this, a number of [github issues](https://github.com/Netflix/ice/issues/49#issuecomment-23497701)
   clarify that these need to be passed in as Java runtime options; they can't be put in the properties file.
   3. Disable the Reservation Capacity Poller (``ice.reservationCapacityPoller=false``). This service
   needs to connect to the EC2 API, and will cause Ice to die if it can't.
   4. For testing purposes, it's a lot simpler and less error-prone (as well as being a lot faster) to
   test the processor and reader separately - at least in serial instead of simultaneously in the same instance.

Once all this is done, running the Ice Processor should retrieve the billing file, process it, and write the processed data to the
fakes3 bucket. Running the Reader should display the data properly. So far I've been unable to find any features (other than the
Reservation Capacity Poller, noted above) that don't work with this setup.

Whether it's related to Ice itself or ideas for acceptance testing isolated applications, I hope this can be of use to someone...
