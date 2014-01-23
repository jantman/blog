Title: Instagram - Scaling a Startup
Date: 2012-04-24 19:31
Author: admin
Category: Miscellaneous
Tags: dogslow, facebook, high scalability, instagram, node2dm, pgfouine, puppet, scaling, statsd
Slug: instagram-scaling-a-startup

If you keep up with news on the 'net, you may have heard about photo
sharing startup [Instagram][], which was [purchased by Facebook for $1
Billion][] just 9 days after they released their Android app. Well, not
only are they based mostly on open source software (well, yeah, pretty
much a given for web startups these days), but they've dealt with
scaling issues like a million new users in 12 hours, and they're
[talking about it][]. There's the [slide deck to a talk that co-founder
Mike Krieger gave][] on TechCrunch and [Scribd][], along with a [High
Scalability article about it][], and an [earlier High Scalability
article that gives an overview of the company and some details of what
and how they're running][]. Instagram Engineering also has a [tumblr][]
account, with a bunch of cool posts like [Keeping Instagram up with over
a million new users in twelve hours][talking about it] (which
specifically mentions [statsd][], [dogslow][], [PGFouine][], [node2dm][]
and some database stuff) and [What Powers Instagram: Hundreds of
Instances, Dozens of Technologies][] which talks about their OS and
hosting (Ubuntu 11.04 on EC2), load balancing (nginx, DNS and Amazon
Elastic Load Balancer), Django, Redis, Solr, Munin, etc.

This is a really cool company, doing some *really* cool stuff, at a
*really* large scale, and growing fast.

On another note, I'm continuing my attempt to read all of the excellent
Puppet articles on [Brice Figureau's (aka masterzen) blog][]. It's
taking a while, as it's really good, in-depth information that I want to
rememeber, but I'd highly recommend it for anyone working with Puppet.

  [Instagram]: http://instagr.am
  [purchased by Facebook for $1 Billion]: http://finance.fortune.cnn.com/2012/04/09/breaking-facebook-buying-instagram-for-1-billion/?section=magazines_fortune
  [talking about it]: http://instagram-engineering.tumblr.com/post/20541814340/keeping-instagram-up-with-over-a-million-new-users-in
  [slide deck to a talk that co-founder Mike Krieger gave]: http://techcrunch.com/2012/04/12/how-to-scale-a-1-billion-startup-a-guide-from-instagram-co-founder-mike-krieger/
  [Scribd]: http://www.scribd.com/doc/89025069/Mike-Krieger-Instagram-at-the-Airbnb-tech-talk-on-Scaling-Instagram
  [High Scalability article about it]: http://highscalability.com/blog/2012/4/16/instagram-architecture-update-whats-new-with-instagram.html
  [earlier High Scalability article that gives an overview of the
  company and some details of what and how they're running]: http://highscalability.com/blog/2012/4/9/the-instagram-architecture-facebook-bought-for-a-cool-billio.html
  [tumblr]: http://instagram-engineering.tumblr.com/
  [statsd]: http://github.com/etsy/statsd/
  [dogslow]: http://blog.bitbucket.org/2011/05/17/tracking-slow-requests-with-dogslow/
  [PGFouine]: http://pgfouine.projects.postgresql.org/
  [node2dm]: http://github.com/Instagram/node2dm
  [What Powers Instagram: Hundreds of Instances, Dozens of
  Technologies]: http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances-dozens-of
  [Brice Figureau's (aka masterzen) blog]: http://www.masterzen.fr/blog/archives/
