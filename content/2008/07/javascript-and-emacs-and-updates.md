Title: JavaScript and Emacs, and updates
Date: 2008-07-01 11:09
Author: admin
Category: Projects
Tags: ajax, call report, dhtml, javascript, pcr, tuxostat, tuxtruck
Slug: javascript-and-emacs-and-updates

Well, thankfully, summer classes are almost over (tomorrow is the last
class). I have a big paper to write for one of them, due at the worst
time possible - July 5th. The day after what is, probably, one of the
busiest days of the year for the [ambulance corps][].

**In follow-ups and news:**

1.  [tuxostat][] has been running for nearly a month in my apartment,
    and appears stable, albeit missing many planned features, and with a
    sub-optimal interface (and no SNMP yet).
2.  3.  [TuxTruck][] is still on the back burner.
4.  I've been playing around with the idea of writing a new electronic
    patient care report system for the ambulance corps, to replace our
    current three-year-old system (written in VB .NET and running on
    Windows). It would probably be coded in Python, with a
    wxWindows/[wxPython][] GUI. I'll start on a small demo version, but
    would like it to be fully modular, and eventually form a codebase
    for [OpenEPCR][].

</p>

Anyway, I've been doing a lot of work for my Building Data-Driven
Websites class (well, alternate assignments, but still a lot of work).
The latest project was an Ajax/DHTML calendar (view-only [here][], and
in [CVS][], of course). Needless to say, this involved a lot of
JavaScript work. To make it worse, I used a fair amount of sample code
to get an idea of how to do things, and way too many of the snippets out
there on the 'net are in formats that are quite unfriendly for pasting
into an Emacs console window.

So, I happened to come by [Steve Yegge's blog][], with a posting on [his
JavaScript mode for Emacs][]. Not only does it seem cool, but it was
also the only one I could find that does syntax highlighting and sane
indentation (important for copied code snippets). So, I grabbed it from
[Google Code][] and - viola!

  [ambulance corps]: http://www.midlandparkambulance.com
  [tuxostat]: http://tuxostat.jasonantman.com
  [TuxTruck]: http://www.tuxtruck.org
  [wxPython]: http://www.wxpython.org/
  [OpenEPCR]: http://www.openepcr.org
  [here]: http://www.jasonantman.com/rutgerswork/BDDW/calendar/
  [CVS]: http://cvs.jasonantman.com/rutgerswork/BDDW/calendar/
  [Steve Yegge's blog]: http://steve-yegge.blogspot.com/
  [his JavaScript mode for Emacs]: http://steve-yegge.blogspot.com/2008/03/js2-mode-new-javascript-mode-for-emacs.html
  [Google Code]: http://code.google.com/p/js2-mode/
