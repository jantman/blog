Title: Pre-Authorized AWS Console URLs for Notifications
Date: 2017-10-08 19:14
Modified: 2017-10-08 19:14
Author: Jason Antman
Category: Monitoring
Tags: aws, iam, monitoring, notifications
Slug: pre-authorized-aws-console-urls-for-notifications
Summary: Pre-authorized AWS Console login URLs with limited permissions allow immediate investigation from notifications.

## Background

Almost all of my work for the past two and a half years has revolved around Amazon Web Services,
but my personal AWS account (mostly a single tiny t2.micro instance that handles a tiny amount
of HTTP traffic and some cron jobs) has languished. Recently I've undertaken a project to modernize
it, moving from an EC2 instance using an AMI baked by [Packer](https://www.packer.io/) and some
custom Ruby code to manage it, to a barebones instance acting as an
[Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) Docker host, and all of my applications
running in containers. This makes for much easier testing and deployment, and is a lot lower effort than
baking and testing a new AMI every time I want to change an nginx config file (yes, everything is immutable).

I've got most of the basic work done and every resource in the account imported into
[terraform](https://www.terraform.io/), containers created and tested to replace what my old EC2
instance is doing, and terraform management of the ECS tasks and services too. So, I decided that
I'd better setup some monitoring of all this before I forget about it. I try my best to keep my account
in the free tier for AWS; my bills have usually been about $15 USD/month in the past (mostly the t2.micro
instance and Route53) and I'm expecting to go up to about $20/month with the new infrastructure.

I've gotten some basic monitoring in place - 7 CloudWatch Alarms for the important things, and a
Lambda function running every 30 minutes that does some more complicated and non-metric checks (and
sends to the same SNS topic as the alarms if it finds a problem). However, I realized how spoiled
I've been at my day job, where a lot of our AWS monitoring infrastructure relies on
[Datadog](https://www.datadoghq.com/) and [PagerDuty](https://www.pagerduty.com/) (both
of which I love not only for their functionality but also for their APIs). While the new
[CloudWatch Dashboards](https://aws.amazon.com/blogs/aws/cloudwatch-dashboards-create-use-customized-metrics-views/)
feature is pretty cool for a tiny infrastructure with no other monitoring tools
(and they can finally be managed via API), CloudWatch still had two big pain points for me
(aside from [cost past the free tier](https://aws.amazon.com/cloudwatch/pricing/)):

1. There's no option for re-notification from Alarms; if you set an SNS Topic target for a
  CloudWatch Metric Alarm, the notification is sent _once_ when the Alarm changes state.
  And that's it.
2. The notification messages are horribly plain.

To solve the first problem, I just have my custom monitoring Lambda function also check
for any CloudWatch Alarms in a non-OK state for longer than 30 minutes (how often the
function runs) and re-notify for them. The second solution is a bit more involved...

## The Problem

The Lambda function that I put in place to do some monitoring sends alerts to a SNS Topic
that delivers them to my phone via SMS and to my personal email account. While I've made use
of the ability to [send different messages per protocol](http://docs.aws.amazon.com/sns/latest/dg/PublishTopic.html#sns-message-formatting-by-protocol)
to send a short notification to SMS and a longer email, I still really miss the rich context
of notifications from real monitoring systems that include graph images and other useful
information. This becomes an even bigger inconvenience since I'm rarely logged in to the
AWS Console for my personal account, and doing so involves a dance with several long passwords
and MFA tokens.

So, I wanted a way to be able to receive an SNS monitoring notification and actually _see_
the metric graphs or events that generated it, rather than getting a plaintext (yeah, the
Simple _Notification_ Service is clearly designed for SMS and mobile push, and can't even
send HTML email) description of the triggered alarm. My first thought had been a Lambda
function triggered by the SNS topic, that would identify the alarm(s) in question, render
a graph of them, and then send that in a HTML email via SES. But that seemed like much more
work than I was interested in; all I _really_ needed to make this workable was a way to quickly
view alarms, metrics and events in CloudWatch.

## Solution

_Disclaimer: This is a bit of a kludge. It was designed for a tiny personal account with one human user, no monitoring other than CloudWatch, and for minimal cost._

For integration with non-SAML identity providers ("custom federation brokers"), AWS IAM
provides a way to
[create a URL that enables federated users to access the AWS Console](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html).
In short, an IAM user with the required permissions can call [AssumeRole](http://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
to generate temporary credentials for a specified IAM Role, and then pass those credentials in
a HTTP request to ``https://signin.aws.amazon.com/federation`` and get back a temporary ``SigninToken`` granting
access to the AWS Console with the assumed role. This token can be used to construct a single URL that signs in
to the Console under the assumed role and brings the user to a specified destination URL in the AWS Console.

The one catch to this process (documented on the link above) is the user that makes the ``AssumeRole`` API call must have
long-term credentials (i.e. a real IAM User). The call to the ``/federation`` endpoint will fail if ``AssumeRole`` was called
by another assumed role's temporary credentials, such as a Lambda function or Instance Profile. That tripped me up at first,
but I ended up figuring out a workable solution.

1. Create a new IAM Role for read-only cloudwatch access and attach the AWS-managed CloudWatch Read Only
  policy to it (``arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess``). This is the role that our pre-authorized
  (federated) console login will use.
2. Create a new IAM User that we'll use to make the AssumeRole call from our Lambda function. This user should have
  a policy with only _one_ permission: calling ``sts:AssumeRole`` on the IAM Role we created in the previous step.
3. Deploy our Lambda function, and pass the Access Key ID and Secret Access Key to it as environment variables.
  This is terrifyingly insecure (see note below), but little risk read-only credentials and an account that
  only has one other user.
4. Add code to our Lambda function to call AssumeRole for the cloudwatch read-only role, and then create the
  [federated login URL](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html)
  for the Console. For this part, I found a really helpful
  [gist with the Python/boto3 implementation already done](https://gist.github.com/weavenet/d21b288327bcc4947e690be13e19c79c).
  For the ``Destination`` parameter on the signin URL, I specified the full URL to the relevant
  CloudWatch Dashboard with my metrics.
5. Embed this URL in your SNS notification text. Most email clients should auto-link the URL, so you'll end up with an email
  notification that's still plaintext, but includes a clickable link for a read-only CloudWatch view with no
  additional authentication required. This provides a much quicker "ok, what does this problem look like?" workflow.

_Longer note on security:_ This isn't terribly secure. I wouldn't implement anything like this at my day job.
But I'm the only user that has access to both my AWS account and my email. If someone gets access to my email,
the fact that they can also view my CloudWatch metrics is likely the least of my worries. Similarly, putting
actual IAM User credentials in Lambda environment variables is horribly, painfully, terrifyingly insecure. But
the credentials are read-only and only for CloudWatch, and in order to them, someone would need to have access
to one of _my_ Users in the account, all of which are much more privileged. So, I decided that it's an acceptably
small risk. I also wouldn't be handing out pre-signed URLs, even with a very limited read-only role, in a
multi-user context. But once again, for a single-user low-value account, it's a workable solution.

_Short note on cost:_ If I were setting up even a similarly minuscule infrastructure for any organization that
relied on it, I'd certainly invest in real monitoring solutions. [Datadog's pricing](https://www.datadoghq.com/pricing/)
isn't bad at all, with a $15 USD per month per host plan (their free plan has 1-day data retention, so it's
really just a demo) and [PagerDuty starts at](https://www.pagerduty.com/pricing/) $9 USD/user/month. But the
combination of those two is more than my entire monthly infrastructure bill right now, so... not really worth it for me.

## Next Steps

If I get around to it, I'd like to stop sending email and SNS notifications directly from CloudWatch alarms,
and instead pass them through a Lambda function first. This would provide a means to include the pre-authorized
Dashboard URL described above, as well as some additional context (such as the last N metrics for the alarm
and the alarm history).

Ideally, though this is quite a bit more work, I'd figure out a simple way of rendering a graph of the
CloudWatch metric in question, and move email notifications from SNS to SES, sending HTML emails with
a bit more detail and some useful graphs. Another option would be to continue with SNS, but (assuming I
consider my email to be relatively secure and my notifications to be not-too-sensitive, both of which are
true) generate graphs and decently-useful HTML pages for each alert, upload them (at pseudo-random paths,
for some level of security from casual onlookers) to a public S3 bucket with website access enabled,
and include _that_ URL in the SNS notification.
