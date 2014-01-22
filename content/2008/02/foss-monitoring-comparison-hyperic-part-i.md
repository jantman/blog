Title: F/OSS Monitoring Comparison - Hyperic Part I
Date: 2008-02-08 16:54
Author: admin
Category: Projects
Tags: hyperic, monitoring, open source
Slug: foss-monitoring-comparison-hyperic-part-i

So, I've made some headway on the comparison. I have Hyperic installed
and partly configured, albeit without email alerts yet. I've found some
serious features that I need missing, but I'm going to give it a full
run before I move on to another.

The full text, updated a few times a day, is available on [my wiki][].
Here's a bit of an excerpt:  
<a name="Part_I_-_Installation"></a>  

### <span class="mw-headline">Part I - Installation</span>

1.  setup Xen virtual machine running OpenSuSE 10.3 base packages. (3
    hours, some server problems, some Xen problems, and some time
    learning Xen administration from the CLI)
2.  Download `hyperic-hq-installer-3.2.0-607-x86-linux.tgz` from
    [Hyperic][] and extract.
3.  Browse to
    [http://support.hyperic.com/confluence/display/DOC/Full+Installation+Guide][]
4.  `cd` into `hyperic-hq-installer` and run `./setup.sh -full`
    1.  The installation can't be run as root (though I assumed it would
        need root privileges).
    2.  I selected to install all 3 components - Server, Shell, and
        Agent.
    3.  Well, whoops! Sorta stupid to not allow installation as root,
        when the default location to install to is `/home/hyperic`. How
        do they expect an arbitrary user to install there? Even worse,
        it appears that the default OpenSuSE 10.3 installation doesn't
        come with `sudo` (!!!!) so I can't try that.
    4.  As root, create `/home/hyperic` and chown to my user.
    5.  Repear the above steps (well, hopefully not all of them).
    6.  Default ports for everything - web GUI on 7080, HTTPS web GUI on
        7443, jnp service on 2099, mbean server on 9093,
    7.  Change domain names in default URLs to logical ones for my test
        environment (no real DNS, just IPcop hosts, so
        devel-hyperic1.localdomian). I hope that I can change these
        later, or even better that absolute paths aren't used too much,
        as this will screw with my idea of using SSH port forwarding for
        remote access.
    8.  Leave the default SMTP server alone and change it later - I
        odn't even have mail running here at the apartment.
    9.  Use the built-in PostgreSQL database with default port of 9432.
    10. Go with the defaults for everything after this.
    11. Everything runs nicely, and then it tells you to login to
        another terminal as root and run a script. I'm not sure I like
        this method, but I guess it works. Login and do it.
    12. How will it start the builtin database? As my user???? Yup.
        postgres is running as my user. Wonderful. Nothing in the
        [install
        document][http://support.hyperic.com/confluence/display/DOC/Full+Installation+Guide]
        mentioned user creation. Was this just assumed? Because in the
        naive world I live in, most installer scripts (think Nagios)
        create a user for you, or tell you to.
    13. Setup script complete. A few instructions follow...

5.  Run `/home/hyperic/server-3.2.0/bin/hq-server.sh start`... as my
    user. *Note to self:* setup a user for Postgres and Hyperic. Believe
    it or not, but it booted - but followed with the message, "Login to
    HQ at: [http://127.0.0.1:7080/][]"
6.  Browsed to [http://devel-hyperic1:7080][] and was greeted by a
    startup page, saying that the server was 18% finished booting. My, I
    yearn for little C binaries and a PHP frontend.
7.  Page turns blank and stops there. I refresh, and get a login page. I
    enter my username and password, and get a little message box where
    the "invalid password" box usually is - says "Server is still
    booting". This is over a minute later. I'm happy to see
    Apache/Coyote1.1, but would like to be able to get into Hyperic in
    less time than it takes the machine to boot to a graphical login
    screen (ok, granted, I'm running XFCE). In SuSE's YaST Xen Monitor,
    I see that the VM is at 45% of its' 464MB RAM, and 90% CPU - with
    8.5% consumed by dom0.
8.  CPU usage for the VM drops to 1% and I login again. BAM! Hyperic HQ.
    Aside from the fact that it shows NO resources... oh... start the
    Agent.
9.  Start the Agent on the VM running Hyperic. It asks me for the server
    IP address. What, no DNS? I enter the IP as it is... for now. I keep
    everything at defaults, including using the hqadmin username and
    password. Successfully started.
10. BAM! In Dashboard, I see the auto-discovered host with the right
    hostname, as well as Tomcat, Agent, JBoss, and PostgreSQL. Amazing!
    Click "Add to Inventory".
11. Check out the "Resources" -\> "Browse" screen. It knows this machine
    is OpenSuSE 10.3, and I see my four services (listed above). Of
    course, no metrics yet, but I see the correct IP, gateway, DNS,
    vendor (SuSE), kernel version, RAM, architecture, and CPU speed.
12. Looking through the "Inventory" screen, I see everything - NICs and
    MACs, running servers and one service (a CPU resource). What more
    could a man want in...let's see.. just over an hour!
13. I really \*love\* the "Views" screen which, even out-of-the-box,
    allows "Live Exec" information from cpuinfo, df, ifconfig, netstat,
    top, who, and more.
14. Well, it's 03:35, and I have work and class tomorrow. I think it's
    time to give Part I a rest. But first...
15. Go to the "Platform" page for my one machine and... YES! Graphs are
    starting to appear!
16. Following the suggestion [here][], I enable log and config tracking
    on the platform for `/var/log/warn` and `/etc/hosts`, respecitvely.
17. Before I call it a night (now 03:42), I stop back at the [downloads
    page][Hyperic] and grab the Linux x86 Agent for the dom0 machine,
    hoping to get some physical information as well. While I'm at it, I
    grab the Linux AMD64 Agent to try on my laptop. I create "hyperic"
    users on each system. On the base Xen server, I give it a shot and
    get "Unable to register agent: Error communicating with agent:
    Unauthorized". Same thing on the laptop.
18. Did a little reading [here][1]. As to keeping all of the defaults,
    it turns out that both clients had firewalls blocking TCP port 2144.
    I opened it up on both, and also set the IP address (that the server
    uses to contact the client) to the correct ones. Viola! Now I have 3
    clients connected, and gatheirng data for the next \~16 hours until
    I have time to check it out agian.

More to come in Part II tomorrow - actually doing something with
Hyperic. For  
now (04:08), time to sleep.

<a name="Part_II_-_Configuration"></a>  

### <span class="mw-headline">Part II - Configuration</span>

Unfortunately, I haven't had much time to play with Hyperic in the two
days  
since installation. The most I've really done is setup Agents on my
laptop,  
desktop, and the host machine (both dom0 and domU for Hyperic), so that
they  
start to collect data.

While I found a lot of upsetting stuff in the features list (see below),
I  
decided to go ahead and add some other devices. On the network at the  
apartment, I have two manageable switches (a Linksys and a 3Com) - which
pretty  
much make up the sum of non-host equipment. I also have an IPcop box,
though I  
assume the standard Linux Agent will handle that. The one item missing
that I  
have at home is my set of APC SmartUPS UPSs with SNMP cards, but I guess
I'll  
just have to skip them for this review.

First, I went in and added a platform (Resources-\>Browse, Tools
Menu-\>Add  
Platform) for the 3Com switch (a SuperStack II Switch 3300). It showed  
successful creation - but nothing else. I went in and entered the SNMP  
community string, IP, and version (1). In about a minute or so, I
started to  
see metrics - Availability, IP Forwards, IP In Receives, an IP In
Received per  
Second. While it's quite basic, that's good for a starting point. While
the  
[[http://support.hyperic.com/confluence/display/DOCSHQ30/Network+Device+platform][]  
Network Device Platform] documentation lists lots of metrics that can
be  
enabled, I'd also like telnet availability and - my big one since I use
a  
"cute" (crappy) IPcop installation for local DNS, a dig on DNS to make
sure  
the entry is there. In the Monitor screen, I was able to enable a bunch
of  
additional metrics (by clicking on the "Show All Metrics" link), though  
there's also no way (that I can find) to monitor the status of
individual  
ports.

Next, I browsed through the "Administration" pages, setup a few users,
and  
started setting \*way\* more default metrics for various platforms,
services,  
and servers. While I don't have mail running yet, that will come this  
weekend. While I added a lot of things as "Default On", I still need to
go  
back and add more things in the templates as Indicators.

I also added some escalations, though they're quite simple - you can
notify HQ  
users or "other users" by email or SMS, write to SysLog, or suppress
alerts  
for 0 minutes to 24 hours. Hopefully I'll also find a plugin for
Asterisk  
integration. One striking omission is user groups. Also, the concept of  
"Roles" (maybe their idea of groups?) is only available in the
Enterprise  
version.

At this point, I also notice one other majoe issue, though perhaps I'll
find a  
solution in my experimentation - there doesn't be a way to setup
default  
alerts for metrics. If they have all of this platform, server, and
service  
information defined as default templates, why not just have a way to
assign  
default users (and groups) to these objects, and have default alerts  
generated?

In terms of Apache 2.2 monitoring, out-of-the-box, nothing worked. No
metrics  
at all. Firstly, Hyperic requires the mod\_status module. Persoanlly,
I'd  
rather handle all of that through a backend, like Nagios. Secondly, it
got the  
pidfile and apache2ctl paths wrong. Furthermore, it has no "smart"
checking for resources - while my Apache 2.2 resource config was clearly
wrong (wrong PID file path, no mod\_status), Hyperic didn't detect this
and was showing the resource as "Down".

After that, I setup a bunch of alerts for things that I thought would be
off-kilter a lot (like WARN log entries on my laptop, high memory usage
on some stressed machines, etc.) as well as log and config file
monitoring and alerts for them. While I didn't have mail working yet, I
figured I might as well get that stuff running.

On the Xen dom0 host that runs the Hyperic vm (box called xenmaster1), I
wasn't able to add config file tracking for any of the /etc/xen/ files.
At this point I notice some serious shortcomings - not only is it not
possible to define a template of alerts for a given
platform/server/service, it's also impossible to define a template for
alerts. I also noticed that it's not possible to define groups of
contacts. This wasn't much of a problem for my test installation - the
alerts are only going to my roommate and I - but it would surely be an
issue in any larger setting.

At this point in configuration, I come to a make-or-break point. With
some of these shortcomings, I really need a way to call a script with
alert information when an alert is generated - whether it's to dial out
through Asterisk or just automatically create a ticket for the problem.

Adding alerts is a cumbersome process. You have to browse to a page for
a specific metric - which means going to the page for a specific
platform, server, or service - and then opening the page for that
metric. The actual alert creation takes up two pages - one for the
metric, threshold, and time-based criteria, and a second for who to
alert. This means that to add alerts for a machine, you need to view the
platform page as well as the services and servers pages, and each metric
therein.

I'll be posting some more in the days to come. From a [post at the
Hyperic Forums][], I was able to find out that a Xen plugin is in the
works, but for the Open Source version, the only way to trigger a script
is to send an email and have it handled by a filter such as Procmail.

  [my wiki]: http://www.jasonantman.com/wiki/index.php/Network_Monitoring_Comparison
  [Hyperic]: http://www.hyperic.com/downloads/dl-hq-oss.html
    "http://www.hyperic.com/downloads/dl-hq-oss.html"
  [http://support.hyperic.com/confluence/display/DOC/Full+Installation+Guide]:
    http://support.hyperic.com/confluence/display/DOC/Full+Installation+Guide
    "http://support.hyperic.com/confluence/display/DOC/Full+Installation+Guide"
  [http://127.0.0.1:7080/]: http://127.0.0.1:7080/
    "http://127.0.0.1:7080/"
  [http://devel-hyperic1:7080]: http://devel-hyperic1:7080/
    "http://devel-hyperic1:7080"
  [here]: http://support.hyperic.com/confluence/display/DOC/HQ+Quick+Start#HQQuickStart-enableTracking
    "http://support.hyperic.com/confluence/display/DOC/HQ+Quick+Start#HQQuickStart-enableTracking"
  [1]: http://support.hyperic.com/confluence/display/DOC/Installation+Non-Windows#InstallationNon-Windows-install
    "http://support.hyperic.com/confluence/display/DOC/Installation+Non-Windows#InstallationNon-Windows-install"
  [http://support.hyperic.com/confluence/display/DOCSHQ30/Network+Device+platform]:
    http://support.hyperic.com/confluence/display/DOCSHQ30/Network+Device+platform
    "http://support.hyperic.com/confluence/display/DOCSHQ30/Network+Device+platform"
  [post at the Hyperic Forums]: http://forums.hyperic.com/jiveforums/thread.jspa?messageID=14561&#14561
