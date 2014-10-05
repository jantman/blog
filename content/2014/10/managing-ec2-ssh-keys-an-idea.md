Title: Managing EC2 SSH Keys - An Idea
Date: 2014-10-04 11:59
Author: Jason Antman
Category: Tech HowTos
Tags: ssh, ec2, aws, keys, public key, pubkey
Slug: managing-ec2-ssh-keys-an-idea
Summary: An idea on how to manage EC2 SSH keys for a large number of users

At work, we have a bunch of EC2 instances (currently hundreds, and growing quickly). We also have a bunch
(probably now around 100, counting contractors) of users. Some users - mainly engineers - need SSH access to all
of the EC2 instances; many others only need access to their team's instances. While I usually advocate sanity checks
and training over access control for employees, many teams have expressed legitimate concern that they don't want
others on their instances; commands that are safe to run in dev/test (like loading test data) might be disastrous
on production instances. So, as part of our automation and tooling team, I've been trying to come up with a way to manage
access to all these instances. Right now we have a single "bastion" (a.k.a. jump box / ssh gateway / keyhole) instance, with a single
shared used keyed to access every EC2 instance; that doesn't scale and doesn't meet the security requirements.

What follows is one theory of mine on how to solve this problem. I've been thinking about this for the past
day; this might not be the Right answer, and it's just a theory at this point, but I think it works.

Requirements and Assumptions
=============================

* We have Active Directory as the one source of authentication/authorization truth, but it's only in the corporate
  network. For various reasons both technical and political, accessing it from AWS (whether directly, over VPN,
  via replication, or via data feeds to a separate LDAP infrastructure in EC2) is simply not possible.
* We want to control SSH access to a bunch of instances. Some of them are persistent and some are ephemeral. Some
  are pre-baked AMIs in auto-scaling groups, with _no_ changes made outside the AMI. Some of them are persistent
  or semi-persistent instances that run Puppet every 30 minutes. Some of them are somewhat special, and can't be
  trivially torn down.
* Most of our instances are in a VPC, and have proper security controls which include SSH access from only a specifically
  white-listed range of IPs. However, some instances are in "EC2 Classic" and have SSH open to the world. We want a
  solution that also protects these instances.
* We're mainly concerned with securing access from (a) users inadvertently accessing an instance they shouldn't be
  on, (b) outside/untrusted parties, and (c) former employees. We trust our employees within reason, and accept that,
  within our security stance, if an employee _really_ wants privilege escalation, they're going to get it. We're not
  overly concerned with protecting against determined, malicious users who already have some access but want more.
* Our current process for security cleanup for former employees is largely based on corporate IT (or is it HR?) turning
  off their AD account. We want to minimize additional steps that need to be completed when someone has access revoked.
* Any solution that we choose needs to be usable with self-service AWS; i.e. any user can spin up their own instances
  or stacks, provided that they use an AMI that is either built by our automation team, or follows guidelines on what
  must be included in all AMIs.
* We have some administrative accounts (Jenkins, as well as some shared privileged accounts on select machines) that need
  unrestricted access to everything.
* Local user accounts aren't an option. This would mean running Puppet constantly on every image and/or rebuilding
  every image each time we gain or lose an employee. That would be especially difficult when we occasionally have
  project-based contractors.
* We're OK with having a bastion/keyhole server in AWS, we just don't want everyone to be able to access everything.
* Our intended network security stance is to have bastion/keyhole servers in AWS (ideally one per AZ), which are only
  reachable via SSH from selected public addresses on our corporate network (which can only be reached by current
  employees with valid, working access). All other instances should only allow SSH from these selected hosts.
* Despite the above, we don't want to rely on an instance being properly configured as our only security measure;
  if an instance is incorrectly configured to accept SSH from 0.0.0.0/0, we still want to prevent users whose
  access has been revoked from logging in to the instance.
* We don't need access to be granted and revoked immediately. We'll assume that in normal operating conditions,
  thirty (30) minutes is a reasonable amount of time to either grant or revoke a user's access.
