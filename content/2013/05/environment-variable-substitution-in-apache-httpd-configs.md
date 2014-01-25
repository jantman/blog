Title: Environment Variable Substitution in Apache httpd Configs
Date: 2013-05-11 12:01
Author: admin
Category: Tech HowTos
Tags: apache, environment, httpd, variable
Slug: environment-variable-substitution-in-apache-httpd-configs

I've been configuring Apache httpd for over a decade, from a single
personal web server to web farms running thousands of vhosts. In most of
the "real" environments I've worked in, we've had some variation of
production, stage/test/QA and development hosts; and usually some method
of managing configurations between them, whether it's source control or
generating them from template. And in all of these environments, there
has invariably been drift between the configurations in the various
environments, whether it's because of poor tools to maintain a unified
configuration or many of those emergency redirect requests that make it
into production but are never backported. This is made all the worse
because everywhere I've worked, the real difference between what
production and other environments *should* be is really just a string
replacement in Apache configurations - `/prod/` to `/test/` or
`www.example.com` to `www.dev.example.com` or something along those
lines.

Well a few days ago I was having a discussion with some co-workers that
dovetailed into this topic, and when I started some research, I found
(*finally after using httpd for years*) that the [Apache httpd 2.2
configuration file syntax
documentation](http://httpd.apache.org/docs/2.2/configuring.html#syntax)
states that httpd supports environment variable interpolation anywhere
in the config files (and [httpd
2.4](http://httpd.apache.org/docs/2.4/configuring.html#syntax) supports
it with Defines as well).

Yup, that's right. All those different Apache configs I've worked with
for years that define separate vhosts, document roots, rewrite targets,
ServerAliases, etc. for `www.example.com` and `www.qa.example.com` and
`www.dev.example.com` really only had to be
`www.${ENV_URL_PART}example.com`, and set `ENV_URL_PART` in the init
script or sysconfig file. (Of course this all assumes that you have your
different environments served by different httpd instances, which you
do, of course...)

For me, this is a very big deal. It means that finally, instead of
maintaining separate sets of configs for different environments which
are (theoretically, except for those emergencies) kept identical by
hand, or updating templates and then re-generating each environment's
configs, we can finally follow the same
commit/merge/promotion-between-environments workflow that we use for
other production code and Puppet configuration. It also means that those
pesky little rewrites and other minor tweaks will make it all the way
back to development environments.

So, here's a little example of how this would work in reality. Let's
assume that we have 3 main environments, `prod`, `qa` and `dev` (though
this should work for N environments) and that domains are prefixed with
"qa." or "dev." for the respective internal environments. We set
environment variables before httpd is started, on a per-host basis,
depending on what environment that host is in. On RedHat based systems,
we'd add the variables to `/etc/sysconfig/httpd` for production:

~~~~{.bash}
HTTPD_ENV_NAME="prod"
HTTPD_ENV_URL_PART=""
~~~~

or for QA:

~~~~{.bash}
HTTPD_ENV_NAME="qa"
HTTPD_ENV_URL_PART="qa."
~~~~

Those variables will now be available to httpd within the configurations
(and also to any applications or scripts that have access to the web
server's environment variables).

Now let's look at an example vhost configuration file that uses the
environment variables:

~~~~{.apacheconf}

ServerName example.com
ServerAlias www.example.com
# Aliases including proper environment name
ServerAlias www.${HTTPD_ENV_NAME}.example.com ${HTTPD_ENV_NAME}.example.com

ErrorLog /var/log/httpd/example.com-error_log
CustomLog /var/log/httpd/example.com-access_log combined

DocumentRoot /sites/example.com/${HTTPD_ENV_NAME}/

# Environment-specific configuration, if we absolutely need it:
Include /etc/httpd/sites/${HTTPD_ENV_NAME}/env.conf


RewriteEngine on
RewriteRule /foobar/.* http://www.${HTTPD_ENV_URL_PART}example.com/baz/ [R=302,L]


~~~~

Every instance of `${HTTPD_ENV_NAME}` will be replaced with the value
set in the sysconfig file, and likewise with every instance of
`${HTTPD_ENV_URL_PART}`. This way, we can have one set of configurations
and use our normal source control branch/promotion process to both test
and promote changes through the environments along with application
code, and ensure that any straight-to-production emergency changes
(everyone has customer-ordered rewrites like that, right?) make it back
to development and qa.

One caveat is that, if the environment variable is not defined, the
`${VAR_NAME}` will be left as a literal string in the configuration
file. There doesn't seem to be any way to protect against this in httpd
2.2, other than making sure the variables are set before the server
starts (and maybe setting logical default values, like an empty string,
in your init script which should be overridden by the sysconfig file).

If you're running httpd 2.4+, you can turn on
[mod\_info](http://httpd.apache.org/docs/2.4/mod/mod_info.html) and
browse to `http://servername/server-info?config` to dump the current
configuration, which will show the variable substitution.
