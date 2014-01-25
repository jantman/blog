Title: Workflow for contributing to GitHub projects
Date: 2012-08-11 09:35
Author: admin
Category: Tech HowTos
Tags: foreman, git, github, workflow
Slug: workflow-for-contributing-to-github-projects

Lately I've been contributing to some open source projects hosted on
[github](http://github.com). I'm pretty new to git, and the process is a
bit confusing for beginners. So, here's a sample workflow, based on the
[The Foreman](http://theforeman.org)'s [foreman github
repository](https://github.com/theforeman/foreman). Note that I'm
developing against the "develop" branch of that repository, not the
master, so that throws in a little difference that isn't documented in
most introductions. To throw in another wrench, I maintan a branch with
the code that I'm currently actually using (i.e. the application code
that I have checked out on the production server), called "jantman".
This is more or less composed of the upstream "develop" branch, with all
of my finished (but not yet merged in the upstream) topic branches. I'm
pretty sure all this is correct, but honestly, I'm still new enough at
git that I can't make any promises. Unfortunatelty, I haven't had the
time to *really* learn git, and I also can't find a simple enough
tutorial that covers all this...

1.  Fork the original repository through the GitHub interface.
2.  On your machine, clone your fork:

~~~~{.bash}
git clone git@github.com:username/reponame.git && cd reponame
~~~~

3.  Make sure you've setup

~~~~{.bash}
git config --global branch.autosetupmerge true
~~~~

4.  Add your upstream repo:

~~~~{.bash}
git remote add upstream git://github.com/upstream_user/upstream_repo.git
~~~~

5.  Fetch it and initialize any submodules:

~~~~{.bash}
git fetch upstream && git submodule update --init
~~~~

6.  Check the current branch (`git branch`, let's assume it's called
    "develop") and rebase to its upstream:

~~~~{.bash}
git rebase upstream/develop develop
~~~~

7.  Create my "jantman" branch, which will be the upstream "develop",
    plus my finished work merged into it:

~~~~{.bash}
git checkout -b jantman origin/develop
~~~~

8.  Create a topic branch to do some work:

~~~~{.bash}
git checkout -b NewBranchName jantman
~~~~

9.  Periodically, push the topic branch to github:

~~~~{.bash}
git push origin NewBranchName
~~~~

10. If you commit to this branch from another computer (or someone else
    commits to it), periodically update your local tracking branch:

~~~~{.bash}
git pull origin NewBranchName
~~~~

11. Periodically, you want to pull in the upstream changes:
    1.  switch to the develop branch:

~~~~{.bash}
git checkout develop
~~~~

    2.  grab the latest version of the upstream git repo:

~~~~{.bash}
git fetch upstream
~~~~

    3.  rebase develop to mirror the upstream develop branch:

~~~~{.bash}
git rebase upstream/develop develop
~~~~

    4.  switch to our personal branch:

~~~~{.bash}
git checkout jantman
~~~~

    5.  rebase our personal branch onto develop (pull all the new
        commits from develop into our personal branch):

~~~~{.bash}
git rebase develop jantman
~~~~

    6.  If we want those new upstream changes to continue down to our
        topic branches:

~~~~{.bash}
git rebase develop topicBranchName
~~~~

12. When we're done with a topic branch, we want to merge it into our
    "personal" branch:

~~~~{.bash}
git checkout jantman; git merge --squash node-table-facts
~~~~

    <p>
    and then commit:

~~~~{.bash}
git commit
~~~~

    <p>
    The `--squash` will squash all the history of that branch down to
    one commit. This is generally easier for integration into upstream,
    and assuming the topic branch was created for a single feature or
    bug, should be logical.

13. If we're sure we don't need it anymore, delete the topic branch from
    our local machine:

~~~~{.bash}
git branch -d topicBranchName
~~~~

    <p>
    and from github:

~~~~{.bash}
git push origin --delete topicBranchName
~~~~

14. Finally, make sure we push our "personal" branch back to origin:

~~~~{.bash}
git push origin jantman
~~~~

15. Assuming all went well, you'll see the new commit on github, and
    have a nice pull request button.

References:

1.  [Contribute —
    Doctrine-Project](http://www.doctrine-project.org/contribute.html)
2.  [Github - Quicksilver Wiki](http://qsapp.com/wiki/Github)
3.  [Contributor Workflow with Github · carmaa/inception
    Wiki](https://github.com/carmaa/inception/wiki/Contributor-Workflow-with-Github)
4.  [Help.GitHub - Fork A Repo](http://help.github.com/fork-a-repo/)

