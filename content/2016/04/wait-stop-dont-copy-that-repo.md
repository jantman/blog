Title: Wait! Stop! Don't copy that repo!
Date: 2016-04-03 20:58
Author: Jason Antman
Category: Ideas and Rants
Tags: clone, fork, repository, code, management, versiong
Slug: wait-stop-dont-copy-that-repo
Summary: An argument for why not to do internal development on open source projects.
Status: draft

Once upon a time, I worked at a company with some of the most talented and passionate people I've ever known. We
were a shop that used almost all open-source software, and ran a CMS that powered a whole bunch of relatively
large sites, as well as working some related and unrelated smaller projects. The language that we used isn't
important; it was an interpreted language with a well-supported packaging system. Most packages lived in Git,
often open source on GitHub, and we also maintained an internal package repository compatible with the language's
tooling.

In the last few months of my tenure there, on their Automation team, I was tasked with migrating from a legacy
internal git server to a new GitLab instance. I'd thought that the hardest part would be coordinating time for
a cutover from the old server to the new one, and ensuring that all changes were synced over. That was incredibly
far from the case.

As I started to examine the repositories on the old server, I was dumbfounded. I'd expected that our internal projects
would be a bit of a mess. What I wasn't prepared for, though, was the state of our external dependencies. In some cases,
we had as many as six internal repositories that all were named like widely-available open source packages for our
language, often hosted on GitHub. There would be a "foo", "foo-old", "foo-new", "foo-<companyname>" and another "foo"
or two under different directories (we managed them somewhat like namespaces/organizations in GitHub and GitLab).
Some of them were actual clones of the original repository with local modifications, but some of them were archives
or exports, with none of the upstream history. Some of them had many local modifications yet retained the upstream
version; some had the version numbers properly identified as a fork, according to the language spec; others simply
continued incrementing the version number with local changes.

I spent almost three weeks trying to reconcile various repositories with both the upstream source and our running
code. In some instances, we'd submitted our changes back to the upstream project, had them accepted, and just never
switched back to the public version. In most cases, we'd never submitted our changes, and were now horribly diverged
from upstream; we'd had more than a few bugs that resulted in developers spending days or weeks trying to reconcile
years of work in order to pull in upstream bug fixes. In a number of cases, the built packages in our internal
package server didn't match up with _any_ commit or tag in _any_ of the source repositories.

A few weeks ago, at my new job, we'd made some fixes that we needed to an open source project. In a meeting, there
was a quick discussion about how to handle them, and the suggestions ranged from opening a pull request to forking
the project (on GitHub) to simply copying it to our internal git server. Perhaps a bit too forcefully, I interjected,
"Wait! __Stop!__ Do __not__ copy that to the private server!"

I've seen many, many examples of this being done: public, open source projects being 

## Why?

- cost of maintenance/overhead
- unless you're going to seriously commit to maintenance in the long term, upstream _will_ fix bugs that you haven't
- the future / the long view
- giving back
- testing - many eyes
- upgrading your software

## A Call To Action

- fork & PR, work off your fork if need be
- versioning or naming to show this (links?)
- vendor it in?

## So, The Suits Won't Let You

I know it's not uncommon in certain industries for companies to have issues releasing work under open source
licenses. If that's the case, I do have a set of recommendations. Please note that I'm not a lawyer; some of
what I suggest may be ill-advised for many people, so please take this with a grain of salt and be sure to
do what's legal and ethical.

1. See if your company's hostility to open source is actually real, or just a conspiracy theory. Just because
everyone says it can't happen, doesn't mean that's fact. Ask your manager, and get it escalated as high up the
chain as it can. Even if it doesn't work for the specific project in question, it could help in the future.
2. Do it on your own time. I know different companies have different policies on this, but I've worked places
where it was perfectly clear that anything I did outside my work hours was my own. If it's a quick fix, why not
whip it up at home and try to get the pull request or patch accepted?
3. Many companies that aren't willing to release their own code/projects under an open source license might
feel differently about something that's just a patch to existing software. Ask about this specifically; if
it's just a few dozen or hundred lines that are already written and fix a problem in an OSS package, they
might be more willing to allow it.
4. If it's legally and ethically advisable, perhaps you can just email your patch to a maintainer of the
project, and explain that you can't fork or submit through the official methods, but you want to give back.
5. If all of the above fail or aren't practical, make sure you've submitted the best bug report you can. The
more detail you give - and the more help you can be in suggesting a possible solution and doing as much of
the leg work as you can - the better. I'm always happy to receive a bug report that explains the exact failure
case, provides pointers to the source code in question, and suggests a solution.
6. Ok, so all of those things failed or weren't feasible, and you need to maintain a private internal version
of the project. For your own sanity and that of the people who come after you, here are some tips:
    1. Resist the impulse to simply copy/archive/export the upstream source. Do an actual git clone of it,
    and get all of that history pulled in to your internal repository. It will make it clear when you
    began internal development, and it will make it possible to merge in future upstream changes without
    spending large amounts of time trying to figure out when the repositories diverged. You'll be able to
    rebase and merge the way you would with any git repository.
    2. Don't work on ``master``. Set a new default branch to be something like ``internal``. Keep all of
    the upstream branches, and use your own. The goal is to keep as much transparency as possible about
    when the project was brought internal, and what work/code is internal vs upstream. Do everything you
    can to make this clear, especially to people who join the company months or years later.
    3. Tag the state of ``master`` when you bring the repository internal, with a descriptive tag like
    ``point-of-divergence``. When you pull master and then rebase upstream changes into your internal
    branch (which you _will_ want or need to do at some point), update the tag. The goal is to be able
    to easily tell at any time (using native git tooling) what work is internal vs upstream, and how
    far behind upstream you are.
    4. Periodically monitor the state of upstream. The goal of all this is to reduce the overhead of
    maintaining software - especially third-party projects that are dependencies - as much as possible.
    Clarity of what work is internal vs external is good. Even better is being able to switch back to
    the official upstream when your bug is fixed. Monitor releases periodically, and test any possible
    fixes for your bug or feature. If one works, switch back to upstream and delete your internal
    repository.
    5. Document all of this clearly. Update the README in your local default branch with an explanation
    of when and why the internal repo was created, what conditions need to be met to switch back to the
    upstream, and how branching, tagging and rebasing on upstream work.
    6. Finally, and I can't stress this enough, resist the impulse to add whatever you want to the internal
    version of the project just because it exists. Have all code changes reviewed not only for quality,
    but for whether or not they belong there. If you're adding organization-specific logic to a third-party
    library, you're probably doing it wrong, and you're preventing yourself from ever benefiting from
    upstream bug fixes or being able to return to the public version. See my notes above on this topic.

I hope some of this prevents others from having to go through as much pain reconciling internal/forked
versions of projects as I did.
