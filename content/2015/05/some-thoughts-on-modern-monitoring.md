Title: Some Thoughts on Modern Monitoring
Date: 2015-05-03 23:10
Author: Jason Antman
Category: Monitoring
Tags: monitoring, nagios, icinga, alerting, graphing, trending, notifications
Slug: some-thoughts-on-modern-monitoring
Summary: Some thoughts on the state of monitoring and what we need.
Status: draft

Tools like Puppet, Chef and their ilk (Salt, Ansible, etc.) have done wonders for how systems are
managed and configured. But it seems that much of the monitoring space has been left behind. Sure,
services such as NewRelic, AppNeta, Sensu, etc. provide good solutions, or at least parts of solutions,
but it seems that the open source world has fallen far behind the times.

Nagios is the de-facto standard, but it still abides by a dated "everything is a machine, and every machine
is persistent" paradigm. It doesn't play well with a highly dynamic, virtualized, autoscaling world. The fork
that I've run lately, Icinga, makes some improvements on the original by providing database-backed configurations
and an API, but that's still at best a bolt-on fix. The open source world has done great things with log
collection and analysis (Logstash) and metric collection and display (Graphite and the many related projects),
but these focus on getting the data, not acting on it. Some interesting solutions have come out of companies
such as NetFlix (<<<links>>>), but they're not really easily-usable general-purpose solutions.

So, what should monitoring in the new world look like?

- Not everything is a machine. We care as much about services and APIs as we do about hosts (probably more).
So, first off, the Nagios paradigm of hosts and services is dated. Firstly, it needs a higher-level container,
such as an Application, that describes a "thing" running across multiple hosts, comprised of multiple services.
There are some hacks to get Nagios to work this way (check-multi, anyone?) but there needs to be a real, high-level
object that understands concepts such as load balancer pools. Also, not every "thing" we want to monitor is a
network host.
- We now live in a highly dynamic world with autoscaling and service registries. Adding another host (whether it's
a VM or an EC2 instance or a container) of a given type should be a simple task in the monitoring tool.
- Similarly, configuration needs to be more centralized. Nagios' check execution model is horribly archaic. There should
be some sort of agent running on monitored hosts that knows what's running on the host and what checks are available. A
central tool should know how to monitor those things. I.e. the agent should report in and say, "Hi, I'm a production
(based on tags or some local configuration) web server running Apache for the FooBar application." The central server
should then determine, "ok, run these checks with these intervals and tell me the results."
- Metric collection and monitoring should be unified. We want numeric data points not boolean values. Our alerting and
graphing systems should use the same data.
- We should be able to query data out of existing data stores, whether it's Graphite or an API. The big paradigm change
here is taking advantage of bulk queries. A query for state of ALL of our EC2 instances should update the correct things.
Executing a command for every host or service check is bad.
- Service discovery and host discovery.
- Notifications. They should have multiple contact methods built-in, and something like PagerDuty. Additionally, end users
should be able to easily manage their own notifications (in addition to central management).
- Default notifications shouldn't be based on fixed thresholds, they should be based on rate of change over time.
- Stop all this SSH nonsense. Either run a daemon specific to this and listening on its own port and API, or use a message
queue. Maybe just use MCollective for some of it.
- Configuration should mostly be stored centrally. The only configuration on a client should be what AM I. The central
service should determine what to do/run and how often.
- We can't think of "nodes" as being able to run an arbitraty daemon. Sort of contrary to the above. We want a daemon
for machines that can run it, and for it to be part of the core project, not some bolt-on. But we need to be able to consider
things that can't run our software - i.e. appliances with their own APIs - as the same first-class citizens that other
things are.
- We need to be able to handle data that isn't just numbers, let alone booleans. Ideally, direct integration with something
like LogStash. Also, what about application-level metrics? What about code introspection and traceback handling like NewRelic?

- Or maybe what we need is just something that pulls all of this together? i.e. Ring of Power that binds (both configures and
pulls data out of) Logstash, NewRelic, Graphite, and some monitoring tool to provide a unified interface and experience and
notifications, as well as update these things dynamically.