* We want to minimize reliance on our existing corporate infrastructure, so that AWS can be used for business
  continuity purposes.

Main Goals
===========

* Provide users with SSH access to EC2 servers; privilege should be able to be granted to a subset of users and/or groups
  for each "application". Users should not be able to access other instances.
* Allow a fixed list of users access to every instance.
* Be able to revoke a user's access without rebuilding instances or ssh-in-a-loop'ing to all of them.
* Many instances are not going to be running Puppet after initial provisioning/AMI creation, so as much as we love Puppet,
  it's not an option to solve this problem.
* This should involve a minimum of administrative overhead when a user leaves the company.

Proposed Solution
=================

My solution relies on SSH agent forwarding and the ``AuthorizedKeysCommand`` introduced in OpenSSH 6.2 (see "Limitations", below, for more information),
most likely inspired by (or maybe literally the same code)
as the patch formerly used by GitHub. This allows sshd to execute an arbitrary command, passing it the login username, which returns output identical to what would
be in the ``authorized_keys`` file. If none of the keys successfully authenticate the user, authentication continues using the usual ``AuthorizedKeysFile``. We take
advantage of this feature, in addition to SSH agent forwarding, to provide our granular access control. Public keys are pulled from a central location _at login time_
(and cached for a set amount of time); each user has control over their own public keys, and a central process builds sets of public keys authorized to access a given
group of instances.

Infrastructure
---------------

Each EC2 instance will be a member of an Access Group, which is a unique identifier for the set of users authorized to access instances
in the group. In implementation, Access Groups will likely just be a tag on EC2 instances that maps to a set of predefined values
(see below for more).

We will have a number of "bastion" (keyhole/jump box/SSH gateway) hosts, ideally one in each Availability Zone where we have instances.
These bastion hosts will only be reachable from within our corporate network (or our VPN); therefore, users must have
current access to our corporate network (where we can rely on Active Directory and other systems to handle authorization) in order to
gain access to AWS. All other EC2 instances will only be reachable over SSH from one of these bastion hosts. The bastion hosts themselves
will not have SSH keys to access other instances; they will, however, have SSH agent forwarding enabled.

Users reach AWS instances by SSHing from a host attached to our corporate network (including VPN hosts) to a bastion host in EC2. From there,
they SSH to the destination instance, making use of SSH agent forwarding to use their local key to authenticate to the instance. We get both
a restricted entry point to AWS (the bastion host, which can enforce further security and logging methods) and the ability to authenticate users
using their own personal public keys on the destination instances.

To make it easier for end-users, we could develop a wrapper script like [Instagram's ec2-ssh](https://pypi.python.org/pypi/ec2-ssh) that
checks for a valid, running ssh agent with keys in it, and then crafts the correct SSH command to land the user on the desired end
host - i.e. something like ``ec2ssh instance_id`` would generate and execute a command like ``ssh -At bastion_hostname 'ssh instance_ip'``.

On the Servers (Instances)
-------------------------

Each instance, when initially built/provisioned, is given a ``get_authorized_keys`` script, which is configured to be run by sshd as the
``AuthorizedKeysCommand``. This script uses one of the following three public key distribution services to retrieve the authorized public keys
for that instance, which are then echoed on STDOUT and used to authenticate the user. For the sake of simplicity, we'll assume (which is
currently the case in our infrastructure) that this script will only run for a single non-root user that is used for logins; it will exit
without returning any output for any other users on the system, effectively preventing logins to them.

