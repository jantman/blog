Title: AwsLimitChecker - Check Your AWS Usage Against Service Limits
Date: 2015-07-25 08:35
Author: Jason Antman
Category: Projects
Tags: aws, ec2, limits, python, awslimitchecker, cloud
Slug: awslimitchecker-check-your-aws-usage-against-service-limits
Summary: Initial release of AwsLimitChecker, a tool to check your AWS usage against service limits and Trusted Advisor.

Over the past year or so, at my day job, we've been leveraging AWS more and more, specifically
[CloudFormation](https://aws.amazon.com/cloudformation/) to manage complete application stacks. One
side-effect of this is that we went through a few periods where we were constantly hitting various
AWS Service Limits - subnet groups, ElastiCache clusters, security groups, and a whole slew of others.
In pretty much all these cases, we weren't *really* aware of the limits; we (the Tooling and
Automation team) had succeeded in our goal of handing our internal customers the tools to spin up
complete application environments, per-developer, on-demand. And it was wonderful until we hit some
magic number of CloudFormation stacks, at which point almost every day for a week or two we had to
open a new AWS Support ticket to have a different limit increased, and deal with completely broken
deploys until that was done (or send out a frantic "someone please delete a dev stack" email).

Early last month we decided that we had to do something about this. As much as I tried, I couldn't
find an existing solution that would monitor our limits and alert us when we approached them; there
were some open source scripts that would do so for a handful of limits (generally just EC2 usage),
and the proprietary solutions that I was able to find didn't seem much better; none of them stated
that they handle VPC or ElastiCache limits, which had been problematic for us. AWS's own
[Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/) has a Service Limits
check available to Business- and Enterprise-level support accounts, but it only monitors 17 of the
94 Service Limits that we identified as relevant to us, and it sends out *weekly* alerts. So,
I decided to write something to solve the problem. My co-workers and I have been trying to get
corporate legal approval to release our work publicly under an OSI-approved license for years,
to no avail. I asked my team if they'd support waiting a while for this work, so I could do it
entirely in my own time, publicly, under an open source license. Happily, they agreed.

Today I'm making the first release of [awslimitchecker](https://github.com/jantman/awslimitchecker),
an AGPL 3.0-licensed Python tool to calculate your AWS resource usage for various services bound by
[service limits](http://awslimitchecker.readthedocs.org/en/latest/limits.html#current-checks), and tell you which ones exceed a given threshold (actually, warning and critical
thresholds). Effective limits are hard-coded to the [published defaults](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html),
but can be overridden in cases where you've received limit increases, and will be automatically updated
from Trusted Advisor data for all limits that it monitors (if your account includes the full TA checks).
awslimitchecker provides warning and critical thresholds that can be set globally as a percentage of the
limit (defaults are 80% and 99%, respectively) or overridden on a per-limit basis, as either a percentage
or a fixed integer usage value.

awslimitchecker is available [from pypi](https://pypi.python.org/pypi/awslimitchecker/0.1.0).
It is compatible and tested with Python versions 2.6 through 3.4, though the library it uses to communicate
with AWS, [boto](http://boto.readthedocs.org/en/latest/), still has a few AWS services which are not python3-compatible.
awslimitchecker includes both a Python module with a [documented API](http://awslimitchecker.readthedocs.org/en/latest/awslimitchecker.checker.html) for those who
don't mind working with Python, and a command line script for those who do.

The project is still very young, and only being used by one organization, but it's proven
stable for us, and I'm more than happy to accept questions, comments, criticisms,
[issues/feature requests](https://github.com/jantman/awslimitchecker/issues) and Pull Requests.
 
