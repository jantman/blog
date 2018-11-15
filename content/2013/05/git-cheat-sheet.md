Title: Git Cheat Sheet
Date: 2013-05-14 05:00
Author: admin
Category: Miscellaneous
Tags: git
Slug: git-cheat-sheet

I use [git](http://git-scm.com/) quite a bit these days, both with an
internal server at work and with a bunch of my projects and random code
that now live on [my github account](https://github.com/jantman/). The
transition from SVN hasn't always been easy. Here's a quick cheat sheet
of some of the things that I usually forget.

-   Show diff of the last commit:

        git diff HEAD^..HEAD

-   Roll back to version xyz of a specific file *(where xyz is a SHA1
    commit ref)*:

        git checkout xyz path/to/file

-   Undo any *unstaged* changes to your branch:

        git checkout -f

-   Undo any staged and working directory changes:

        git reset --hard

-   Update submodules after cloning a repository:

        git submodule update --init

-   Rebase on current master to pull in new changes:

        git rebase master

-   Rebase on current master, but for files that changed, take our
    version *(for some reason, a plain rebase seems to sometimes show
    conflicts on files that haven't changed in ages on master)*:

        git rebase -s recursive -Xtheirs master

-   Delete a local branch:

        git branch -d BranchName

-   Delete a remote branch from origin:

        git push origin --delete BranchName

-   Roll back your branch to the same state as the branch in origin:

        git reset --hard origin/BranchName

-   Revert a specific commit:

        git revert COMMIT_HASH

-   Track an upstream branch (i.e. in a project you forked):

        git remote add --track master upstream https://github.com/user/project.git

-   Pull in upstream changes:

        git checkout master && git fetch upstream && git merge upstream/master

-   Merge "stuff" from someone else's fork into yours:

        git remote add other-guys-repo URL_TO_REPO
        git fetch other-guys-repo
        git checkout my_new_branch
        git merge other-guys-repo/master

-   Prune local branches that have been deleted in the remote (origin):

        git remote prune origin


