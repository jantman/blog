Title: Windows advances, Cutting out the middle-man
Date: 2007-12-07 16:29
Author: admin
Category: Ideas and Rants
Tags: lcd projector sflc busybox microsoft windows tv streaming
Slug: windows-advances-cutting-out-the-middle-man

So I have a nice weekend of real-world non-technical activities ahead of
me. A welcome end to a week of insanely busy school work, and a welcome
break before the threat of exams 2 weeks away becomes real. I've been
working on a few projects - centralized logging and analysis, some way
to easily tie Nagios, log analysis, traffic analysis, etc. into a
one-look heads-up display, and a few other things. I even got the power
adapter for my LCD so that I can have a try at the [giant wall-size LCD
projector](http://www.tomsguide.com/us/supersize-your-tv-for,review-342.html).
However, reading through my usual RSS feeds today, I felt the urge to
comment on a few things.

First, for those who haven't heard, the SFLC and the BusyBox developers
have filed [another
lawsuit](http://www.softwarefreedom.org/news/2007/dec/07/busybox/)
alleging GPL violations, this time against Verizon for distributing an
Actiontec router to FiOS customers, sans source code. I'm a FiOS
customer (in fact, the very text you're looking at is coming to you
courtesy of residential fiber) but got in on the wagon before they were
giving away these "fancy" routers. It's good to see, though, that the
F/OSS world is standing up for its' values, and perhaps the mainstream
proprietary world will start to understand that just because you can
give a copy of BusyBox to your friends doesn't mean they can disregard
the license.

<span style="font-weight: bold;">Windows Advances?</span>  
I came by [this blog
post](http://blogs.ittoolbox.com/linux/locutus/archives/if-the-gui-is-so-good-then-why-is-microsoft-dropping-it-20951?e=unrec#commentsForm)
discussing the fact that, apparently, Windows 2008 is going to be able
to be installed in a CLI-only (yes, that's right, no GUI) mode.

I'm not going to preach about Microsoft turning unix-y. Rather, I think
it just reiterates something that I've said time and time
again:<span style="font-style: italic;"> I'm setting up a DNS server.
It's going to be administered in a web GUI or by scripts. Why should I
tie up RAM and processor cycles to display a GUI that, if the system
works right, will never be looked at?

<span style="font-style: italic;"></span></span>Rather than seeing this
as some victory for Linux, Unix, etc., I take it a bit more
realistically (though still, perhaps, over-optimistically):  
Maybe Microsoft is finally realizing that their one-size-fits-all
mentality doesn't work. That people want options. And, even more
mysteriously, that not everyone wants to have to buy the newest hardware
just to run an OS.

<span style="font-weight: bold;">Cutting out the Middle Man:</span>  
I found and [article at
internetnews.com](http://www.internetnews.com/stats/article.php/3655796)
entitled
"<span style="font-family:Verdana, Arial, Helvetica, sans-serif;font-size:-1;"><span>The
Young, Smart And Loaded Watch Online TV</span> ". Many parts of it
saddened me - like the thought of allowing providers to push
advertisement through my computer, or tracking my viewing habits in
great detail.

However, this is something that's occurred to me many times. Firstly, I
already use [MythTV](http://www.mythtv.org/) to watch tv. So,
realistically, I'm already watching TV on a computer. I have broadband
in both my home and apartment (and anywhere else I'd want to be). I have
a coaxial cable coming from the wall, plugged into my computer. And I
have to hook a tuner up and capture the video. Why not cut out the
middle man?

I pay Cablevision somewhere around $30/month for TV. That covers not
only the content, but also the costs for them to maintain a vast network
of cable lines stretching from where-ever to my house. I already have
broadband, why not just get TV over that?

Admittedly, I doubt any provider would give me what I want. But let's
think about it for a moment. Their only cost is a datacenter somewhere.
I simply connect to a somehow-authenticated video stream over my
existing broadband connection, and watch TV! All they need is a contract
to rebroadcast. They can even pay on a per-view basis, as they would be
able to tell who's connected to what at a given time. They just need a
data center with a LOT of bandwidth, some sattelite or fiber video
lines, and a system to capture each channel they offer. It then just
gets streamed.

Sounds wonderful to me. I'm already paying for high-bandwidth, why not
pay a third-party to stream TV to me instead of paying the cable
company? They don't need to maintain anywhere near the level of
infrastructure - no physical cabling, no satellites, and QoS would be
determined by each individuals' ISP. It would even allow me to have one
account and watch at home, at my apartment, or at work.

The catch, at least for me? Well, while this might be viable, the odds
are there would be a proprietary viewer application. That's bad.
Firstly, it's useless if you can't record it and watch it later, or
transfer it to another computer. But more importantly, the odds of such
a company embracing a standardized technology (like just streaming
everything over the web and depending on SSL and HTTP-based
authentication) that will run on my Linux boxen is pretty slim.  
</span><span style="font-style: italic;"></span>
