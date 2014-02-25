Title: openEPCR
Date: 2007-12-27 01:46
Author: admin
Category: Miscellaneous
Tags: emergency medical, EMS, free, healthcare, medical, open source, openepcr, patient care report, pcr, prehospital
Slug: openepcr

I've been toying around for a while with the idea of creating a software
package for handling Electronic Patient Care Reports for EMS (Emergency
Medical Services) agencies. There are a few popular packages around, but
most of them are web-based. In the event of a disaster - or even bad
storm - when Internet connectivity is minimal to non-existent, frankly,
you're up the creek without a paddle. There are also, to my knowledge,
no Free/Open-Source (or free of cost) packages available. This isn't
good, especially with many states and regions moving to standardized
PCRs with electronic submission. This is even worse for the thousands
(or more) of purely volunteer EMS organizations out there, who have
little to no budget.

So, I've started a project - [openEPCR](www.openepcr.org).

I know that, for me, this is a \*big\* undertaking. I figured that Java
is the best option, since it's available on almost all platforms,
robust, and frankly is very well accepted. The idea is that such a
system should be able to cost \*nothing\* - so the target audience is
people using Linux (or BSD or Solaris) or an existing Windows
installation, along with a simple server - MySQL, PostgreSQL, or another
database, along with some web server running PHP. I'll admit that my
Java isn't what it used to be - but more to the point, frankly, if I'm
the only person working on this, it'll take years to finish. So,
hopefully, when I get a more concrete plan, I'll be able to enlist some
other developers - especially someone more knowledgeable than me about
how best to deal with data caching (in the event - or certainty, as in
wireless or vehicular applications - of a loss of connectivity), mobile
devices, and HIPPA compliance.

The overall idea is to design a platform that is a base for an EPCR -
something that can handle data collection, printing a hard copy,
analysis, administration, security, etc. - and all the while be
organization-independent. In essence, a framework. Firstly, after having
this problem with [PHP EMS Tools](http://www.php-ems-tools.com), it
should all be designed with i18n/L10n in mind from the beginning,
providing good and easy support for translations. More importantly, all
settings should be configurable. To top off the problem, anything that's
obviously organization-specific - like the data set, layout of input
forms on the screen, reports on the data, printed copy (both blank and
filled-in), user access rights/RBAC, authentication methods, etc. -
should all be designed as pluggable modules. The end result would be a
system where a single organization or group of organizations can develop
- or pay to have developed - a "module" that includes all of this. The
license would have additional terms stating that any changes to the
code, modules, or updates to modules \*must\* be given back to the
openEPCR community. The general idea is something like this scenario:
the state of New Jersey decides to adopt a standardized PCR and data
set. Many volunteer ambulance squads don't have the funds for a
commercial solution. A bunch of them pool their resources or funds and
develop a "module" for openEPCR that provides everything required to
implement a printed and electronic version of the NJ state PCR. If a
single organization wishes to deviate, they can simply "extend" that
module as they see fit, building off of the main code. OpenEPCR itself
remains neutral, but provides a repository of modules to use or modify.

As I see it, there are three main difficulties:

1.  Designing something that's abstracted to such a great degree.
2.  Dealing with data when we don't know the environment - we might be
    stand-alone, always connected to a single master database server,
    intermittently connected, or even connecting to a different server
    every time.
3.  We want centralized administration - optimally, all custom data,
    settings, and organization-specific information (as well as updates
    to this) will be pushed out from a central server to all clients.
    But we need to assure security in an environment that is untrusted
    and may even be hostile - perhaps even hostile users - and balance
    the fact that some instances of the software may be actively
    collecting and recording data before they have been notified of a
    certain change or update.

So, if you think this sounds interesting, or have any suggestions - from
either the technical or EMS standpoint - please check out the [project
homepage](http://www.openepcr.org) or drop me an
[E-Mail](mailto:jason@jasonantman.com).

Excerpted from the homepage is a bit of information on my goals:

**Project Mission:**
OpenEPCR aims to provide the Emergency Medical Services sector with a
Free (as in Freedom, a.k.a. Open-Source) Electronic Patient Care Report
(EPCR) software solution. Licensed under the [GNU
GPL](http://www.gnu.org/copyleft/gpl.html "http://www.gnu.org/copyleft/gpl.html"),
it will be easily extendable by users' organizations. Such a solution
does not currently exist. Furthermore, many states and regions are
moving to electronic data aggregation for EMS. OpenEPCR aims to provide
an easy way for organizations to adopt a standardized data set and
submit their data - and only the data that they choose - to a trusted
third party. The software will attempt to do all of this while paying
heed to applicable standards on privacy and security, as well as being
fully platform-independent.

**Project Goals:**

1.  Provide *all* code licensed under the GNU GPL, and make code as
    easy as possible to modify and extend.
2.  Be fully platform-independent and database-independent, running in a
    platform-independent language.
3.  Have NO reliance whatsoever on outside services i.e. be able to run
    in a disaster situation with a full communications breakdown.
4.  Be designed with internationalization (i18n) and localization in
    mind, specifically with easy support for translations.
5.  Have all data set, user information, rights/access management,
    authentication, and authorization abstracted, allowing
    organization-specified rules as well as various authentication means
    (central server, local file, passwords, hardware tokens, OTP, etc.)
6.  Attempt to conform to HIPPA and other applicable standards governing
    security and privacy.
7.  Allow all organizational data such as PCR forms, data sets,
    printable versions, etc. to operate as pluggable modules; changing
    the entire PCR structure should be as easy as adding a few new files
    and running a script.
8.  Be designed with both the small, volunteer, virtually budget-less
    squad and the large paid organization in mind.
9.  Run on a variety of devices including desktops, laptops, and mobile
    devices of all flavors.
10. Operate in environments including standalone, central server, ad-hoc
    network, and a network of distributed master servers.
11. Have the utmost regard to integrity of data - data loss or
    corruption is NOT an option.
12. Support virtually unlimited customization for an end-user
    organization.
13. Be designed with ease of extension in mind - it should be easy for
    end-user organizations to design custom add-ons that integrate
    fully, while conforming to the Access Control model.
14. Eventually, include support for administrative functions such as
    equipment/vehicle checks, scheduling, roster functionality, etc.
15. Eventually, consider creation of an integrated incident management
    system for patient, resource, and personnel tracking.
16. Be designed with as much space for custom software hooks as
    possible.
17. Attempt to pull together developers from various disciplines and
    gather suggestions from a vast sampling of the EMS field.

