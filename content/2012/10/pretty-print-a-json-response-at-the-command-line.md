Title: Pretty-Print a JSON response at the command line
Date: 2012-10-09 14:44
Author: admin
Category: Tech HowTos
Tags: curl, json, python, rabbitmq
Slug: pretty-print-a-json-response-at-the-command-line

I've been doing some work with [RabbitMQ](http://www.rabbitmq.com/)
lately, and have been doing some testing against its HTTP-based API,
which returns results in JSON. If you're looking to pretty-print a JSON
response for easier viewing, here's a nice way to do it at the command
line using Python and
[json.tool](http://docs.python.org/library/json.html):  

` curl http://username:pass@hostname:55672/api/overview | python -m json.tool`{lang="bash"}
