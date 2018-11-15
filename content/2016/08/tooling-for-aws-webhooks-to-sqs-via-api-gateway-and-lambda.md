Title: Tooling for AWS - webhooks to SQS via API Gateway and Lambda
Date: 2016-08-06 21:38
Author: Jason Antman
Category: AWS
Tags: aws, webhook, lambda, github, api-gateway, sqs, queue, python, terraform
Slug: tooling-for-aws-webhooks-to-sqs-via-api-gateway-and-lambda
Summary: Project I created that uses Python and Terraform to setup an AWS API Gateway instance to receive webhooks, and enqueue their content in SQS queues via Lambda.

A few weeks ago at work, I was party to two discussions about possible tooling needs, both very low-priority. One was the possible need to sync MarkDown documentation
from GitHub repositories to... another thing that can hold docs. The other was relating to the new Version 2 Docker Registry, [distribution](https://github.com/docker/distribution).
We have some Jenkins jobs that dynamically populate dropdown fields for build parameters with Docker image names and tags, using the [Active Choices Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Active+Choices+Plugin).
Right now we're directly querying the Docker Registry API from Groovy, every time the Build With Parameters page is loaded. With the original version 1 Docker Registry,
images were often missing from the results (eek!) but the performance was good. With the switch to the v2 Registry, it takes almost two minutes to load the page.
While brainstorming solutions, we decided that caching the list of images and tags in the Registry was the solution. For bonus points, it would also be nice to
be able to query based on image labels - something that's not exposed in the Registry API at all. Luckily, the Registry has an option to fire a webhook every time
a new image is pushed.

Both of these problems have solutions that involve webhooks, from GitHub and Docker Distribution, respectively. They also both involve doing time-consuming things in custom code with the
data in those hooks - transforming MarkDown to another markup and pushing the result to an on-premesis system in the case of GitHub, and ``pull``ing and inspecting Docker
images in the case of the Registry. As such, the "typical" webhook things like [Zapier](https://zapier.com/) won't fit the bill. All I really needed was something to receive webhooks
and push the content of them into a queue. Ideally, it would also be something that would utilize existing services we have, namely AWS.

After working a bunch of nights and the good part of a weekend, I have a solution: my new [webhook2lambda2sqs](https://pypi.python.org/pypi/webhook2lambda2sqs) Python package.

This implements what I think is the cheapest and lowest-overhead solution for anyone with an existing AWS account:

* Setup an [API Gateway](https://aws.amazon.com/api-gateway/) that receives json POST and GET requests.
* It passes them to a [Lambda Function](https://aws.amazon.com/lambda/) which pushes the content to one or more [SQS](https://aws.amazon.com/sqs/) queues, for consumption by an application.

The tooling is written in Python, but leverages [HashiCorp's Terraform](https://www.terraform.io/) to actually manage the AWS resources.

From a JSON configuration file as simple as:

```
{
  "endpoints": {
    "some_resource_name": {
      "method": "POST",
      "queues": ["myqueue"]
    },
  },
}
```

and a single command (``webhook2lambda2sqs genapply``), you'll have the complete system up and running, receiving HTTP POST requests
at an AWS-generated URL and pushing them into the ``myqueue`` SQS queue. Best of all, going by my testing (this is based on the time
the Lambda function takes to run, which can vary quite a bit), the whole thing is __free for the first 1 million requests per month__
if your account is still on the Free Tier, and otherwise is less than $4/month for the first million requests.

The configuration can handle setting up multiple distinct endpoint paths in the same API Gateway, each
sending the data to one or more SQS queues. It also has options for enabling logging (to CloudWatch Logs) both in the function
and on the API Gateway, pushing API Gateway metrics to CloudWatch, and configuring rate limiting.

The ``webhook2lambda2sqs`` program generates the Python code for the lambda function and packages it correctly for Lambda, and
then generates a Terraform configuration to manage all required AWS resources. Separate commands are available that wrap Terraform
(mainly to deal with some issues with its API Gateway implementation) to run ``plan``, ``apply`` and ``destroy``. There are
also helper commands to view the Lambda Function and API Gateway logs from CloudWatch, view messages in the queue(s) and
GET or POST a test message to one or all of the endpoints.

Full documentation is available at [http://webhook2lambda2sqs.readthedocs.io/en/latest/](http://webhook2lambda2sqs.readthedocs.io/en/latest/)
and the package (Python 2.7, 3.3-3.5) can be downloaded [from PyPI](https://pypi.python.org/pypi/webhook2lambda2sqs).
