Title: Visualization of when I'm working on personal vs work projects
Date: 2015-06-05 21:20
Author: Jason Antman
Category: Miscellaneous
Tags: git, commits, python, graphs, visualization
Slug: visualization-of-when-im-working-on-personal-vs-work-projects
Summary: A fun python script to visualize the time of day and day of week of your commits to personal vs work repositories.

I was thinking the other day - as I was pushing out some final code reviews for work at 11PM before taking a day off -
about how much work I do outside of "work hours". And the answer is, I don't really know, especially when it comes to
projects that I really enjoy and find interesting. So, I decided to have some fun with [GitPython](https://github.com/gitpython-developers/GitPython)
and find out.

The result of this was [whendoiwork.py](https://github.com/jantman/misc-scripts/blob/master/whendoiwork.py). It's a pretty simple script,
and also makes some pretty big assumptions, but I found the results interesting. Given some local directories which contain git clones
of my work repositories, and some which contain clones of my personal repos, it iterates over all\* of the commits in them by me
(going by the git author name) in the last N days (default 365); it counts commits to personal repositories as +1 and to work
repositories as -1, and adds them to buckets per hour of day, per day of week. It then uses [matplotlib](http://matplotlib.org/)
to build a heatmap, with the maximum commits per hour for work repos in blue and the maximum per hour for personal in red.

I can't vouch that it's 100% accurate, but the results were interesting to me; while it seems like I tend to do a fair amount
of work in the evenings, compared to work on personal projects, all of my work for my employer is well contained in my normal
7-3 work day.

Here's an example of the output of this script, for my own work, run with:

    ./whendoiwork.py -v -a /home/jantman/GIT -b /home/jantman/work/git -b /home/jantman/work/git/ops -d 365 -t 'US/Eastern' --repoAlabel personal --repoBlabel work

Note that this iterates over every commit in all of the git repos it finds, possibly multiple times. On my own
system (9G of git repos with a few hundred thousand commits), this took about 2 minutes.

![heatmap of days of week and hours of day when I commit to work vs personal repos](https://raw.githubusercontent.com/jantman/misc-scripts/master/whendoiwork.png)

If you find any bugs/issues with it, please pass them along by [opening an issue](https://github.com/jantman/misc-scripts/issues).
