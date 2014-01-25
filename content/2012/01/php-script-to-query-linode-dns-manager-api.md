Title: PHP Script to Query Linode DNS Manager API
Date: 2012-01-20 22:49
Author: admin
Category: Tech HowTos
Tags: api, dns, linode, PHP, sysadmin
Slug: php-script-to-query-linode-dns-manager-api

I'm in the process of moving all of my public-facing services, currently
hosted on a single
[Linode](http://www.linode.com/?r=5c8ad2931b410b55455aadbcf0a8d86d6f698a91),
to a new virtual machine (still with Linode, of course, just a new
CentOS 6 VM). Of course, I've got a *lot* (about 60) of DNS records,
spread across 8 domains, that point at the old machine. For name-based
vhosts in Apache, my usual procedure is to migrate everything over to
the new host and then change DNS, and once the change propagates (I'm
using Linode's DNS hosting, so it makes things a LOT easier but I don't
have `rndc reload` anymore) I test in a browser and, assuming all is
well, disable the vhost on the old server. To do all this, I need an
easy way to get a list of all the DNS records that still point to the
old machine.

Luckily, to augment their web-based control panel (Linode Manager),
Linode has a pretty full-featured [API](http://www.linode.com/api/) with
bindings for Python, Perl, PHP, Ruby, Java and others. While I like
Python and I'm starting to learn Perl (by trying to shift most of my
non-time-sensitive scripting to it) for my new job, PHP is still my
strongest language (and the majority of my existing administrative
scripting is written in it, especially handy when it comes time to add a
web front-end to things). So I wrote the following script to query
Linode's [DNS Manager API](http://www.linode.com/api/dns) using [Kerem
Durmus' Linode API PHP wrapper](https://github.com/krmdrms/linode/)
(installation instructions and info at that Github link). The script
simply writes all Linode DNS records for all zones to a CSV file (this
could take a while if you have a lot of records...).

~~~~{.php}
, many thanks to him for releasing this.
   *
   * INSTALLATION (as per krmdrms README):
   *  pear install Net_URL2-0.3.1
   *  pear install HTTP_Request2-0.5.2
   *  pear channel-discover pear.keremdurmus.com
   *  pear install krmdrms/Services_Linode
   *
   * Also requires php-openssl / php5-openssl
   *
   * USAGE: php linodeDnsToCsv.php
   *
   * Copyright 2011 Jason Antman  , all rights reserved.
   * This script is free for use by anyone anywhere, provided that you comply with the following terms:
   * 1) Keep this notice and copyright statement intact.
   * 2) Send any substantial changes, improvements or bog fixes back to me at the above address.
   * 3) If you include this in a product or redistribute it, you notify me, and include my name in the credits or changelog.
   *
   * The following URL always points to the newest version of this script. If you obtained it from another source, you should
   * check here:
   * $HeadURL: http://svn.jasonantman.com/misc-scripts/linodeDnsToCsv.php $
   * $LastChangedRevision: 25 $
   *
   * CHANGELOG:
   * 2011-12-17 Jason Antman :
   *    merged into my svn repo
   * 2011-09-12 Jason Antman :
   *    initial version of script
   *
   */

require_once("/var/www/linode_apikey.php"); // PHP file containing:   define("API_KEY_LINODE", "myApiKeyHere");
require_once('Services/Linode.php');

// get list of all domains
$domains = array(); // DOMAINID => domain.tld
try {
  $linode = new Services_Linode(API_KEY_LINODE);
  $result = $linode->domain_list();

  foreach($result['DATA'] as $domain)
    {
      $domains[$domain['DOMAINID']] = $domain["DOMAIN"];
    }
}
catch (Services_Linode_Exception $e)
{
  echo $e->getMessage();
}

$records = array(); // array of resource records
$linode->batching = true;
foreach($domains as $id => $name)
{
  $linode->domain_resource_list(array('DomainID' => $id));
}

try {
  $result = $linode->batchFlush();
  
  foreach($result as $batchPart)
    {
      foreach($batchPart['DATA'] as $rrec)
    {
      if(! isset($records[$rrec['DOMAINID']])){ $records[$rrec['DOMAINID']] = array();}
      $records[$rrec['DOMAINID']][$rrec['RESOURCEID']] = array('name' => $rrec['NAME'], 'type' => $rrec['TYPE'], 'target' => $rrec['TARGET']);
    }
    }
}
catch (Services_Linode_Exception $e)
{
  echo $e->getMessage();
}

echo '"recid","domain","name","type","target"'."\n";
foreach($domains as $id => $name)
{
  foreach($records[$id] as $recid => $arr)
    {
      echo '"'.$recid.'","'.$name.'","'.$arr['name'].'","'.$arr['type'].'","'.$arr['target']."\"\n";
    }
}


?>
~~~~

That will print out a list containing the Linode DNS record id (recid),
domain, record name, type and target:

~~~~{.text}
"recid","domain","name","type","target"
"137423","jasonantman.com","","TXT","v=spf1 mx:jasonantman.com -all"
"3597859","jasonantman.com","","MX","linode1.jasonantman.com"
"3488952","jasonantman.com","","mx","linode2.jasonantman.com"
"3472952","jasonantman.com","blog","CNAME","linode1.jasonantman.com"
~~~~

If you want to, say, search for only records that include host
"example", you could use grep and awk like:

~~~~{.bash}
php linodeDnsToCsv.php | grep linode1 | grep -v '"linode1","a"' | awk -F , '{printf "%-27s %-20s %-7s %s\n", $2, $3, $4, $5}' | sed 's/"//g'
~~~~

I hope this helps someone else out, and saves them a few minutes of
coding...
