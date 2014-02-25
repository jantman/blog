Title: What I Look For When Interviwing SysAdmin Candidates
Date: 2012-07-05 11:07
Author: admin
Category: SysAdmin
Slug: what-i-look-for-when-interviwing-sysadmin-candidates

I recently came by a question on ServerFault, [Listing side projects in
a jr. sysadmin
resume](http://serverfault.com/questions/210218/listing-side-projects-in-a-jr-sysadmin-resume/405054#405054)
asking whether people (hiring managers) think it's appropriate to put
"side projects" (running your own web and mail servers, freelance web
work, etc.) on your resume. Since I've been interviewing candidates for
a few SysAdmin positions lately, I thought I'd take the time to write
down a few of my ideas on this. Two disclaimers first, though. (1) I tend
to be pretty geeky, progressive, and very open source/DevOps focused at
heart. Not everyone I work with will agree with what I say here. As a
candidate, remember that you'll probably interview with all types, and
what I say here won't be the best advice with Enterprise types. I'm very
open source centric, and have always held SA jobs where the majority of
the software I run is open source and not vendor supported. (2) If you
happen to actually interview with me, don't make the mistake of reading
this and tailoring your resume/responses to fit if that's not accurate.
I'm not a manager, I'm a line SA.

**First, my response to the ServerFault question:**

> Not a hiring manager, but an SA doing technical interviews and hiring
> recommendations, and also have only been with my current employer for
> 7 months (so I've been on both sides of the table recently). My
> current employer is a pretty big company and pays well, so we're quite
> selective.
>
> SA candidates with 5-10 years experience and a laundry list of
> certifications, software and hardware names, protocols, etc. are a
> dime a dozen. I'm looking for people who really love what they do. I
> have an instant bias against resumes that don't have either a personal
> website/URL, or some personal projects/experience other than 9-5 job
> on them. There are lots of people who meet the technical
> qualifications. I want someone truly passionate, and that means
> learning and experimenting outside of work.
>
> Personally, on my resume, I have a few personal projects listed
> (mainly programming projects and volunteer IT work I did for
> non-profits), and I also have a link to my personal resume site that
> has links to my SVN repo, and a bunch of other projects.

**Some things I look for:**

-   Not in all cases, but I like to see a website or blog listed on a
    resume. It's a big plus. I have
    [resume.jasonantman.com](http://resume.jasonantman.com) with copies
    of my resume in various formats, as well as a bunch of links I'd
    like employers to see.
-   If you're a working SA, I should be able to find you on Google.
    Either by name or email address, I expect to google the contact
    information I find on your resume and find at least some mailing
    list/forum posts, bug reports, or software projects.
-   I can't stress this enough, **do not overstate your experience**.
    I've been an SA for 5 years, a hobbyist for much longer, and I've
    never used the word "expert". I list software, protocols, languages
    on my resume as beginner/basic, intermediate, and "strongest". If
    you list something as "advanced" or "expert", be prepared to answer
    expert-level questions. If you can't explain a 3-way handshake,
    don't list TCP/IP on your resume. If you list "strong knowledge of
    Linux internals", you should be able to at least explain `open()`
    and `close()`. If you list advanced RADIUS experience, I *will* ask
    you to explain CSID, WPA key exchange, and what attributes are valid
    in an Access-Reject. In short, don't say you're a genius in
    something unless you are; you never know when your interviewer may
    have spent the last 6 months immersed in it.
-   All SAs should have some programming skills. If you're a recent
    graduate (let's say any time in the last 5-8 years) I'd expect at
    the very least a vague memory of C++, VB or Java. If you're a
    working SA, I expect to see either strong Bash skills, or at least a
    functional knowledge of Perl. Python, PHP or Ruby; preferably both.
    If you're a "senior" Linux SA, you should know enough C to be able
    to make sense of `strace` output.
-   As stated above, non-full-time-job projects are a big plus. When I
    took my first SA job, the majority of my experience had been doing
    volunteer work for a non-profit ambulance corps (which I was also a
    volunteer EMT on). If I said that I did 40 hours a week for them, it
    would be an understatement. I wrote a few 10,000+ line PHP
    applications for them, and designed the infrastructure to run them
    24x7x365. Small shop? Sure. But I learned a LOT, especially about
    how to make things resilient enough that I didn't get paged often.

I'm sure I'll update this over time as I distill more of my ideas.
