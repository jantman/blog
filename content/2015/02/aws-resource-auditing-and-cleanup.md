Title: AWS Resource Auditing and Cleanup
Date: 2015-02-11 17:18
Author: Jason Antman
Category: Ops
Tags: aws, ec2, cleanup, audit, automation
Slug: aws-resource-auditing-and-cleanup
Summary: Some thoughts on tooling to audit AWS resources and clean up unused ones.
Status: draft

- cleanup of AWS stuff
- name? Thresher - shark logo? CloudCycle? CloudMiser? AuditBot? RoboAudit? something with a connotation of cost savings, auditing, discarding unused things, or sorting things.
- bunch of resources

main points:
- find and cleanup forgotten/unused resources, terminate
- identify underutilized resources; flag for review
- overall policy auditing - security, etc. - keypairs, security groups, ACL settings, etc.
  - audit user accounts against an internal database (i.e. AD?) - separate issue
- cost allocation / reporting

cleanup:
- anything stopped longer than X days
- volumes, snapshots, launch configs older than X days and not used
- AMIs older than X days and not used anywhere (instances or other AMI)
- any instances with 'Packer' in the name, older than 1 day

underutilization:
- CPU - CloudWatch - instances below a given average threshold over a given amount of time
- this should be a plugin?
- low memory usage
- EBS volumes low used disk space - custom metrics, Diamond
- general sense here - we have a list of CloudWatch metric names, and a threshold for each one, along with an averaging period. want to flag any resource that has data for the metric, and it's below the threshold for the given period.
- flag for review

e.g.:
  - flag any EBS volume with less than 60% utilization over the past 3 days
    - with at least 3 days of data
    - that doesn't have tags matching a given list
  - flag any EC2 instance using less than 55% of memory (same other params as above)

security auditing:
- can come later

cost allocation:
- hourly job (with 1 day lock?) that looks in an s3 bucket for new detailed billing records
- if new, deletes the existing records for that billing record and parses into a DB (RDBMS? NoSQL?).
- calculates various rollups at parsing time
- metadata table for invoices / months
- keep raw records in one table? and rollup in others
- month-to-month comparison?
want to be able to:
- stuff like my HTML cost by project report
- arbitrary, ordered list of string tags
- explore costs by those tags (nested)
- explore by any one of those tags
- default view is nested, hierarchical using those configured tags (i.e. ['ApplicationName', 'ServiceClass', 'ResponsibleParty']), then under that by AWS service, then resource type, then... more specific (billing line type?)
- ability to filter by arbitrary ones of these - i.e. data transfer, etc.
- notifications for under-utilized/cleanup should include cost of the resource and savings

API for all of this
- API and form-based web UI for delaying resource deletion

- recurring job to detect resources nearing limits and take action - email or open ticket

- maybe NoSQL is best because no migrations, and can store bills natively?

- Celery is nice for us, but let's assume we want to find resources to be deleted and then enqueue tasks to delete them; Celery queue introspection is an unknown; we want to be able to have a web UI and API view of pending tasks / queue contents

Some default behavior, but plugins
- setuptools entry points plugins
- enable and disable plugins at runtime
- standardized API for plugins - shouldn't need to recompile, just install the plugins and restart the service (or maybe API call)
- plugin ideas:
  - determining contact information for a resource (deletion/notification)
  - textual description of a resource - i.e. how we format resources in email notifications
  - determining if a resource is a cleanup candidate
  - how soon certain resources should be cleaned up?
  - CloudWatch metrics to determine underutilized resources

- do calendar like SimianArmy - cleanup tasks and routine notifications only happen on non-holiday weekdays

- critical notifications - nearing resource limits, major security findings, etc. - should go out at any time

