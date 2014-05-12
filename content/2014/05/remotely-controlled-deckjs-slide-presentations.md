Title: Remotely-controlled deck.js slide presentations
Date: 2014-05-12 09:34
Author: Jason Antman
Category: Tech HowTos
Tags: slide, presentation, deck.js, deckjs, javascript
Slug: remotely-controlled-deckjs-slide-presentations
Summary: A wonderful GitHub project by chrisjaure to remotely control deck.js slide presentations.

I've been struggling to find a good, cross-platform remote meeting solution. We're using [iMeet](http://www.imeet.com)
at work at the moment, but there's no way to present or screen share from a Linux machine. For most of our ops and
automation team daily and weekly meetings, we use [TeamSpeak](http://www.teamspeak.com/) - sure it's not open source,
but it's simple, supports all OSes that matter to us (Mac, Linux, Windows, Android and iOS), can be self-hosted,
and has the holy grail, functional push-to-talk. But it's audio only.

On Friday I was running two short elaboration meetings, and had quick little slide decks done up in [deck.js](http://imakewebthings.com/deck.js/)
to keep us on track. I couldn't help but think, gee, it sure would be nice if instead of switching to Mac or a VM and sharing my screen,
we could just use the audio communication mediums that we already do, and I could simply control the slides in a browser.

Well this morning I stumbled on [Chris Jaure](http://cleverchris.com/)'s [deckjs-remote](https://github.com/chrisjaure/deckjs-remote)
project that does exactly that. It's a nodejs npm module that runs a websocket server, and allows people to join a session and follow
along as the presenter changes slides.

I did have a few hiccups getting it working - mainly some issues with CORS. The README.md has a large block of markup to be added to
the slide deck html to support "older browsers that don't support CORS." I'm running Firefox 28.0 (Firefox has supported CORS since
3.0, quite a few years back) and still needed to add this to get everything working. I also needed to manually add a script tag
for socket.io coming from the nodejs server in order to get everything working.

There's a bit of a delay for the socket connection to come up after initially loading the page, but once that's done, the presenter
("master" session) should get the password prompt, and any guests should get a prompt asking if they want to join the current
session. Perhaps the best part is that the nodejs server interally stores each deck by URL, so it seems to work perfectly fine
when running one instance for N presenters (i.e. a single instance running persistently on a shared server).