The script will first check for authorized keys cached locally (either on disk or in memory, to be determined). If they're found and less
than some age threshold (we'll say five minutes), the cached version is returned. This is intended to both reduce latency when performing
multiple sequential logins, and to allow logins to continue functioning through short periods of degraded network connectivity. If no recent
keys are found cached on disk, the script will retrieve them from the configured public key distribution service. If the service does not
return an appropriate response within an acceptable time limit, or is unreachable, the script will exit with no output. This will prevent
logins from users authorized with this method, but will fall through to the standard ``AuthorizedKeysFile`` method. A number of permanent
authorized public keys will be included in each instance, to allow emergency administrative access in the event that the key distribution
service fails.

If we're willing to assume that the instances themselves are trusted (which I think is a valid assumption), the key retrieval script on
each instance will determine the Access Group that the instance belongs to, and then request the authorized keys for that Access Group.
Determination of Access Group will likely be made via user data passed into the instance at provisioning time, or via retrieval of a
tag value for the instance.

If assuming trust locally on the instance is not sufficient, then the burden of identifying the instance's access group is shifted
to the key distribution service (likely by identifying the IP address of the requesting instance, and then using the EC2 API to
determine which group that instance belongs to). With this solution, only the second alternative key distribution service is
feasible.

If a shorter delay to authorization changes is needed, it would be feasible for instances to also run a separate process
(cronjob, daemon, etc.) that polls the key distribution service at a regular interval to check for updates (i.e.
HTTP HEAD, something SQS-based, etc.) and updates the local cache when they occur.

Public Key Distribution Service
===============================

Instances will retrieve their authorized public keys from a key distribution service. Three examples follow:

Alternative 1 - Scalable Architecture - AWS and Local
-----------------------------------------------------

Keys will be managed by a web-based application (with a complete and documented API) living in the corporate data center.
The application will provide facilities for authorized users (managers, operations) to define new Access Groups and modify
the list of users allowed to access them. Individual end-users will be able to manage their public keys. At a set interval,
a standalone script will retrieve a list of all users defined in the application and check the status of their corporate Active
Directory accounts. Any users whose accounts have been deactivated or locked will be flagged as such in the application. Whenever
a change is made in the application (including a user being flagged as deactivated), all Access Groups that include that user
will have their authorized\_keys file (composed of the authorized\_keys files of all users with access) written to an S3 bucket
that's only writable by the privileged
user running the application. All instances will have IAM roles that allow them to read the bucket.

This method allows us to provide self-service to users and application administrators, and keeps all data about users within
the corporate network. It provides automatic revocation of access for disabled Active Directory accounts. It does introduce
a delay in revocation of access for disabled AD accounts, but a delay of ~10 minutes is certainly not a concern in our
environment.


Alternative 2 - Scalable Architecture Entirely in AWS
-----------------------------------------------------

A similar application exists, but lives entirely in AWS, utilizing its native high availability technologies (i.e. multi-AZ
RDS as a data store). A script still runs in the corporate data center, but all it does is query the API for a list of all
active users, check AD account status, and deactivate any users that no longer have a valid account. Instead of writing the
authorized key files to an S3 bucket, the application serves them directly in real-time. The application could
store keys and data in a RDBMS, or perhaps something like OpenLDAP, depending on which technologies are best known and
what the performance requirements are.

This is more of an infrastructure challenge and introduces additional points for failure; if the application above (1)
fails, it will only impact _changes_ to access, whereas if this application fails, all user access (aside from the static
emergency keys) will break. However, this method allows us to control access at a level finer than Access Groups; rules
could be developed based on any attributes of the requesting instance, including (if the latency was allowable) queries
to the EC2 API for instance-specific data.

Alternative 3 - Simple Architecture
-----------------------------------

A text file stores mappings of Access Groups to the Active Directory users and groups authorized for them. The text file
is manually maintained, stored in version control, and all changes must comply with an access policy and be peer-reviewed.
A script runs at a set interval (let's say cron every 5-10 minutes) that reads the user/group mapping, translates groups
to their membership list, and checks the AD account status of every listed user. Users without valid/current/enabled accounts
are removed from the lists in memory. For the remaining (active) users for each Access Group, their ``~/.ssh/authorized_keys``
file is read. All user's authorized_keys files are concatenated together per Access Group, and the result is written to
an S3 bucket.

This is by far the simplest method, and relies on our NFS shared home directories to allow users to manage their public
keys by simply using the standard file. This keeps all user-related data in our corporate data center, and means that we
have only one script and its' cron job to maintain, rather than a whole application. The text-file-based method of access
control isn't terribly scalable, but it should work for the ~100 users that we have to deal with. Checking AD account status
when generating the file should provide a feasible safeguard for users whose corporate accounts are locked/revoked without
requiring someone to remember to also remove them from the AWS user list.

Advantages Over Other Solutions
-------------------------------

* Self-service for users and for managers/administrators of applications.
* No manual intervention when a user leaves the company; users automatically deactivated when their AD account is.
* No cron job or daemon to run on instances, and no centralized process to break key distribution; each instance
  automatically pulls the current authorized keys when a login is attempted.
* Doesn't depend on Puppet, so it allows individual applications to use Puppet as they desire, without complication
  or confusion.
* Only depends on centralized (corporate data center) infrastructure for key updates (at most). Failure of connectivity
  between AWS and the corporate data center can be worked around assuming there is an alternate path of access (such as
  a bastion host that allows logins from engineers/managers from a trusted outside host).
* Management of access can be delegated to application owners/managers, while still allowing engineers full access.
* Uses the strength of public key authentication; no passwords to change.
* Ensures that select static trusted keys always have access to instances, even during a failure of the key distribution
  system.
* In emergencies, keys could be distributed directly to the authorized\_keys file, bypassing the distribution system,
  or key file cache lifetime could be increased.
* Can be easily audited by having a scheduled job add a key for all instances, wait ~15 minutes, and then attempt SSH
  connections to all instances.

Trade-Offs
-----------

* Delay between user access addition/removal and updates (though this can be minimized by a shorter cache time).
* Latency during initial login with a cold cache.
* Addition of another system that could break.

Limitations
-------------

My company is a CentOS shop. The ``AuthorizedKeysCommand`` feature of OpenSSH itself was only released in [OpenSSH 6.2](http://www.openssh.com/txt/release-6.2),
on March 22, 2013. A patch for it was backported to the 5.3p1 version of openssh-server in RHEL and CentOS 6. However,
this method will certainly not work on CentOS 5, which is still running OpenSSH 4.3. Be aware that when the new ``AuthorizedKeysCommand``
feature was backported, the man page was not updated; ``man sshd_config`` is still conspicuously missing these options, and I couldn't
find anything in the RPM changelog about it, but the ``openssh-5.3p1-authorized-keys-command.patch`` file is clearly there in the
5.3p1 SRPM, and the options are there but commented out in the ``sshd_config`` it provides. I actually thought this would be near-impossible
to do on CentOS 6 until I found the ``openssh-ldap`` package (in the default repos) and discovered that it uses this feature.

Also, this solution requires (depending on which alternative is chosen) working access to either S3 or instances serving an application.
Assuming proper configuration (and distribution across AZs) this should be a non-issue.

Accountability
---------------

If accountability is a concern, we will handle this through detailed logging in every step of the key creation, authorization, distribution
and retrieval process. In addition, all instances will run sshd with ``LogLevel VERBOSE``, which will log the fingerprint of all public keys
used to connect to the instance. Logs will be written to a secure, append-only medium.

References and Further Details
==============================

* There is an existing ``openssh-ldap`` package in CentOS that provides instructions on setting up public key storage in an LDAP backend,
  using ``AuthorizedKeysCommand``.
* [Someone said](http://andriigrytsenko.net/2013/05/authorizedkeyscommand-support-and-centosrhel-5-x/) they successfully built the current
  6.2 OpenSSH for RHEL/Cent 5.
* An EC2 instance can retrieve its own tags using tools such as ``awscli`` or ``ec2-api-tools`` and an appropriate IAM role set on the instance.

Rejected Ideas
===============

While thinking through this I considered and rejected a number of alternate methods. Here are some of them:

* While SSH's relatively new Certificate support (CA-based) sounds nice, it doesn't solve the problem; according to
  [this blog post](http://neocri.me/documentation/using-ssh-certificate-authentication/) it uses a CA to sign keys,
  but doesn't do a CRL lookup, it relies on a RevokedKeys file manually sync'ed to all servers. So, this poses the
  same problem as managing authorized_keys as a file distributed to instances.
* Managing per-application users or groups on the AWS bastion hosts requires a lot of administrative overhead, and isn't really an option for us.
  Though this would be a simple implementation using either groups for each application with private keys group-readable,
  or using per-application users and the proper sudo configuration.
* Prior to finding out about ``AuthorizedKeysCommand``, my top idea was essentially this same implementation on the
  key distribution server side, but writing it to an S3 bucket, and running a cronjob on each EC2 instance to pull
  down the authorized\_keys file.
* Just Don't - See [this blog post](https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/)
  as a reference. But the gist is, "If you have to SSH into your servers, then your automation has failed".
  Sure, development and test stacks will be spun up, probably with either a single user's key, or a shared
  key. But after that (i.e. in prod), instances are cattle. Logs should be shipped to a central store, CloudWatch
  and/or other monitoring technologies (i.e. NewRelic, Diamond to graphite) should get most of the data that's
  needed. I'm not seriously agreeing to __disable__ SSH access, but to put in place the tools that it's needed
  so rarely (on non-dev instances) that it's feasible to ask one of a small group of privileged people to
  perform the task.
* Trust our users - If someone can push to master, full control of our systems is just a backtick (or popen) away.
  Recognize that if someone wasn't trustworthy, we wouldn't hire them. Let everyone access a single bastion host.
  Discourage unauthorized use via strong password policies and other standard security measures
  (perhaps OTP-based two-factor authentication). Discourage malicious use via detailed audit logging, with logs
  shipped to an append-only secure storage location.
* SUID wrapper script - All users have SSH access to a bastion host as their normal
  active directory user. They run a SUID wrapper script that has a list of which users are allowed to access
  which EC2 instances (or security groups, subnets, etc). When the user calls this script, it checks if the
  specified host is in a group they're allowed to access, and if so, SSHes to that host using a key only readable
  by the owner of the script. This is somewhat complex; there's a good possibility of security issues with the
  script itself, and it means that we're probably only allowing interactive logins - we're limited by the
  capabilities of the wrapper script, it's not just a normal SSH client.
* Key Pushing- A script runs in one central location. It has a mapping of which users/groups are allowed
  to access which EC2 instances. Every X minutes the script runs. It grabs ``~/.ssh/authorized_keys`` for all
  users that are allowed EC2 access, and then generates an authorized\_keys file for each group of instances.
  The script checks a cache, and if the file has changed for a group of instances since the last run, it queries
  the AWS API to determine which instances are in that group, and distributes the authorized\_keys file to them.
  The "distributes" part would, unfortunately, probably have to be scp.
* Bastion host per application. Users are allowed access to this host either via authorized\_keys managed by Puppet,
  or via sudoers rules on a bastion host in the corporate network. But yeah, we'd end up with a __lot__ of these.
* Various thoughts around AD in the cloud, replicated AD in the cloud, OpenLDAP in the cloud pulling from AD, or
  AD over VPN. These were all rejected either because of corporate security policies, or because relying on internal
  AD for authentication would mean that a data center or connectivity failure also affects AWS.
* Puppet - We actually *run* puppet on every instance. Maybe against our master, maybe masterless with a script
  to deploy some modules before every run. At a minimum, it manages ssh authorized keys for ec2_user. We implement
  some method where each user has a manifest with their own public keys, that they can maintain. Managers can add users
  to the group(s) for their applications, and that users' keys are automatically deployed. Revoking keys, on the other
  hand, is a bigger problem. This requires some sort of "this person is going away" procedure, which currently doesn't
  exist (or involve the groups who maintain AWS infrastructure), and would be one more thing for a human to forget.
  There are also instances that have "special stuff" going on with Puppet that would complicate this.
* Generate a list of authorized keys, turn it into a manifest, and run puppet masterless on it via a cronjob (pulling
  the manifest from S3). This involves most of the same problems as above, plus means that we have Puppet running
  in two different ways on some instances (triggered via mco against a master, and cron'ed in apply mode).
