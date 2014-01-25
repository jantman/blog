Title: Thunderbird SSL "Domain Name Mismatch"
Date: 2010-02-12 09:34
Author: admin
Category: Tech HowTos
Tags: certificates, dns, Mozilla, SSL, Thunderbird
Slug: thunderbird-ssl-domain-name-mismatch

Some of my servers that are only for internal/personal use have SSL
certs with a mismatched hostname. The cert for my mail server is issued
for the CNAME used for my mail server, not the actual hostname. Of
course, this means that Thunderbird gives me some annoying errors
because they're worried:

![Domain Name Mismatch in Thunderbird](/GFX/Domain_Name_Mismatch.png)

Luckily, there's an
[add-on](https://addons.mozilla.org/en-US/thunderbird/addon/2131) called
"Remember Mismatched Domains" that adds a simple "remember this
decision" check box, much like the one now found in Firefox. Problem
solved!

![Thunderbird Domain Name Mismatch after
add-on](/GFX/Domain_Name_Mismatch2.png)
