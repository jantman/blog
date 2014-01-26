Title: Nagios check_by_ssh and NAT
Date: 2009-10-22 13:58
Author: admin
Category: Monitoring
Tags: monitoring, Nagios
Slug: nagios-check_by_ssh-and-nat

At a remote location, I have a number of machines to monitor but only
one IP (dynamic on a residential connection). Most of my remote
monitoring with Nagios uses check\_by\_ssh. Previously, I'd used one
host for Nagios to SSH to, and then chained together another
check\_by\_ssh to reach the remote hosts. Unfortunately, this means
nothing past the one first host can get monitored if the first host is
down. All of the other hosts (everything is behind NAT) have SSH visible
externally on different ports.

SSH itself doesn't like one IP/hostname with SSH on different ports -
host key verification will fail, as the SSH client only looks at the
address that it's connecting to, not the port number. Normally, this is
bypassed by using a `.ssh/config` file like:

~~~~{.text}
Host foo1
        Hostname foo.example.com
        HostKeyAlias foo1
        CheckHostIP no
        Port 22
        User nagios

Host foo2
        Hostname foo.example.com
        HostKeyAlias foo2
        CheckHostIP no
        Port 222
        User nagios

Host foo3
        Hostname foo.example.com
        HostKeyAlias foo3
        CheckHostIP no
        Port 10022
        User nagios
~~~~

And then you SSH using the "Host" named in the config file, not the
actual hostname.

Unfortunately, the only way to get check\_by\_ssh to do this was a bit
messy, and required defining a bunch of extra macros for each host:

~~~~{.text}
./check_by_ssh -o Hostname=foo.example.com -o HostKeyAlias=foo1 -o CheckHostIP=no -o Port=222 -o User=nagios -H foo.example.com -C uptime
~~~~

So, I made a quick little patch for check\_by\_ssh.c (patched against
the released nagios-plugins-1.4.14) :

~~~~{.diff}
--- check_by_ssh.c      2009-10-22 14:32:26.000000000 -0400
+++ check_by_ssh_ORIG.c 2009-10-22 14:12:15.000000000 -0400
@@ -181,7 +181,6 @@
                {"skip", optional_argument, 0, 'S'}, /* backwards compatibility */
                {"skip-stdout", optional_argument, 0, 'S'},
                {"skip-stderr", optional_argument, 0, 'E'},
-               {"ssh-config", optional_argument, 0, "F"},
                {"proto1", no_argument, 0, '1'},
                {"proto2", no_argument, 0, '2'},
                {"use-ipv4", no_argument, 0, '4'},
@@ -199,7 +198,7 @@
                        strcpy (argv[c], "-t");

        while (1) {
-               c = getopt_long (argc, argv, "Vvh1246fqt:H:O:p:i:u:l:C:S::E::n:s:o:F:", longopts,
+               c = getopt_long (argc, argv, "Vvh1246fqt:H:O:p:i:u:l:C:S::E::n:s:o:", longopts,
                                 &option);

                if (c == -1 || c == EOF)
@@ -222,7 +221,7 @@
                                timeout_interval = atoi (optarg);
                        break;
                case 'H':                                                                       /* host */
-                 /* host_or_die(optarg); */     /* commented out 2009-10-22 by jantman for ssh config file use */
+                       host_or_die(optarg);
                        hostname = optarg;
                        break;
                case 'p': /* port number */
@@ -300,12 +299,6 @@
                        else
                                skip_stderr = atoi (optarg);
                        break;
-               /* added 2009-10-22 by jantman for ssh -F option (config file) */
-               case 'F':                                                                       /* ssh config file */
-                       comm_append("-F");
-                       comm_append(optarg);
-                       break;
-               /* END added 2009-10-22 by jantman */
                case 'o':                                                                       /* Extra options for the ssh command */
                        comm_append("-o");
                        comm_append(optarg);
@@ -411,8 +404,6 @@
   printf ("    %s\n", _("Ignore all or (if specified) first n lines on STDERR [optional]"));
   printf (" %s\n", "-f");
   printf ("    %s\n", _("tells ssh to fork rather than create a tty [optional]. This will always return OK if ssh is executed"));
-  printf (" %s\n", "-F");
-  printf ("    %s\n", _("path to ssh config file [optional]"));
   printf (" %s\n","-C, --command='COMMAND STRING'");
   printf ("    %s\n", _("command to execute on the remote machine"));
   printf (" %s\n","-l, --logname=USERNAME");
~~~~

It works fine. The only problem is that I disabled the check that the
given hostname/IP is valid, so instead of getting a nice "Invalid
hostname/address - foobar" error, you'll get the usual "Remote command
execution failed: ssh: foobar: Name or service not known" error (though
it will still give an exit code of 3). I had to do this because
check\_by\_ssh was checking for a valid hostname itself, though SSH
needs to be passed the "Host" alias as defined in the config file.

With the patch, we now have something nice and clean like:

~~~~{.text}
./check_by_ssh -H foo1 -F /home/nagios/.ssh/config -l nagios -i /home/nagios/.ssh/id_dsa -C uptime
~~~~

Which only adds the "-F" flag to what I was already using, and is safe
to use for all hosts.

When I get a chance, I'll figure out a way to gracefully deal with the
host aliases ("fake hostnames") and submit a patch. Most likely, I'll
add another option so that you have to specify both the actual hostname
(so it can check that it exists) and the alias used in the config file
(perhaps "-a"?)
