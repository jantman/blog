Title: The Hubris of Software Development
Date: 2017-10-09 20:05
Modified: 2017-10-09 20:05
Author: Jason Antman
Category: Ideas and Rants
Tags: software, engineering, development, safety, culture
Slug: the-hubris-of-software-development
Summary: Some thoughts on modern software development, and how much our industry still needs to mature.
Status: draft

I'll apologize in advance that this is a bit of a rambling rant...

I just finished reading ["The Coming Software Apocalypse" by James Somers](https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/),
and the article really resonated with me on a deep level. I've never worked on life-critical software, but I
have worked at a number of companies with very large workloads, places that pushed popular and widely-deployed
software past its tested limits... and seen it fail in unusual and unexpected ways. And after a decade in the
industry, I've seen first-hand far too many examples of shoddy work, from laziness or lack of planning
("rare edge case" bugs being hot within minutes of real production user traffic) to outright unethical
practices (like dead-man switches in code). But even more disturbing to me are the times I've seen teams
of brilliant and experienced software professionals befuddled by a failure, trying desperately to figure
out why something isn't working right.

And I think in technology, we're simply too full of ourselves. It's hubris. We've designed and built things
that no one mortal can fully - or often even mostly - understand. We do it in the name of requirements, and
we do it in the name of cost and efficiency and timelines. The smart people among us who work for good companies
build resilient software, but so often we simply accept some amount of completely mysterious failure
as normal in technology. We build systems that we trust with our pictures and thoughts, but would never
trust with our bank accounts or pay checks. What about with our lives? Somewhere in the world, right now,
a developer who's spent their entire career writing applications where a 1% error rate is acceptable, is
developing something that will be connected to a car's internal network. And speaking for myself at least,
a 1% error rate is not acceptable for something that can talk to my car's steering, accelerator and brakes.

I should probably be deeply embarrassed by this, but the conclusions of James' article - model-based design
and formal specifications - aren't comfortable for me. I was never mathematically inclined, and it just feels
_uncomfortable_ to me... though that's probably a statement more about my education than anything else. But
the article did really get me thinking about the state of software development. About how our systems have
gotten more complex by orders of magnitude but our methods haven't really evolved as much as we'd like to
think. We put our faith in new languages and patterns, in peer review, in automated testing. But how much
can those things really help us? We're technologists, and we love technology and technological solutions.
But in the best case, adding tools to a problem only augments the individual developer's imagination
and understanding with that of whoever wrote the tools - albeit far abstracted from the problem at hand.

So many times I've seen software developers, testers or operations folks take on a new piece of work -
pull a ticket, grab a card, whatever each team calls it - and start writing code almost immediately.
I've done it. I still do it. Sometimes I start writing the code in my head on my drive in to work,
thinking about the amazing way I'm going to solve some problem. And sure, that might work fine for
simple or familiar tasks. But how often do we do the same thing for tasks that aren't simple,
that aren't familiar to us, that are - at least in some respect - completely new and novel, but we
still want to start coding.

If the result of our work was physical instead of virtual, would anyone be able to work that way?
If your customer asked you to build them a bicycle or a lawnmower, would you start by whipping up
a quick front wheel, then maybe a handlebar, ask the person sitting next to you to make an axle,
and hope that it all fit together the way you wanted? Most likely not. I know that at this point,
many people (and myself at times) will make the argument that because our work has no physical raw
materials, rework is cheap, so experimentation should be encouraged. But what I'm talking about isn't
experimentation, as we've all known since our elementary school science teachers taught us about
the scientific method. Experimentation, at the very least, involves a clear hypothesis and plan
for how to prove or disprove it. This is more like... luck. Or maybe an educated guess.

The pragmatist in me wants so badly to defend these methods - methods that I've used many
times, still do, and probably will well into the future - based on their results. The system
worked. The application runs. Within the context of the small set of test cases that my
mind could identify, it operates correctly. Maybe it even handles real production traffic
for seconds, minutes, days or months. But what does that all mean?

While the modern principles of DevOps, CI/CD, decent testing and resilience have done great
things for the Web and modern end-user applications, exponential backoff doesn't work very
well when the problem we're trying to solve is keeping some people alive inside a speeding
metal box. And looking at the past decade of history in software systems that we'd think
should be safe - cars, banks, medical devices - it's pretty clear that we need to be doing
a lot better than we are throughout all of the industry.

Diagramming, modeling and discussion. Don't be isolated. The power of visualization and discussion on reasoning about design.

Engineering, professional ethics, real professional standards... especially when software becomes more critical, and legislation and regulation lags far behind.

Title change to Engineer.

...

But this issue isn't just about ethics, responsibility, and better quality work in critical systems. It goes beyond that; it's about the economic cost of shoddy work, about the disservice that poor quality work does to its users and the image of our industry, and the risks posed by our world placing increasing trust and power in the hands of an industry where mediocre quality is the norm. As software developers and other technology professionals, so much of what we produce is hidden from the customer (whoever that customer is, whether they're paying us or not). It's often impossible or impractical to fully "inspect" our work. And I've seen - many times, from both sides - the often shocking shortcuts that can be taken when technology workers know they won't be held accountable.

I grew up in a small suburban town; it wasn't perfect, but it was a small close-knit community of people who really
cared about their friends and neighbors. We had a municipal police force of twelve officers, all of whom lived in town
or in an adjacent town, and most of whom had spouses and/or children in town. When they hired new officers they always
gave strong preference to young residents with no previous police training, preferring to do the training locally.
They felt that the training programs of the state police academy weren't right for a small town; the state turned out
officers with training that focused on violent crime, impersonal interactions with citizens, and quantity over quality.
Those aren't the qualities looked for when serving the residents of a small community - in a capacity that as often as
not had nothing to do with crime - where courtesy and relationships were valued. And, more importantly, they found
that it was much more difficult to un-train an officer with previous experience than to train someone with the right
attitude from the beginning.

Right now, by and large, the software development industry as a whole is focused primarily on producing poor or
mediocre work quickly. Sure, there are many notable exceptions, but the average software project in the world right
now is judged mainly on whether it was finished on time and within budget and meets the functional requirements,
not whether it's well-architected, maintainable, or reliable. That is a tremendous liability for our profession.
As software enables becomes more critical parts of our lives - whether in autonomous vehicles, the power grid,
or just the POS system that we can't buy groceries without - there will be more demand for workers to develop,
test and operate these applications. And while the people writing code for your car's anti-lock brakes might be
used to the rigorous quality of life-critical systems, the people writing the UI on your dashboard probably
aren't. The longer we as an industry continue accepting marginal quality, focusing mostly or completely on functional
requirements, and allowing individuals in isolation to engineer large parts of systems, the more collective
risk we'll all have to deal with. Retraining a developer who's spent most of their career focused on
fast and cheap - whether explicitly or implicitly - to focus on the highest quality possible isn't easy.

"Runs multiple hours without crashing" might be a non-functional requirement at best for a game on my phone,
but it's pretty damn important for my car.

http://blog.cleancoder.com/uncle-bob/2017/10/04/CodeIsNotTheAnswer.html

http://blog.cleancoder.com/uncle-bob/2017/08/28/JustFollowingOders.html
