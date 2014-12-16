Title: AWS CloudFormation and RDS Snapshots
Date: 2014-12-15 09:29
Author: Jason Antman
Category: Tech HowTos
Tags: aws, cloudformation, rds, mysql, snapshot
Slug: aws-cloudformation-and-rds-snapshots
Summary: Some tips, tricks and non-intuitive information about working with AWS CloudFormation and RDS snapshots.
Status: draft

For the past few weeks, I've been working on spinning up a WordPress stack on Amazon AWS. It's intended to be a production application,
so it uses Multi-AZ and a few other tricks to try to achieve relatively high fault tolerance (nothing insane, still in one region). It uses
AWS's [RDS](https://aws.amazon.com/rds/) hosted MySQL service for the database, and the stacks are created with [CloudFormation](https://aws.amazon.com/cloudformation/).
Using CloudFormation has been an utterly wonderful experience and being able to spin up an entire stack - multiple autoscaling web server
instances, a database, memcache, etc. with the click of a button in ~20 minutes - is as close to operations nirvana as I've ever gotten.

One of the last steps for me was to work on database backups and restoration; both restoring the production application's database to a
previous snapshot, and restoring a production database snapshot to a test or development stack. This took a few days of testing, and I
wasn't able to find much complete information on the nuances of it; there are also some pieces that are not intuitive and (IMO) not
documented well enough in the AWS docs. In short, it's horribly easy to blow away your entire database. So, I'm going to attempt to document
some of what I learned, in the hope that it will benefit others.

At the bottom of this post I've included some snippets from my CloudFormation template, which I make reference to. It's probably worth looking
through that, as I make reference to some of the names used in it. Also, to make sense of this, you should be familiar with the nomenclature used by CloudFormation,
such as the [template anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html) and the difference between
parameters and properties, and resources and instances.

__Note:__ I'm writing this in mid-December 2014. I'll make every effort to keep this updated as I continue working with AWS, but it's possible
that some of the problems described herein will be fixed by AWS in the future.

DeletionPolicy Snapshot
------------------------

