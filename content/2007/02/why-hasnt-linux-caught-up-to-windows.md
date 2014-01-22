Title: Why hasn't Linux caught up to Windows?
Date: 2007-02-19 17:20
Author: admin
Category: Ideas and Rants
Tags: compatibility, development, distribution, linux, novice, windows
Slug: why-hasnt-linux-caught-up-to-windows

Those of us who are involved in the Linux community are often frustrated
by the lack of widespread acceptance of Linux. Granted, I haven't used
all of the newest "desktop" distributions ('distros'), but I know that
my choice - openSuSE - is far from being ready to compete with Windows
for the novice user market. From the first few screens of the
installation, it's clear that this isn't something for the uninitiated.
However, to get off on a short tangent, openSuSE has also severely
hampered access to the command-line-only, text-mode installation, which
I need in order to install on many of my servers.

Granted, it will take a lot of work to get Linux to retain its' strong
points, and still be user-friendly for the non-technical user. However,
there are three main points that I see as being the biggest problems for
new users. All of which, coincidentally, are ones which some people
would bill as strong points of Linux. And they all have to do directly
with some of the founding principles of Linux - interoperability and
choice.

\A) Packaging.  
Searching for a package for a linux system goes something like this:
figure out what package format your distro uses, figure out the distro
version and architecture, and then start checking the online
repositories. If it's something simple, you may be able to use a you
distro-specific maintenance program to automatically upgrade it. If not,
you can sift through the myriad online repositories for packages that
fit your package manager (RPM, Apt, etc.) and your distro/architecture.
If you have no luck there, find the package's homepage, and hope someone
has contributed packages for your distro and architecture - usually a
hit-or-miss situation. Last but not least, when all else has failed, you
choose either to compile from source yourself, or give up. Compiling
from source not only requires some knowledge of your system, Linux, and
the compilation sequence used by the software - hopefully the generic
GNU-style ./configure, make, make install and not some more esoteric
scheme. Furthermore, compilation requires a whole slew of tools to be
installed on your system - make, gcc, autoconf, and may others,
depending on package. While it's not practical for people with limited
resources, homogenous environments, or novice users, I operate in a
largely heterogeneous environment - i586/compatible systems running SuSE
9.3-10.2 - and therefore maintain a dedicated system for compilation, if
merited.

All of this complexity just enforces the novice's idea that there is not
much software available for Linux, as many novices are limited (due to
technical knowledge) to the packages that come with their OS.

While there are a few schemes to standardize all of this, the real
solution is quite complex, and would be based on a single package system
to be adopted by all distros (beginning with the main ones). Such a
system should have the following features:  
1) Ability to work easily with all distros  
2) I main configuration file which can define which directories to use -
i.e. /etc, /bin, etc.  
3) Support for both simple, novice-oriented interfaces and expert-level
configuration  
4) Multiple interfaces, including command-line, text/ncurses, GTK, and
other graphical subsystems  
5) A generalized package format that is non-distro-specific  
6) Integration with an online master-list of repositories  
7) Ability to search, download, and install packages from these
repositories  
8) Automatic update ability  
9) Ability to mine the repositories for updates, and display a list on
screen or emailed to a user account  
10) Very good tools for easy compilation from source.

Some of these ideas would be incorporated in the tool itself, and some
as add-on modules.

The features that I, as administrator of a largely heterogeneous network
of about 10 machines, would most like to see are:  
1) Truly automatic updates via list - select which packages can be
automatically updated, and run a cron job nightly to check for any
updates for those packages and automatically get and install them.  
2) LAN-based updating - A single server on the LAN maintains a list
(perhaps gathered via an automatic tool) of ALL packages installed on
ALL LAN machines. Each night the configured clients will update this
list over the network, and then the master server will download all
available updates for all packages. Once this is complete, it will send
a message to all LAN machines, which will then update their software
from the central repository on the LAN. This would, in effect,
automatically keep all LAN machines 1) on the same version of each
package and 2) totally up-to-date.  
Kernel updates would be done manually, but should have an option for the
administrator to push the update to all machines.

\B) Distro-specific tools, filesystem layout, etc.  
This is not only a barrier for novice users, but experienced users as
well. If you do a search online for Linux training, you will surely come
by a nubmer of certifications - NCLE, RHCE, etc. The many distinct
certifications - offered by each Linux vendor and independent training
companies - underscore the inherent differences in Linux distributions.
While I'm perfectly comfortable working with SuSE Linux (by Novell), if
I was to sit down in front of a Gentoo system, I would probably be
totally lost.

While the LSB project (http://www.linux-foundation.org/en/LSB) has aimed
to provide compatibility between distros, there are three main points
which must still be addressed:  
1) The organization of filesystems on different distros, specifically
the directory tree and default locations for certain components, still
differs. In the interest of usability, the Linux directory tree should
be standardized, so that locations of programs, files, etc. will be
identical across distributions.  
2) An effort needs to be made to make administration as similar as
possible across all distros. This means that program names,
functionality, location, etc. should be standardized as much as
possible.  
3) It seems that each distro has its' own administration tool - YaST for
SuSE, and others for other distros. An effort needs to be made to
develop a tool encompassing all of the features in one, distro-neutral
form. Webmin (www.webmin.com) has done this wonderfully in a web-based
interface, but attention should be focused on a text-mode console
version as well.

\C) GUI  
Perhaps the biggest hurdle for novices using Linux, and the biggest
development challenge, is general ease of use. While the above two
points may fall into this category, I am specifically referring to the
general, day-to-day use of the operating system.

While I will not begin to suggest solutions, the main problems that I
see are as follows:  
1) The stability and security of Linux must be kept intact, unlike
distros such as Lindows.  
2) There must remain a way for advanced users to perform advanced
tasks.  
3) As much of the inner workings should be hidden from the end-user as
possible, unless specifically requested.  
4) I good system would have a field added to a users' GECOS data
specifying their level of "novice-ness" - i.e. allowing a dumbed-down
interface for users while retaining a full interface with Expert
features for those who want it.  
5) "Mysterious" things such as file permissions should be hidden from
novice-level users when not absolutely needed.  
6) There must be a strong integration with "anti-mistake" tools and DWIM
technology. The system itself should manage file permissions in a way
that grants only the minimum needed access.  
7) There should be good, strong mistake detection, specifically in terms
of catching a user's inadvertent changing of file permissions, deleting
required files, etc.  
8) Tools should be built so that the novice user is never required to
login as root or run a root shell.  
9) Perhaps, and I'm sure this is controversial, the root account should
be given either CLI-only access, or should not have X running by
default, so as to discourage novice users from running day-to-day tasks
as root.

I'm sure I've missed a lot, and have also probably mentioned a number of
things that are already in place. However, the bottom line is that Linux
has to be able to achieve the easy of use and interoperability (between
distros) that Windows currently has, while retaining the extensibility,
advanced features, security, and stability that make Linux what it is.
