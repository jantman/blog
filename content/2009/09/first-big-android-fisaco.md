Title: First big Android ... fisaco
Date: 2009-09-29 08:44
Author: admin
Category: Miscellaneous
Tags: android, google
Slug: first-big-android-fisaco

Well, I wanted to call this a $\#!\^storm, but I don't think it's grown
to those proportions yet. But any new platform will have its hiccups,
and Google is relatively new to the OS world.

So, here's the news. Google issued a legal Cease and Desist order to a
developer Steve Kondik (known as [Cyanogen][]). The story goes something
like this... Steve is an active Android developer, doing a lot of work
on the lower-level stuff (lower level than apps), including multi-touch
and more home screens. His changes are essentially at the OS-level, and
Android doesn't have a full-fledged package management/patching
mechanism like Linux distros, so making use of them requires recompiling
stuff and re-flashing the device with a new ROM image (since the
installation apps can't handle stuff this low-level). Here's the rub: in
order to work on a device, the ROM image needs to include both
closed-source Google apps and proprietary (device manufacturer) drivers.
While these apps and drivers are available for download, the license
terms prohibit redistribution. But in order for Steve to create a
fully-functional ROM image, he has to include the closed code.

There are some writeups on this at [Linux Magazine][] and a good, timely
analysis at [Linux Insider][].

There's also a clarification by Google's Dan Morrill on the [Android
Developers][] blog.

So, what's my take on all this (not that another guy taking about this
is needed)?

Firstly, I think this is relatively minor. The community will work
around it, whether with Google's blessing or not. The bigger issue
that's coming to light is the fact that Google isn't simply altruistic,
they're a for-profit entity. They have every right to be, and they have
every right to exercise some amount of control over Android. The
community needs to realize that Android isn't a silver bullet, and isn't
even the Linux of the phone world. On the other hand, Google needs to
realize two important facts: 1) the openness of Android is what's
driving developers to it, and they need to do all they can to continue
that, and 2) most of those developers are flat-out used to running Linux
with an all-GPL system, and aren't used to the concept of not being able
to roll their own distribution.

So what's my advice?

1.  Google should further decouple their Apps from the Android platform.
    Specifically, instead of requiring users to back things up, they
    should provide a redistributable application that installs their
    other apps. *Allow a user to flash a bare-bones community ROM image,
    and then pull whatever else they want from Google.* If Google
    intends on toeing the line that Android is Free but the (Google)
    Apps aren't, then Google should provide an acceptable means for
    users of community ROM images to easily and painlessly re-install
    the closed Google apps on that image.
2.  Google should require that handset manufacturers do the same. Create
    a redistributable application that can be part of community ROM
    images, which will (via tethering or whatever) download and install
    any proprietary device-specific drivers that are needed.

Bottom line of my opinion - it's fine if Google exercises their full
control over their own closed apps. But they should provide an avenue
for non-technical end-users to easily upgrade a community (i.e. Free)
ROM image with the expected Google Apps and device manufacturer
software.

  [Cyanogen]: http://twitter.com/cyanogen
  [Linux Magazine]: http://www.linux-mag.com/cache/7544/1.html
  [Linux Insider]: http://www.linuxinsider.com/rsstory/68237.html?wlc=1254230361
  [Android Developers]: http://android-developers.blogspot.com/2009/09/note-on-google-apps-for-android.html
