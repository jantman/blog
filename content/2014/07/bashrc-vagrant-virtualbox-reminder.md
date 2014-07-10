Title: bashrc Vagrant / VirtualBox reminder
Date: 2014-07-10 06:45
Author: Jason Antman
Category: Tech HowTos
Tags: vagrant, bashrc, profile, virtualbox
Slug: bashrc-vagrant-virtualbox-reminder
Summary: Add a little reminder about Vagrant/VirtualBox running machines in your profile/bashrc.

Lately I've been using VirtualBox VMs, both managed by Vagrant and otherwise, quite a lot.
I've also been doing a bunch of development work with them. And inevitably, I close a screen
window and fo on with my work and end up with a few "orphaned" virtualbox VMs running that
I've forgotten about.

Below is the snippet I've added to my ``~/.bashrc`` to keep me aware of this situation. Unfortunately
the ``vagrant global-status`` command is relatively slow, so this adds (on my machine) about
1.5 seconds of wall-clock time to my ``.bashrc`` (hence the process check first).

~~~~{.bash}
# Vagrant/VirtualBox reminder
if pgrep VBoxHeadless &>/dev/null; then
    vblist=$(VBoxManage list runningvms)
    [ -n "${vblist}" ] && echo -e "\e[1;31mRunning VirtualBox VMs:\e[0m\n${vblist}\n"
    if which vagrant &> /dev/null && vagrant help | grep -q global-status; then
        vagrantstatus=$(vagrant global-status | sed '/^\s*$/q')
        echo "$vagrantstatus" | grep -q running && { echo -e "\e[1;31mRunning Vagrant Machines:\e[0m" ; echo "$vagrantstatus" | head -2; echo "$vagrantstatus" | grep running; }
    fi
fi
~~~~
