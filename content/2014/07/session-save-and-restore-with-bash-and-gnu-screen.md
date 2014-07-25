Title: Session Save and Restore with Bash and GNU Screen
Date: 2014-07-25 10:09
Author: Jason Antman
Category: Tech HowTos
Tags: bash, screen, restore, bashrc
Slug: session-save-and-restore-with-bash-and-gnu-screen
Summary: How to automatically save and restore GNU screen sessions including windows, pwd and history

I've been using [GNU Screen](http://www.gnu.org/software/screen/) for a very long time; I pretty much do _all_ of my
daily work in it. I have long-lived screen sessions pretty much everywhere; at any given time, I've got a session running
on my desktop (that probably has 19 windows open and active) and a few on various remote hosts. I also have a really
bad habit of using screen windows to hold work in progress, things that I need to revisit, and what I want to do
next. This isn't as big of a deal on boxes in a datacenter that rarely go down, but my home desktop ends up getting
rebooted every few weeks (and not always at planned times).

__Warning__ - what I'm about to describe is, really, a fragile and somewhat ugly hack. I'm pretty sure that if I took
the time to learn and switch to zsh (or another, more modern shell) and tmux, I could probably do this easier. But my
shell environment is something I'm pretty stuck in. So, if this is useful to anyone else, cool. But caveat emptor.

screen 4.2.0 introduced some extensions to the `-Q` remote querying capabilities, including the ability to retrieve a
list of current windows and their titles via `screen -Q windows`. A few months ago, I wrapped a python script around
this that reads the currently open windows along with their title and window number, and writes out `~/.screenrc.save`
that's `~/.screenrc` with `screen -t` lines to recreate my currently open windows with their titles. After a system
crash or reboot, I could `screen -c ~/.screenrc.save` and get all of my windows and their titles back. So, that's
a slightly better reminder of what I was working on assuming I keep my titles relevant. But each window just dumped
me into `~/` like usual, so I'd just have the window title to remind me what I was working on. 

I ran this script for a few months; you can see the original version [here](https://github.com/jantman/misc-scripts/blob/ab6a14774d5dd6250aac98f804c33d3dc26a32eb/savescreen.py).
However, this still really isn't what I'd call "session restore". I had window titles as "hints" to what I was doing,
but everything else was left to my memory.

Enter some awful `bashrc` hackery. Please note that my bashrc is a bit complicated, mainly due to git completion
and getting a proper prompt for python virtualenvs, but here's the magic portion:

~~~~{.bash}
# git prompt - make it work everywhere
if [[ -e /usr/share/git/completion/git-prompt.sh ]]
then
    source /usr/share/git/completion/git-prompt.sh
elif [[ -e /usr/share/git-core/contrib/completion/git-prompt.sh ]]
then
    source /usr/share/git-core/contrib/completion/git-prompt.sh
elif [[ -e ~/bin/git-prompt.sh ]]
then
    source ~/bin/git-prompt.sh
fi

#set the PROMPT
cur_tty=$(temp=$(tty) ; echo ${temp:5});
# git prompt configutation
GIT_PS1_SHOWDIRTYSTATE=1
GIT_PS1_SHOWUNTRACKEDFILES=1
GIT_PS1_SHOWUPSTREAM="auto"
GIT_PS1_SHOWCOLORHINTS=1

# for screen session-saving hack, set per-window history file if in screen
[[ -n "$STY" && -n "$WINDOW" ]] && export HISTFILE=$(readlink -f ~/.screenhist/$WINDOW)
shopt -s histappend

# make sure our screen session-saving hack directories exist
[[ -d ~/.screenhist ]] || mkdir ~/.screenhist
[[ -d ~/.screendirs ]] || mkdir ~/.screendirs

__wrap_git_ps1 ()
{
    # commands here now get executed every time bash constructs a prompt
    # for screen pwd saving
    if [[ -n "$STY" && -n "$WINDOW" ]]
    then
        SCREENLINKDIR=$(readlink -f ~/.screendirs)
        rm -f $SCREENLINKDIR/$WINDOW
        ln -sf $(pwd)/ $SCREENLINKDIR/$WINDOW
    fi
    # virtualenv stuff for prompt
    venv=''
    [[ $VIRTUAL_ENV != "" ]] && venv="\[\033[31m\](${VIRTUAL_ENV##*/})\e[0m"
    __git_ps1 "$venv\u@\h:$cur_tty:\w" "\\\$ "
    history -a
}
PROMPT_COMMAND='__wrap_git_ps1'
export PS2="> "
~~~~

So... the hack. First we source the git prompt scripts that come with git (trying the
locations they should be at on all of the machines I commonly use, and if it can't find
any of them, falling back to a copy in my homedir) and set some configuration variables
for them (as well as capturing the current tty). We then (conditionally on being inside
a screen window) set our history file to a per-screen-window path, and have history append.
At this point we also make sure some directories we'll use exist.

Now the real fun. `PROMPT_COMMAND` specifies a function for bash to execute to build the
prompt string; this is called every time bash needs to display the prompt (so, effectively,
every time a command completes in the shell). We set it to `__wrap_git_ps1`, a function we
just defined. The magic happens in this function. Screen sets some environment variables
inside each window, including `STY` (the name of the screen session you're in) and
`WINDOW`, the current window number. If both of these are set, we symlink our current
`pwd` to `~/.screendirs/$WINDOW` (note some hackery, explicitly removing the link if it
already exists, to get this to work correctly). We then throw in some python virtualenv-specific
prompt settings, and pass on the strings we've constructed to `__git_ps1` which adds the
git-specific information, and then sets `PS1` correctly. Finally, we explicitly append to
current history, to make sure the history on disk is always accurate and up-to-date.

This works in combination with the [latest version](https://github.com/jantman/misc-scripts/blob/master/savescreen.py)
of savescreen.py, which has some minor changes. The line to create each window, formerly:

~~~~{.python}
fh.write("screen -t \"{name}\" {num}\n".format(name=windows[n], num=n))
~~~~

becomes:

~~~~{.python}
fh.write("screen -t \"{name}\" {num} sh -c \"cd $(readlink -fn {dirpath}/{num}); bash\"\n".format(name=windows[n], num=n, dirpath=dirpath))
~~~~

When each window is created at startup, we `cd` into the previous `pwd` (the path
that the `~/.screendirs/$WINDOW` symlink, created by bashrc, points to) and then
call our shell. When this is combined with the `HISTFILE` change, the effect is that
`screen -c ~/.screenrc.save` brings us back into a screen session that has not only
all of our previous windows and their titles, but also a shell in each window's previous
working directory, and that window's history.

__Limitations__:

1. I should've also used `$STY` in each of the paths, so this would be multi-session-safe.
   I didn't, so this has undefined behavior if more than one screen session is running as
   your user.
2. A lot of this is lost, obviously, if you `sudo su` or `ssh`, or in any other way end up
   as a different user.
3. I'm thinking about rolling in some method of automatic `virtualenv` activation (since it,
   unfortunately, doesn't have anything like `.rvmrc`). Maybe in the next version.
