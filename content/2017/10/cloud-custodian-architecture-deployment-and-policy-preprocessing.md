Title: Cloud Custodian Architecture, Deployment and Policy Preprocessing
Date: 2017-10-24 16:49
Modified: 2017-10-24 16:49
Author: Jason Antman
Category: Tech HowTos
Tags: aws, cloud-custodian, cloud custodian, c7n, lambda, sqs, splunk
Slug: cloud-custodian-architecture-deployment-and-policy-preprocessing
Summary: Details of how I setup Capital One's Cloud Custodain at work, including our monitoring, logging and policy preprocessing.

[TOC]

_This post was originally published to my company's internal blog platform; I'm publishing it here for the
larger Cloud Custodian user community, but unfortunately I haven't gotten (or sought) approval to publish
any of our internal code referenced herein._

At work I've spent quite a bit of time over the past few weeks working on our deployment of Capital One's
[cloud custodian](https://github.com/capitalone/cloud-custodian) (a.k.a. [c7n](https://pypi.python.org/pypi/c7n))
for rules and policy enforcement in our AWS accounts, both to replace our aged
[Netflix Janitor Monkey](https://github.com/Netflix/SimianArmy/wiki/Janitor-Home)
installation and to enable us to expand the cleanup rules we execute and begin
enforcing more granular policies. While we've only been running c7n for a few months
(and most of that time in a test only/dry run mode), we've already accumulated
29 different policies (mostly Janitor Monkey replacements for tag enforcement and low utilization instance termination)
and are adding new ones rather quickly. Based on interest from colleagues I'd like
to explain a bit about how we manage and deploy Cloud Custodian, and specifically
about how we preprocess our policies to generate the ``custodian.yml`` configuration.

## Overall Architecture

We currently run all of our Cloud Custodian policies as Lambda functions, taking
advantage of c7n's excellent [Lambda support](http://www.capitalone.io/cloud-custodian/docs/policy/lambda.html).
Each policy currently runs on a schedule (based on CloudWatch Events); we've experimented
with running policies based on Config rules, Instance state changes and CloudTrail Events,
but most of those executed too quickly to prove useful for our needs (specifically tag enforcement
policies, as many of our development teams use tooling that defers tagging until significantly
after resource creation). In addition to the main Lambda functions that execute the policies,
we run a number of other ancillary tools related to Cloud Custodian:

1. We use the [Custodian Mailer (c7n-mailer)](https://github.com/capitalone/cloud-custodian/tree/master/tools/c7n_mailer)
  tool for email notifications, coupled with a customized
  [email template](https://gist.github.com/jantman/44eede9654dbb64e1d2abaa62ebbc0f3#file-redefault-html-j2) based on the [example](https://github.com/capitalone/cloud-custodian/blob/master/tools/c7n_mailer/msg-templates/default.html.j2)
  for visually appealing and useful notifications across email clients (like the example below). This also runs as a Lambda
  function, and processes notification events that c7n policies push onto an SQS queue.
  ![screenshot of c7n notification email template](/GFX/custodian-email-example.png)
2. We use Splunk as our (new) central logging solution and run a custom Lambda function, ``sqs_splunk_lambda``,
  forked from ``c7n-mailer`` but modified to send cloud-custodian policy run results to Splunk Cloud instead of email.
  Cloud Custodian's [notify action](http://www.capitalone.io/cloud-custodian/docs/generated/c7n.html#c7n.actions.Notify),
  which is used to trigger ``c7n-mailer``, works by pushing some JSON data to an SQS queue; this data includes the full
  details of the policy itself, the resources that the policy matched, and why (what filter(s)) each resource was matched.
  Our policy preprocessor (see below) adds a notify action to _every_ policy that sends to a specific, separate SQS queue
  for the Splunk function. The Lambda function processes this queue every five minutes, removes some repetitive and
  less-important data (to get the message size below 10KB), and then sends the JSON message on to Splunk. This places
  the full data from every policy execution in Splunk, and allows us to search
  Splunk for high-level queries like "every EC2 Instance that c7n stopped", "every resource matched by a specific policy",
  or "every action that a specific policy has taken".
3. Asynchronous Lambda function executions - such as those triggered by CloudWatch Events - are automatically retried up
  to three times if the invocation fails. However, there's no easy way to tell if all tries of a particular function
  invocation failed. ``errorscan.py``
  is our solution to this problem. We configure all of our Cloud Custodian policy Lambda functions with a Dead Letter Queue,
  a feature of Lambda that pushes a message to a SQS queue if all retries of an invocation failed. ``errorscan.py`` runs
  once a day via Jenkins and checks for messages in a single shared Dead Letter Queue (DLQ). If there are any, it uses CloudWatch
  Logs to associate the queue entry with the Lambda function that failed, and outputs the logs from the failed invocation(s).
  The ``errorscan.py`` script also examines the Failed and Throttled Invocations metrics in CloudWatch for each function.
  If there were any entries in the DLQ or failed/throttled invocations metrics beyond a specified threshold, the job will
  report that information and then fail, triggering a low urgency notification to our on-call engineer.
4. We store our policies in git, one file per policy, with common default values removed. Our ``policygen.py`` script,
  explained in detail below, reads the policy files, interpolates our defaults, performs some sanity checking,
  and then generates the single ``custodian.yml`` file actually used by c7n.

## Test and Deployment

We test and deploy our Cloud Custodian infrastructure using a Jenkinsfile.
For simplicity of dependencies, most of the stages utilize the Jenkins [Docker Workflow](https://plugins.jenkins.io/docker-workflow)
plugin and run inside the public [python:2-wheezy](https://hub.docker.com/_/python/) image and the jobs that manage the
infrastructure dependencies run inside the public [hashicorp/terraform](https://hub.docker.com/r/hashicorp/terraform/) image.
Most of the actual custodian commands are run from a ``Makefile``, which makes it
easier to run the same commands from either the Jenkins pipeline or a local development environment.

We follow a pull request GitHub workflow, and only allow merges to the master branch from PRs that have been successfully
built by Jenkins. Our pipeline differentiates between builds of the master branch (which triggers deployment) and builds
of PRs or other branches (which are test/dry run only).

The steps in the pipeline are as follows:

1. __Terraform__ - run a ``terraform apply`` for master, or a ``terraform plan`` for non-master. This uses terraform to manage the
  required infrastructure for c7n,
  namely the CloudWatch Log Group for the c7n lambda functions, the s3 bucket for the c7n output, the IAM Role that the
  c7n functions execute with, and the SQS queues for the mailer, splunk log shipper, and the dead letter queue.
2. __virtualenv__ - Setup a new Python virtualenv in the Docker container for the following steps, and copy the current directory
  (git clone / Jenkins workspace) to ``/app`` in the container. We do the latter because Jenkins runs as a normal user
  but the public Python docker container prefers to run as root (0:0). To prevent problems, we copy the Jenkins workspace
  to ``/app`` in the container, run what we need to, and then copy any desired output back to the workspace and ``chown``
  it to Jenkins' user and group when finished.
3. __tox__ - Install [tox](https://tox.readthedocs.io/en/latest/) in the virtualenv; we use this to run pytest unit tests for
  our custom code in subsequent steps.
4. __policygen tests__ - Run unit tests for our ``policygen.py`` script.
5. __sqs_splunk_lambda tests__ - Run unit tests for our ``sqs_splunk_lambda`` Splunk log shipper code.
6. __Validate__ - Install dependencies for c7n, generate our ``custodian.yml`` file using ``policygen.py``, and then
  run ``custodian validate`` on the resulting file. This step also generates the ``policies.rst`` file containing a
  table of our current policy names and comments/descriptions (which we include in our internal Sphinx-built documentation),
  and copies both ``custodian.yml`` and ``policies.rst`` back to the Jenkins workspace for archiving in the job history.
7. __mugc dry run__ - Cloud Custodian deploys its Lambda functions via a reusable Lambda management library,
  [c7n.mu](https://github.com/capitalone/cloud-custodian/blob/master/c7n/mu.py), and we use its garbage collection
  tool, [mugc.py](https://github.com/capitalone/cloud-custodian/blob/master/tools/ops/mugc.py), to clean up the
  Lambda functions and CloudWatch Events for policies we've deleted. In this step, we do a dry run of the garbage
  collection script.
8. __custodian dry run__ - This performs a ``custodian`` dry run as a final check for our policies, copies the
  dry-run results/output back to the Jenkins workspace, and archives it in the job history.
9. __Run__ - For builds of the master branch, we do the actual ``mugc.py`` garbage collection of old Lambdas/Events,
  do the actual ``custodian`` run to provision our c7n Lambda functions, and provision the ``c7n_mailer`` Lambda function.
  For non-master branches, we only install the mailer's dependencies (sanity check) and print our mailer config file
  to STDOUT.
10. __sqs_splunk_lambda__ - For builds of master, we install our ``sqs_splunk_lambda`` code and provision its
  Lambda function. For builds other than master, we run ``sqs_splunk_lambda --validate`` to validate its configuration
  file. This step is run in a ``VaultBuildWrapper``, as it securely retrieves Splunk credentials from our
  [HashiCorp Vault](https://www.vaultproject.io/) instance.
11. __Build Docs__ - We run a Sphinx build of our documentation, which is mostly static content but also includes the
  generated list of our policies from step 6.
12. __Publish Docs__ - For builds of master, we push the HTML documentation built in the last step to the ``gh-pages`` branch
  for serving via GitHub Pages.
13. __Job DSL for Monitoring Job__ - For builds of master, we run
  [Job DSL](https://jenkinsci.github.io/job-dsl-plugin/) to create or update a persistent Jenkins job
  (outside the pipeline) that runs ``errorscan.py`` once a day and notifies us if any Lambda function errors were found.

We also have shell scripts provided for testing changes and doing dry runs locally, which use the same Docker images and Makefile as the Jenkins-based build.

## Policy Preprocessing

Our ``policygen.py`` script is responsible for reading in the directory of per-policy YAML files,
performing some sanity checks on them, interpolating defaults from a ``policies/defaults.yml`` file,
and then writing out the single ``custodian.yml`` that Cloud Custodian actually runs. The overall program flow is as follows:

1. Read in all ``.yml`` files from the ``policies/`` directory; build a dict of policy names to the policy contents, deserialized from YAML into native Python data structures. For each policy file, ensure that the filename without the extension (i.e. the basename) matches the value of the "name" key in the policy YAML; raise an exception if any policies do not have a filename that matches their policy name.
2. Remove the ``defaults`` policy from that dict, and store it separately for later use.
3. Iterate over all policies in the dict, lexicographically by policy name; for each of them, interpolate our defaults into the policy and append the result to a "policies" list. See below for details of the defaults interpolation process.
4. Generate "cleanup" policies and append them to the list. This step is a holdover from before cloud-custodian had the [mugc Lambda cleanup tool](https://github.com/capitalone/cloud-custodian/blob/master/tools/ops/mugc.py) but we still use it; this uses the names of all current policies to generate two policies that identify Lambda functions and CloudWatch Event Targets, respectively, that were provisioned by Cloud Custodian for policies that no longer exist. The resulting policies run once per day, and email us if there are any "orphaned" Cloud Custodian functions or rules.
5. Run a series of sanity and safety checks on the generated policies (see "Policy Sanity Checks", below, for more information).
6. Write the final ``custodian.yml`` that will be used by Cloud Custodian, containing all of our final policies.
7. Write a ``policies.rst`` file that will be incorporated into our Sphinx-generated HTML documentation site. This file contains a table with one row per policy for all of our policies; the first column is the policy name as a HTML link to the policy ``.yml`` file in the git repository, and the second column is the text of the policy's ``comment`` or ``comments`` field.

### Interpolating Defaults into Policies

The most important part of ``policygen.py`` is the interpolation of defaults into policies.
When we originally deployed Cloud Custodian in our test environment, we noticed that our
policies had two large blocks that were almost identical across all policies: the ``mode``
configuration telling Cloud Custodian to deploy the policies as Lambda functions triggered
by periodic CloudWatch Events rules, and the notification action that we use for email
notifications. This was the genesis of ``policygen.py``; we moved these common policy
sections to a ``defaults.yml`` file, and wrote ``policygen.py`` to perform intelligent
merging of the defaults with each policy file, allowing us to override defaults in the
individual policies but still keep some mandatory settings.

Our ``defaults.yml`` file currently looks like this:

```yaml
# IMPORTANT NOTE: **ALL** policies will have an additional notification action.
# See README.md and policygen.py `SPLUNK_SQS` for further info and config.
mode:
  type: periodic
  # This will trigger our rules at 15:20 UTC (11:20 EDT / 10:20 EST)
  # it might be better to spread them out over time a bit, but right now our
  # main concern is ensuring that policies run during work hours.
  schedule: 'cron(20 15 * * ? *)'
  timeout: 300
  execution-options:
    log_group: /cloud-custodian/123456789012/us-east-1
    output_dir: 's3://SOME-BUCKET-NAME/logs'
  dead_letter_config:
    TargetArn: arn:aws:sqs:us-east-1:123456789012:cloud-custodian-123456789012-deadletter
  role: arn:aws:iam::123456789012:role/cloud-custodian-123456789012
  tags:
    Project: cloud-custodian
    Environment: dev
    OwnerEmail: us@example.com
actions:
  - type: notify
    questions_email: us@example.com
    questions_slack: ourChannelName
    template: redefault.html
    to:
      - resource-owner
      - us@example.com
      - awsusers@example.com
    transport:
      type: sqs
      queue: 'https://sqs.us-east-1.amazonaws.com/123456789012/cloud-custodian-123456789012'
```

This provides us with our default execution mode (Lambda function triggered once a day
at a defined time via CloudWatch Events) and its configuration options (mainly, the
IAM Role used for execution, the Dead Letter Queue, CloudWatch Log Group, and S3 output
configuration for policy results), as well as our default email notification configuration
using SQS to c7n-mailer.

All of these options can be overridden in individual policies intelligently; a simple example
policy that emails us about any VPC Peering Connections in a state other than
"active" would look like:

```yaml
# REMINDER: defaults.yml will be merged in to this. See the README.
name: inactive-vpc-peers
comment: Notify RE of any VPC Peering Connections not in Active state (i.e. pending-acceptance, failed, etc.)
resource: peering-connection
filters:
  # Peering Connection not in "active" state
  - type: value
    key: Status.Code
    op: ne
    value: "active"
actions:
  - type: notify
    violation_desc: The following VPC Peering Connections are in a state other than "active"
    action_desc: likely need to be accepted, deleted, or investigated.
    subject: '[cloud-custodian {{ account }}] VPC Peering Connections not in Active state {{ region }}'
    to:
      - us@example.com
```

This policy automatically inherits all of the ``mode`` defaults configuration and the ``notify``
action is merged with the defaults; the resulting generated policy will combine all of the keys
in the defaults notification action and the policy notification action, with the exception of the
``to`` block where the defaults are overridden by the policy.

The actual process of merging the policy and defaults is a recursive deep merge of the dicts, merging
the individual policy over a copy of the defaults, with special logic for lists and
``type: notify`` actions. Overall, the procedure is:

- We start with ``defaults.yml`` as a base, and layer the policy-specific config on top of it.
- We merge recursively (i.e. deep merging).
- Keys from the policy overwrite identical keys in the defaults; the policy-specific config always wins over the defaults.
- In the case of lists (i.e. the ``actions`` list), the end result includes all elements that are simple data types (i.e. strings). For
  dict items in lists, we look at the value of the ``type`` element; if both the policy and the defaults lists have
  dicts with the same ``type``, we merge them together, with the policy overwriting the defaults. Defaults dicts without a
  matching ``type`` in the policy will always be in the final result, **except for** ``actions`` with a type of ``notify``; policies that do
  not have a ``type: notify`` action will not have one added. This allows us to set defaults for dicts embedded in lists, like the
  ``type: notify`` action.
- When finished merging, add a notification action to every policy that pushes to the Splunk queue, which is handled by our
  sqs\_splunk\_lambda code.

To merge the two dicts together, we begin with a copy of the defaults and then iterate over all of the items in the policy as key/value pairs, updating the defaults as we go to build the final policy:

  - If the key from the policy-specific config isn't in the defaults, we add the key and value and move on. Otherwise;
  - If the value is a list, we use special list merging logic (see below) and update with the result of the list merge.
  - If the value is another dict, we call the same function recursively and update with its result.
  - If the value isn't a list or dict, we assume it to be a simple type (string, int, etc.) and overwrite the default value with the one specified in the policy-specific configuration.
  - The end result of this is returned.

List merging is somewhat special, to let us set defaults for actions:

- We begin with the policy itself as the base list, instead of the defaults.
- Any non-dict items in defaults that aren't in the policy are appended to the policy list.
- Any dict items in the policy list with a ``type`` key/value pair that matches one of the dict items in the defaults list, will have additional key/value pairs added from the defaults dict.
- Any defaults dicts not handled under the previous condition will be appended to the result, with the exception of a ``type: notify`` dict in the ``['actions']`` path.

### Policy Sanity Checks

Before writing out the final ``custodian.yml`` configuration, each policy is run through a sanity/safety checking
function. The function is written to be easily extendable to add new policy checks (written in Python), but currently
only has a single check to ensure that any ``marked-for-op`` filters come first in the filter list. When we originally
deployed Cloud Custodian, one of our policies had a ``marked-for-op`` filter (which allows Cloud Custodian to take action
on a resource that was specifically tagged for delayed action in the future) accidentally nested under an ``or`` clause
in the policy YAML (which was unfortunately easy to do, as it only required accidentally indenting the block two extra
spaces). This resulted in the policy taking action immediately instead of a week later, which could have been catastrophic
(luckily the action in this case was benign). To prevent this from happening again, our checks ensure that ``marked-for-op``
filters, if present, always come at the beginning of the list of filters.

## Conclusion

We're still in the process of expanding our Cloud Custodian deployment; right now we're only running
it in one region of one non-production account, but that one region contains the vast majority of our infrastructure.
We'll be expanding to other regions and then production accounts in the next few weeks, and that will require changing
some portions of our configuration, management, and policy generation code to compensate. So far we've seen good results
with using Cloud Custodian to enforce tagging and cost-reduction rules, such as terminating instances that have been
idle for a long time. We hope to continue extending the role that Cloud Custodian plays in cost reduction, and also
expand into enforcing more security and "housekeeping" policies.
