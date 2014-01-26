Title: Practical PHP and MySQL
Date: 2008-06-26 14:29
Author: admin
Category: Miscellaneous
Tags: books, linux, PHP, programming, rutgers
Slug: practical-php-and-mysql

I'm taking a summer course in Building Data Driven Websites - not that I
thought I'd learn much in such a course at
[SCILS](http://scils.rutgers.edu), but I'd like to graduate on time, and
need the credits, and Bill Crosbie is just the type of rare teacher that
can keep even me awake and interested. Our book is [Practical PHP and
MySQL: Building Eight Dynamic Web
Applications](http://www.informit.com/store/product.aspx?isbn=0132239973)
([Amazon](http://www.amazon.com/Practical-PHP-MySQL-Building-Applications/dp/0132239973)
by [Jono Bacon](http://www.jonobacon.org/). Now, I know it's not a
*real* book like, say, [ESA3 by
Frisch](http://oreilly.com/catalog/9780596003432/), which has a healthy
[web presense](http://www.aeleen.com/home.htm). But this thing is all
code and doesn't even have a web site, let alone easy code downloads!

The book does come with a heavily customized Ubuntu LiveCD. However,
when I popped it in my [OpenSuSE workstation](http://www.opensuse.org),
I couldn't really make much out of the CD - there was certainly no
easy-to-find "this is the code" directory. Well, after some exploring, I
mounted the [SquashFS](http://squashfs.sourceforge.net/) filesystem and
poked around a bit. Strange... seems to only have one real user (root)
and, though they claim this is a fully-functional LAMP server, no Apache
or MySQL. Really weird. Well, after poking for a few minutes, I found
the holy grail - `/root/.bash_history` was intact! Just a quick look
through it with `less` and I found what I was looking for: `/opt/lampp`.
It appears that the install is actually ApacheFriends'
[LAMPP](http://www.apachefriends.org/en/xampp-linux.html), or XAMPP for
Linux (gotta wonder if the guy writing this book doesn't even know how
to install Apache... I'm sure XAMPP for Linux is more bloated than a
customized build of Apache/MySQL/PHP from source, especially since it's
only being used to host 8 sample projects, so a lot could be left out).

Anyway, it appears that LAMPP is running in a chroot'ed environment. The
actual sample code is rooted at `/opt/lampp/htdocs/sites`. It seems that
*all* of the PHP files are also owned by root and chmod'ed 777! And
the top-level `index.php` file makes use of absolute links, so obviously
he never thought that someone may want to copy the sample code and use
it on a *real* box.

I just can't imagine someone who's a beginner with Linux, let alone a
Windows person, trying to get this source code onto a machine where they
can actually play with it. And... to make the situation worse... the
LiveCD has vi and vim, but no Emacs!!!! Eeeek!!

For anyone who needs it, I have the archive available [on my
site](http://rutgerswork.jasonantman.com/BDDW/PracticalPHPandMySQL.tar.gz).
For non-\*nix people, you'll need [Gzip](http://www.gzip.org/) or an
equivalent program to extract it.
