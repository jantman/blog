Title: Bug / Issue Tracking Software
Date: 2007-09-07 11:44
Author: admin
Category: Software
Tags: bug tracking, bugs, bugzero, eventum, flyspray, otrs, rt, ticketing, trac
Slug: bug-issue-tracking-software

I recently posted the following to the DevShed forum in hope of an
answer:

> I've spent the last 48 hours reading up on bug
> tracking software. At the moment, I'm using the SourceForge tracker for
> my public projects and a custom (lightweight kludge) system for internal
> and customer-specific stuff.
> 
> First off, I'm looking for something that's F/OSS and no-cost. Beyond
> that, it should have a web-based interface, preferably coded in PHP as
> that's what I'm most comfortable writing code for.
> 
> I've looked into many possibilities. At the moment, they're pretty much
> narrowed down to RT, FlySpray, Codetrack, Trac, and a few other
> america's promise rorabaugh3possibilities. I've immediately disregarded
> anything without an online demo, so some may have slipped by me.
> 
> I can do some coding to add a few features as needed, but here's what
> I'm looking for:
> 
> 1) Web-based interface
> 2) Ability to handle multiple projects
> 3) Ability to handle modules/branches of a project - specifically to be
> used for projects which also have custom, user-specific modifications on
> a branch.
> 4) \*multiple\* bug submission forms - ideally, one for team
> members/technical users, one (simplified) for non-technical end users,
> and one for non-technical users which also collects browser/OS
> information, as many of my projects are web-based.
> 5) If possible, integration with CVS or SVN so that I can track commits
> related to a specific bug.
> 6) Fine-grained access control. There should be a way to submit an
> anonymous (unregistered user) bug. Anonymous submissions and registered
> user submissions should be authorized on a project-by-project (or
> branch-by-branch) basis. There should also be access control on viewing
> \*any\* information at all for certain projects/modules (so the same
> system can be used for internal-only projects).
> 
> I'm sure that I have a lot of other requirements, but these are the ones
> that stuck out in my mind. Also, though I don't have a system up and
> running yet, there's a possibility I may be moving to LDAP for all auth,
> so something where I could drop in a custom auth module would be a plus.
> 
> Any suggestions?
> 
> I know I probably won't find \*all\* of this in one place, but I'd like
> to minimize the amount of programming I have to do. After all, starting
> a new programming project to track bugs in an existing one isn't
> especially efficient.

We'll see what happens out of it.

I recently received a few emails from someone attempting to get [PHP EMS
Tools](http://www.php-ems-tools.com) up and running for his EMS agency.
I did a lot of correspondence via email, and ended up in a bit of a
predicament. First off, since CVS is down, I had to make a copy of the
latest development sources from their live location on my web server,
and revert to using RCS for the development work. Secondly, he wasn't
familiar with the SourceForge trackers and didn't have an account with
them, so I had to manually enter the bug reports. This was not good. I
need something better.

I know that a lot of ticketing systems use e-mail interfaces, but I have
no interest in that - I want to be able to require certain information
for certain people. Moreover, I have a few main issues with most of the
ticketing software I've seen:

1.  It's either designed for development team members or non-technical
    end users. I want a system that can present an end-user with a
    simple, non-jargon-filled issue submission form, yet put that right
    in with issues entered by developers, which would have a greater
    depth of technical content. Developers should be able to follow-up
    on users' tickets and add technical details as needed. Most
    importantly, since most of my projects are web-based, I want to add
    JS to the form which will include the users' browser and OS
    information in the ticket.
2.  I don't have a server farm. I don't expect to be getting hundreds of
    bugs a year, let alone week. As such, it makes no sense for me to
    run a separate system for every project. I want a system that can
    handle multiple projects.
3.  Furthermore, I want it to handle internal projects as well - server
    upgrades, hardware issue tracking, etc. As such, it should support
    fine-grained access control, both for viewing and submitting bugs.
    Some projects should allow anyone to view bugs, and allow a
    non-registered (provided the email address is valid) user to submit.
    Some projects shouldn't let anyone but me see \*anything\*.
4.  I need support for branches within projects. While PHP EMS Tools
    only has the trunk publicly available, I now have two branches, one
    customized for my organization and one for this gentleman's
    organization. I want a system that can understand that these are
    branches of the main project, and that bugs may pertain to only one
    of these branches, but that all of the bugs from the trunk will
    pertain to them.
5.  I would love a system that can somehow integrate with CVS or SVN, so
    that I can associate a specific commit with a specific bug(s).

So far, I'm considering FlySpray, RT, and Trac. I'm also looking at
Eventum, Codetrac, and BugZero. I'm interested in OTRS as I've heard
good things about it, but I can't seem to find a web-based demo. Most
likely, I'll probably give two or three of them a whirl, and then add in
the custom code to do what I need. Of course, none of this will happen
until I either get CVS back up or migrate to SVN.
