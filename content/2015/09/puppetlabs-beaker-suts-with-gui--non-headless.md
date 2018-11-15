Title: Puppetlabs Beaker SUTs with GUI / Non-Headless
Date: 2015-09-19 11:09
Author: Jason Antman
Category: Software
Tags: puppet, beaker, sut, rspec, virtualbox, headless, GUI
Slug: puppetlabs-beaker-suts-with-gui--non-headless
Summary: How to enable the GUI / disable headless mode on a puppetlabs Beaker SUT.

[Beaker](https://github.com/puppetlabs/beaker/) is a puppetlabs tool for automating acceptance testing
of puppet modules; in most common use cases, it uses a [Vagrant](https://www.vagrantup.com/)/
[virtualbox](https://www.virtualbox.org/) VM to run the tests.

This week, I was writing tests for a [module](https://github.com/jantman/puppet-archlinux-workstation)
that configures my desktop and laptop, including installing and setting up Xorg and KDE and the
[SDDM](https://github.com/sddm) display manager. I wanted to be able to test that they not only
got installed, but actually ran without dieing - which required a graphincal environment (ideally,
I'd visually confirm this as well).

To do this in Vagrant, you'd just add a ``gui = true`` option to the
[virtualbox provider](https://docs.vagrantup.com/v2/virtualbox/configuration.html) in your Vagrantfile.

It isn't documented anywhere, but I [found](https://github.com/jantman/puppet-archlinux-workstation/commit/6ca19a24853681c468eba38735c8d2d7f54cd616)
that Beaker has support for this as well; all you need to do is add ``vb_gui: true`` in your node definition YAML.

~~~~{.diff}
--- before.yaml	2015-09-19 11:20:47.772523116 -0400
+++ after.yaml	2015-09-19 11:20:20.768867546 -0400
@@ -1,11 +1,12 @@
 HOSTS:
   arch-x64:
     roles:
       - master
     platform: archlinux-2015.09.01-amd64
     box: jantman/packer-arch-workstation
     hypervisor: vagrant
+    vb_gui: true
 
 CONFIG:
   log_level: verbose
   type: foss
~~~~

Once that's done, the VirtualBox VM will run with a graphical display enabled. This is probably only useful on a local
machine or if you're running on a remote host have you have access to and have [vrdp](https://www.virtualbox.org/manual/ch07.html)
enabled, but in some edge cases like my module, it's useful.