CloudFormation resources support a [DeletionPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html)
attribute that says what to do to a resource when deleted. For RDS instances, "Snapshot" is an option, which takes a manual snapshot when the resource
is deleted (manual snapshots, unlike the automated daily ones, live on even after the instance is deleted). Be warned, this only takes effect when you
delete the __entire stack__. If you make a change to one of the [DBInstance properties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html)
that requires a [resource replacement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html#update-replacement) to
take effect, the RDS instance will be replaced with a new one, and all of the data and automatic snapshots from the old one will be deleted.
That last part deserves repeating: automatic snapshots (the daily ones created by RDS) are tied to the instance; if the instance is replaced
by CloudFormation, you lose all automatic (backup) snapshots with it.

Stack Policy to Prevent Updates
--------------------------------

To prevent RDS data loss from accidentally changing a property of the instance, it's wise to add a
[stack policy to prevent updates to RDS resources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html).
This will prevent CloudFormation from making any changes to the RDS instance at all. Once the stack policy
is in place, in order to make changes to the RDS instance you would either need to set a temporary stack policy
to allow the update (see the "Updating Protected Resources" section of the [stack policy documentation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html))
or simply delete and re-create the stack (the recommended method, if it's feasible for you).

Setting a proper stack policy should prevent many of the pitfalls I describe below; however, for completeness,
I've described how RDS resources behave currently without a stack policy protecting them. The
[AWS::RDS::DBInstance resource documentation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html)
describes which properties can be updated in-place ("Update requires: No interruption" or "some interruptions")
and which trigger complete replacement of the RDS instance ("Update requires: replacement").

Restoring Snapshots and DBName
-------------------------------

The DBSnapshotIdentifier property on a MySQL RDS instance specifies a RDS snapshot to restore into the instance. The DBName
property will create a new RDS instance with a single blank database of that name. This bears repeating again; if the DBName
property ever changes, your RDS instance will be replaced with one with a new, blank database of that name.
When creating a MySQL RDS instance, you can specify either the ``DBName`` or ``DBSnapshotIdentifier`` property, but not both;
if you attempt to specify both, you'll get an error, "DBName must be null when Restoring for this Engine."

If you want to restore a snapshot to a new RDS instance, you'll need to ensure that ``DBName`` is null (either not specified at all, or the special ``AWS::NoValue``
[pseudo parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html)). In order
to do this automatically (and since NoValue/null can't be passed in as a template parameter), in the template snippet below I've defined a
``UseDbSnapshot`` [condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html)
that evaluates to true if the ``DBSnapshotIdentifier`` parameter is not empty. In my ``RDS::DBInstance`` resource,
I conditionally set (using [``Fn::If``](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html#d0e42982))
the ``DBSnapshotIdentifier`` and ``DBName`` properties depending on the value of ``UseDbSnapshot``. The end result is that if the
``DBSnapshotIdentifier`` parameter is not empty, it is passed in as the ``DBSnapshotIdentifier`` property of the resource and
the ``DBName`` property is set to ``AWS::NoValue``. Otherwise, the ``DBSnapshotIdentifier`` property is set to ``AWS::NoValue``
and the ``DBName`` parameter is passed in to the corresponding property on the resource (indicating to create a new blank database
of that name).

To explain this a bit more, CloudFormation seems to have no introspection into RDS instances. The ``DBName`` parameter
exists only in CloudFormation itself, and is only evaluated as a diff from the previous template; if it changes,
CloudFormation spins up a completely new RDS instance with a single blank database of that name. Whether or not
the value of ``DBName`` matches the database currently in the RDS instance (say, restored from a snapshot)
is not known by CloudFormation. In short, if you create an RDS instance from a snapshot of a "foo" database
and then change the template to have a ``DBName`` of "foo", CloudFormation will spin up a new RDS instance
with an empty "foo" database.

Restoring to a New Stack
-------------------------

When restoring to a new stack (stack creation), specify the ``DBSnapshotIdentifier`` and make sure ``DBName`` is set
to ``AWS::NoValue`` per the previous paragraph (condition in the template). Note that for the life of the stack, you
must continue specifying these parameters (or the "use previous value" option for them). Using my example template
below, if you restored into a new stack using the ``DBSnapshotIdentifier`` parameter and then later updated the stack
and omitted that parameter (which, because of the condition, would set it to ``NoValue`` and set the ``DBName`` parameter
to its default value) the RDS instance would be replaced with a new one with a blank database.

Because of this, stack updates should always use the previous value for the ``DBSnapshotIdentifier`` parameter; this can
be done through the AWS Console, or using the ``aws`` command line tools and a parameter like: ``--parameters ParameterKey=DBSnapshotIdentifier,UsePreviousValue=true``.

Restoring to an Existing Stack
-------------------------------

Restoring a snapshot to an existing stack is a bit more nuanced. You can't restore a snapshot to an existing RDS instance,
you can only restore to a new instance. If you do this through the AWS Console, you'll end up with an RDS instance disconnected
from your CloudFormation stack. So the way to do this is more or less the same as restoring to a new stack - specify
the ``DBSnapshotIdentifier`` parameter for your template, and it will create a new RDS instance with the snapshot. The same
rules about using previous values for the parameters hold true. If you used a stack policy to prevent updates to the RDS
instance, you'll need to override that with a temporary policy when doing the restore.

There are a few caveats to keep in mind with this procedure. The first, obviously, is that there may be some application downtime
when the existing database is replaced with the new (restored) one, and any writes will obviously be lost. Also, this only
works on RDS instances that were created with DBName or a __different__ snapshot. In order to restore the same snapshot to
an RDS resource a second time, you need to first update with the ``DBSnapshotIdentifier`` parameter removed and have the RDS
instance re-created with an empty database, and then update again with the ``DBSnapshotIdentifier`` in order to do the restore.
This is because CloudFormation doesn't reconcile the current state of instances to determine which actions to take, it only diffs
the updated template against the existing one. If the existing template and the updated one have the same value for the RDS instance's
properties (specifically ``DBSnapshotIdentifier``), CloudFormation determines there are no changes, and does nothing.

LaunchConfig Metadata Issues
-----------------------------

The EC2 instances I'm using for this project are "baked" AMIs (built with [packer.io](https://packer.io/)) in an Auto-Scaling Group (ASG).
They use a [LaunchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html) to write
out a file on disk with the database connection information for the application. In addition, my ASG has an [UpdatePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html)
designed to perform rolling updates (termination and replacement) of EC2 instances when their properties change.

In my testing, I noticed a number of times where updates to the RDS resource that triggered creation of a new RDS instance - such as restoring from
a snapshot in an existing stack, or changing the DBName - properly triggered an update of the LaunchConfig, but failed to trigger
the rolling update of the EC2 instances. This left the application in a state where one or more (sometimes all) of the EC2
instances couldn't connect to the database, because the file written out by the LaunchConfig still contained the old DB connection
information. For non-production stacks where the entire stack can be deleted and recreated instead of updating the RDS resource,
this shouldn't be an issue. Otherwise, if changes are made that replace the RDS instance, I'd recommend watching for the
LaunchConfig update completion, and manually terminating instances (or increasing the size of the ASG to add instances)
to ensure that the running EC2 instances have the updated LaunchConfig.

Another option would be to use the [cfn-hup daemon](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-hup.html) to
listen for stack updates that cause changes in resource metadata, and perform the required actions without needing the rolling update
to replace the instances.

How to Do Things Using the Template Below
------------------------------------------

I'm currently using the ``aws`` command line tools to perform stack creation and updates,
wrapped in a Rakefile (I plan on changing this to use [boto](https://github.com/boto/boto)
inside a [Jenkins](http://jenkins-ci.org/) job). What follows is a quick high-level guide
on how to accomplish various RDS-related tasks, using the template snippet below.

* __Build a new stack, using a RDS snapshot__ -

~~~~{.bash}
$ aws cloudformation create-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,ParameterValue='my-snapshot-identifier'
~~~~

* __Temporarily override stack policy to allow updates__

    1. Create a file with the following contents (we'll assume it's at ``/home/myuser/allow_all_updates.json``):
            ~~~~{.json}
            {
              "Statement" : [
                {
                  "Effect" : "Allow",
                  "Action" : "Update:*",
                  "Principal": "*",
                  "Resource" : "*"
                }
              ]
            }
            ~~~~
    2. In the following ``aws`` commands, append ``--stack-policy-during-update-url file:///home/myuser/allow_all_updates.json``

* __Update a stack (built using a RDS snapshot), without losing data__ -

~~~~{.bash}
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,UsePreviousValue=true
~~~~

* __Load a RDS snapshot into an existing stack__ (that isn't already using this snapshot) -

~~~~{.bash}
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,ParameterValue='my-snapshot-identifier'
~~~~

* __Load a RDS snapshot into an existing stack again__ - (i.e. restore from the same snapshot a second time; this one is a kludge)

~~~~{.bash}
$ # re-create the RDS instance with a blank DB (DBName)
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,ParameterValue=''
$ # then load the snapshot again
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,ParameterValue='my-snapshot-identifier'
~~~~

CloudFormation Template Snippet
--------------------------------

This is by no means complete, but just includes the parameters, conditions, and resources which I make reference to.

~~~~{.json}
{
  "Parameters" : {
    "DBName" : {
      "Default": "wordpress",
      "Description" : "The WordPress database name",
      "Type": "String",
      "MinLength": "1",
      "MaxLength": "64",
      "AllowedPattern" : "[a-zA-Z][a-zA-Z0-9]*",
      "ConstraintDescription" : "must begin with a letter and contain only alphanumeric characters."
    },
    "DBSnapshotIdentifier" : {
      "Description" : " The RDS MySQL snapshot name to restore to the new DB instance.",
      "Type": "String",
      "Default": ""
    },
  },

  "Conditions" : {
    "UseDbSnapshot" : {
      "Fn::Not" : [{
        "Fn::Equals" : [
          {"Ref" : "DBSnapshotIdentifier"},
          ""
        ]
      }]
    }
  },

  "Resources" : {
    "DBInstance" : {
      "Type": "AWS::RDS::DBInstance",
      "Properties": {
        "DBName"            : {
          "Fn::If" : [
            "UseDbSnapshot",
            { "Ref" : "AWS::NoValue"},
            { "Ref" : "DBName" }
          ]
        },
        "Engine"            : "MySQL",
        "MasterUsername"    : { "Ref" : "DBUsername" },
        "DBInstanceClass"   : { "Ref" : "DBClass" },
        "DBSecurityGroups"  : [{ "Ref" : "DBSecurityGroup" }],
        "DBSubnetGroupName": { "Ref": "DBSubnetGroup" },
        "AllocatedStorage"  : { "Ref" : "DBAllocatedStorage" },
        "MasterUserPassword" : { "Ref" : "DBPassword" },
        "DBSnapshotIdentifier" : {
          "Fn::If" : [
            "UseDbSnapshot",
            { "Ref" : "DBSnapshotIdentifier" },
            { "Ref" : "AWS::NoValue"}
          ]
        },
        "MultiAZ" : true
      },
      "DeletionPolicy" : "Snapshot"
    },
    "WebServerGroup" : {
      "Type" : "AWS::AutoScaling::AutoScalingGroup",
      "Properties" : {
        "LaunchConfigurationName" : { "Ref" : "LaunchConfig" },
      },
      "UpdatePolicy": {
        "AutoScalingRollingUpdate" : {
          "MinInstancesInService" : "1",
          "MaxBatchSize" : "1",
          "WaitOnResourceSignals" : "true",
          "PauseTime" : "PT10M"
        },
        "AutoScalingScheduledAction" : {
          "IgnoreUnmodifiedGroupSizeProperties" : true
        }
      },
      "CreationPolicy" : {
        "ResourceSignal" : {
          "Timeout" : "PT10M",
          "Count" : "2"
        }
      }
    },
    "LaunchConfig": {
      "Type" : "AWS::AutoScaling::LaunchConfiguration",
      "Metadata" : {
        "AWS::CloudFormation::Init" : {
          "config" : {
            "files" : {
              "/opt/wordpress/cloudformation_db.php" : {
                "content" : { "Fn::Join" : ["", [
                  "<?php\n",
                  "define('DB_NAME',          '", {"Ref" : "DBName"}, "');\n",
                  "define('DB_USER',          '", {"Ref" : "DBUsername"}, "');\n",
                  "define('DB_PASSWORD',      '", {"Ref" : "DBPassword" }, "');\n",
                  "define('DB_HOST',          '", {"Fn::GetAtt" : ["DBInstance", "Endpoint.Address"]},"');\n",
                ]] },
              }
            }
          }
        }
      }
    }
  }
}
~~~~
