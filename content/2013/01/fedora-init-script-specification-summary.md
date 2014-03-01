Title: Fedora Init Script Specification Summary
Date: 2013-01-03 11:30
Author: admin
Category: Ops
Tags: centos, fedora, init, redhat, startup
Slug: fedora-init-script-specification-summary

I've been deploying some new software lately (specifically
[selenesse](https://github.com/marisaseal/selenesse), which combines
[Selenium](http://seleniumhq.org/) and [fitnesse](http://fitnesse.org/),
[xvfb](http://en.wikipedia.org/wiki/Xvfb)). None of these seem to come
with init scripts to run as daemons, and the quality of the few
Fedora/RedHat/CentOS init scripts I was able to find was quite poor. The
Fedora project has a [Specification for SysV-style Init Scripts in their
Packaging wiki](http://fedoraproject.org/wiki/Packaging:SysVInitScript),
which specifies what a Fedora/RedHat/CentOS init script should look
like, in excruciating detail. What follows is an overview of the more
important points, which I'm using to develop or modify the scripts I'm
currently working on.

-   Scripts must be put in `/etc/rc.d/init.d`, not in the `/etc/init.d`
    symlink. They should have 0755 permissions.
-   Scripts must have a Fedora-style [chkconfig
    header](http://fedoraproject.org/wiki/Packaging:SysVInitScript#Chkconfig_Header)
    ("chkconfig:", "description:" lines), and may have an [LSB-style
    header](http://fedoraproject.org/wiki/Packaging:SysVInitScript#LSB_Header)
    (BEGIN INIT INFO/END INIT INFO). See [Initscript
    template](http://fedoraproject.org/wiki/Packaging:SysVInitScript#Initscript_template).
-   Scripts **must** make use of a lockfile in `/var/lock/subsys/`, and
    the name of the lockfile must be the same as the name of the init
    script. (There is a technical reason for this relating to how sysv
    init terminates daemons at shutdown). The lockfile should be touched
    when the daemon successfully starts, and removed when it
    successfully stops.
-   Init scripts should not depend on any environment variables set
    outside the script. They should operate gracefully with an
    empty/uninitialized environment (or only LANG and TERM set and a CWD
    of `/`, as enforced by `service(8)`, or with a full environment if
    they are called directly by a user.
-   [Required
    actions](http://fedoraproject.org/wiki/Packaging:SysVInitScript#Required_Actions)
    - all of the following actions are required, and have specific
    definitions:
    -   **start**: starts the service
    -   **stop**: stops the service
    -   **restart**: stop and restart the service if the service is
        already running, otherwise just start the service
    -   **condrestart (and try-restart)**: restart the service if the
        service is already running, if not, do nothing
    -   **reload**: reload the configuration of the service without
        actually stopping and restarting the service (if the service
        does not support this, do nothing)
    -   **force-reload**: reload the configuration of the service and
        restart it so that it takes effect
    -   **status**: print the current status of the service
    -   **usage**: by default, if the initscript is run without any
        action, it should list a "usage message" that has all actions
        (intended for use)

-   There are specified exit codes for [status
    actions](http://fedoraproject.org/wiki/Packaging:SysVInitScript#Exit_Codes_for_the_Status_Action)
    and [non-status
    actions](http://fedoraproject.org/wiki/Packaging:SysVInitScript#Exit_Codes_for_non-Status_Actions).
-   They must "behave sensibly". I've found this to be one of the
    biggest problems with homegrown init scripts. If `servicename start`
    is called while the service is already running, it should simply
    exit 0. Likewise if the service is already stopped. Init scripts
    **must not kill unrelated processes**. I don't know how many times
    I've seen scripts that kill every java or python process on a
    machine.

I intend to use this as a quick checklist when developing or evaluating
init scripts for RedHat/Fedora based systems. In my experience, the
biggest problems with most init scripts revolve around poor handling of
PID files and lockfiles, mainly:

-   Killing processes other than the one that the script started (i.e.
    killing all java or python processes), usually because the PID isn't
    tracked at start
-   Starting a second instance of the subsystem because lockfiles aren't
    used, or the status function is broken.
-   improper exit codes
-   either explicitly relying on environment variables (and therefore
    breaking when called through `service(8)`), or conversely, not
    cleaning/resetting environment variables that are used by dependent
    code or processes.