- cleanup plugins return true/false for whether or not a resource should be cleaned up
- plugins also return a confidence level of 0-10, 0 being "totally unknown, ignore me" to 10 being "do this NOW, I'm SURE".
- for a resource, execute every plugin and do whatever has the highest confidence. In a tie, don't cleanup wins over cleanup.
- for cleanup plugins, should return 0-9 for cleanup, reserving 10 for a "NEVER clean this up EVER" check
- e.g. for the notification info plugins, we might use ResponsibleParty with confidence=10, something based on ApplicationName confidence=5, Name tag munging confidence=2, then fall through to a catchall contact with confidence=1
- could have a plugin that takes a list of Name tags or instance IDs, returns False (do not clean up) with a confidence of 10
- builtin plugin that figures out which instance and DB this app itself is using, and sets do not clean up with confidence=10

- plugins should be configurable via web UI and ReST API. This should be a builtin feature, i.e. plugins should have namespaced configuration options (with defaults) that they can read/write from/to the database using common code in the base.
- e.g. a plugin to prevent deletion of instances with Name tags matching a given list of REs should be able to store those REs in the DB, and have them configured via API or web UI.

- integration with PuppetDB or other third-party CMDB type things, so that we can audit what's running inside the instance (i.e. OS version, etc.)
- same thing for AMIs, somehow???

missing part of this:
(1) authorization of resource creation, enforced tagging, tracking of resource creation with internal data, resource limit tracking. i.e. really what we're talking about is an EC2 API proxy that we could require every user on our account to go through, which would determine if the request should be granted, and if so, log it. OTOH, this is overkill for *our* organization because so far we've been successful in limiting AWS deployments to our tooling. Also, we have CloudTrail and can leverage that. It might be useful to determine what we're actually trying to enforce, such as approved OS images/configurations, etc. and then build tooling to audit on an ongoing basis to make sure everything in AWS meets those requirements.
(2) 

want to total up cost savings in cleanup reports

other stuff:
- users without MFA?
- instances not in VPC


References
-----------

* [Janitor Monkey](https://github.com/Netflix/SimianArmy/wiki/Janitor-Home), of course. What don't we like about it?
  * Conformity Monkey misses a lot of what we're concerned with. It reported NOTHING for our environment.
  * No cost analysis at all
  * No insight into resource utilization
  * EC2 instance cleanup logic is based solely on being removed from ASGs, which doesn't work with dev instances or CloudFormation.
  * Difficult to extend - write Java, compile, etc.
* some scripts to cleanup volumes, snapshots
* a blog on [Hooking into the AWS shutdown flow](http://copperegg.com/hooking-into-the-aws-shutdown-flow/) that's really just a phone-home at shutdown.
* [AWS re:Invent 2014 | (APP311) Lessons Learned From Over a Decade of Deployments at Amazon](http://bit.ly/1xV3o0i)
* [AWS re:Invent 2014 | (APP310) Scheduling Using Apache Mesos in the Cloud](http://bit.ly/11lNxeS)
* [AWS re:Invent 2014 | (APP304) AWS CloudFormation Best Practices](http://bit.ly/1qIOzh3)
* [AWS re:Invent 2014 | (APP306) Using AWS CloudFormation for Deployment and Management at Scale](http://bit.ly/1qJoSwF)
* [AWS re:Invent 2014 | (ARC307) Infrastructure as Code](http://bit.ly/11p59ag)
* [AWS re:Invent 2014 | (DEV308) Automating Your Software Delivery Pipeline](http://bit.ly/1uxoBeD)
* [AWS re:Invent 2014 | (PFC306) Performance Tuning Amazon EC2 Instances](http://bit.ly/1xLz86Z)
* The whole [re:Invent 2014 Security track](https://www.youtube.com/user/AmazonWebServices/Cloud)
* [Netflix Edda](https://github.com/Netflix/edda/wiki#dynamic-querying)
* Netflix Chronos (not OSS yet) - change logging via a ReST API
* [Scout2](https://isecpartners.github.io/Scout2/) AWS security auditing
* [AWS security resources](https://gist.github.com/chanj/6c48c059ad4b72a60bf3)
* [Reddit - Keeping your AWS Account Squeaky Clean](http://www.reddit.com/r/aws/comments/2uwxgv/keeping_your_aws_accounts_squeaky_clean/)
* [optimal-spyglass-open-source](https://github.com/OptimalBI/optimal-spyglass-open-source)
* [Netflix Ice](https://github.com/Netflix/ice)

