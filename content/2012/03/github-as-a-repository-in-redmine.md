Title: Github as a repository in Redmine
Date: 2012-03-27 21:36
Author: admin
Category: Miscellaneous
Tags: git, github, redmine
Slug: github-as-a-repository-in-redmine

As a follow-up to my [CVS to SVN to Git](/2012/03/cvs-to-svn-to-git/)
post, I have the [PHP EMS Tools](http://www.php-ems-tools.com)
repository migrated from my SVN to
[github](https://github.com/jantman/php-ems-tools). Since I'm moving the
website and all development to a [Redmine](http://www.redmine.org/)
instance, the next step is setting up Github to work as a revision
control repository in redmine. Well, it's dead simple. I just followed
the instructions for the [Redmine plugin: Github
hook](http://mentalized.net/journal/2009/08/03/redmine_plugin_github_hook/)
, with the exception that I followed the [redmine instructions for
setting up the repository
clone](http://www.redmine.org/projects/redmine/wiki/HowTo_keep_in_sync_your_git_repository_for_redmine)
instead of Step \#2 in the plugin instructions. All worked well, though
I'll admit I only tried it talking to redmine over plain HTTP, not
HTTPS.
