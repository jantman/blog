Title: Web-based collaboration/documentation software
Date: 2010-04-27 16:43
Author: admin
Category: Miscellaneous
Tags: collaboration, documentation, project management, Projects, wiki
Slug: web-based-collaborationdocumentation-software

This question was posted both to the
[SAGE-members](http://www.sage.org/lists/) list
([thread](http://mailman.sage.org/pipermail/sage-members/2010/msg00788.html))
and to
[ServerFault](http://serverfault.com/questions/136416/free-web-based-software-for-team-collaboration-documentation):

> Looking for some advice here, as my search has turned up to be pretty
> fruitless.
>
> My group (9 people - SAs, programmers, and two network guys) is
> looking for some sort of web tool to... ahem... "facilitate increased
> collaboration" (we didn't use a buzzword generator, I swear). At the
> moment, we have an unified ticketing system that's braindead, but is
> here to stay for political/logistical reasons. We've got 2 wikis
> ("old" and "new"), neither of which fulfill our needs, and are
> therefore not used very often. We're looking for a free (as in both
> cost and open source) web-based tool.
>
> Management side:  
>  Wants to be able to track project status, who's doing what, whether
> deadlines are being met, etc. Doesn't want full-fledged "project
> management" app, just something where we can update "yeah this was
> done" or "waiting for Bob to configure the widgets".
> [TeamBox](http://www.teambox.com) was suggested, but it seems almost
> too gimmicky (Twitter/Facebook ripoff?), and doesn't seem to meet any
> of the other requirements that I see coming up:
>
> Non-management side:  
>  - flexible, powerful wiki for all documentation (i.e. includes good
> tables, easy markup, syntax highlighting, etc.)  
>  - good full text search of everything (i.e. type in a hostname and
> get every instance anyone ever uttered that name)  
>  - task lists or ToDo lists, hopefully about to be grouped into a
> number of "projects"  
>  - file uploads  
>  - RSS or Atom feeds, email alerts of updates
>
> We're open to doing some customizations (adding some features,
> notification/feeds, searching, SVN integration, etc.) but need
> something F/OSS that will run under Apache.
>
> My conundrum is that most of the choices I've found so far fall into
> one of these categories:  
>  - project management/task tracking with poor
> wiki/documentation/knowledge base support  
>  - wiki with no task tracking support  
>  - ticketing system with everything else bolted on (we already have
> one that we're stuck with)  
>  - code-centric application (we do little "development", mostly SA
> work)
>
> Any suggestions?
>
> Or, lacking that, any comments on which software would be easiest to
> add the lacking features to (hopefully ending up with something that
> actually looks good and works well)?

I'm still awaiting responses from both SAGE and ServerFault, but I have
a strong feeling that most of the suggestions will fall into one of the
major categories I already identified, mainly:

1.  Project management/task tracking with poor wiki/documentation
    support (a la TeamBox)
2.  Wiki with no task tracking support
3.  Ticketing system with everything else added in (useless since we
    already have to use a different ticketing system).
4.  Something code-centric, i.e. built around a software development
    workflow, which isn't us.

So, I have a very strong feeling that whatever solution we end up going
with, we'll need to spend quite a bit of time bolting on whatever else
we need. Adding a full-featured wiki to another package isn't going to
be very easy... especially since TeamBox is written in RoR, and we're
mostly PHP guys.
