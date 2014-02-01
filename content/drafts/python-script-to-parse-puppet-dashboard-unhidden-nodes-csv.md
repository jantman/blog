Title: Python Script to Parse Puppet Dashboard unhidden-nodes.csv and report nodes last run before a given time
Date: 2013-06-26 10:09
Author: admin
Category: Puppet
Tags: csv, dashboard, dateutil, node, puppet, python
Slug: python-script-to-parse-puppet-dashboard-unhidden-nodes-csv
Status: draft

Puppet Dashboard is OK, but the sort by latest report feature seems
broken for me. It can, however, output a CSV file of any list of nodes
(all nodes, by group, by class, by search string, etc.). Here's a quick
little python script that parses that CSV (feel free to reuse that logic
if you want) and outputs a list of nodes sorted by latest report,
optionally only the ones with a latest report before a given time. The
latest version of the script lives at:
[https://github.com/jantman/misc-scripts/blob/master/find\_outdated\_puppets.py](https://github.com/jantman/misc-scripts/blob/master/find_outdated_puppets.py)

~~~~ {lang="python"}
~~~~
