Title: Relational / Object-Oriented Asset Management
Date: 2007-02-21 16:27
Author: admin
Category: Ideas and Rants
Tags: asset management, asset tracking, IT, object-oriented, relational
Slug: relational-object-oriented-asset-management

I just purchased four new servers, and set out to find some good asset
management software. Specifically, I'm looking for a PHP package that
allows me to track the details of all of my hardware. While software and
configuration tracking would surely be good for some applications, I
already have a package to handle that.

I searched a few popular sites, including SourceForge, and came up with
a dozen or so possibilities that looked good. They varied in level of
detail and features, but all had one common failure - they lack an
object-oriented or relational approach. What do I mean by that? Most of
them are designed so that you enter data in a form, it goes into a
database, and exists just as a table of data. Devices, networks, etc.
exist independently.

What do I want? An object-oriented approach that can handle
relationships between objects, and hierarchies. Lets design a few
objects as examples: We'll have Networks, Servers, Interfaces, Switches,
Hard Drives, and UPSs. They each represent the real-world hardware. An
interface, for our purposes, will be a physical way of connecting two
devices - an NIC, serial line, etc.

If you're experienced in object-oriented programming, you can think of
relationships as inheritance, with an added capability of other
references.

Our Server object will represent a real-world server. It has components
(other objects) such as Interfaces, Hard Drives, and others.

How does this all pull together?

We define, in our asset management software, a Server which has one
Interface (Ethernet NIC called "NIC1") and three Hard Drives (called
HDD1-HDD3). The Interface, in turn belongs to a Network (LAN/VLAN), and
has a field called "connection" which references a Interface of a Switch
object, specifically Interface "Port1" on Switch "Switch1". We'll define
one Network called "LAN" which is identified by the 192.168.0 IP range
(a field of the Network object). We create a Switch object, which
belongs to LAN, has IP 192.168.0.2, and has 24 Interfaces, called
"Port1" through "Port24". This represents a BayStack 450-24T Ethernet
switch. We'll also define a UPS called "SmartUPS", which in turn has an
Interface which is part of "LAN", Connected to Switch1 on Port21.

Now, you see the concept beginning to emerge. We have, in essence, an
inter-related mesh of objects representing physical hardware and its'
properties. This can all be thought of in a three-dimensional form,
which represents the connections and relationships in our network.

The main two advantages of this approach are:

1.  The ability to quickly recognize relationships between objects. If,
for example, we looked at a summary page in Switch1, we would see a
number of static fields describing its properties (manufacturer, model,
IP, MAC, etc.) as well as a diagram of its' relationships. Such a
diagram would look something like:

````
Port1  -> NIC1 -> Server1
Port21 -> SmartSlotCard1 -> UPS1
````

It would also have a listing of Networks which this device is a member
of, specifically:

LAN

In practice, on a web interface, each one of these entries would be a
link to that object's summary. Clicking on LAN, UPS1, Server1, etc.
would show us the summary of that object, so that we can browse through
our physical network. Clicking on LAN, for example, would show LAN's
properties, as well as all devices that are members of LAN (related to
it).

The power of such an approach also relies on binding objects to specific
pieces of hardware. For example, the disk drives in Server1 (HDD1, HDD2,
HDD3) would in turn be references to objects representing actual
physical assets. We can then move these assets around. For example,
let's say that we assign a unique serial number of 000306 at a physical
hard drive. We now create an object for it, and reference HDD3 in
Server1 to this object. If we reconfigure Server1 (physically) by
removing HDD1 (000306) and place it on a shelf, we could then edit
Server1's HDD3 object to be "empty", and have 000306 reassigned to an
object "Shelf02" that represents a physical storage location. By viewing
the summary for Server1, we would see that HDD3 is "empty", but if we
viewed Shelf02, we would see that 000306 is there, waiting to be used.
When we add a server, Server2, we could assign 000306 to that server,
as, say, HDD2.

To give another example, UPS1 is an uninterruptible power supply. We can
"assign" devices to it, such as Switch1 and Server1. Viewing a summary
for UPS1 would show us that Switch1 and Server1 are connected to it.
Similarly, viewing the summary for either Server1 or Switch1 would show
us that they are connected to UPS1. If we add UPS2, we could simply edit
the Server1 object so that it is connected to UPS2, and the UPS1 and
UPS2 objects would show this change automatically.

2. Historical tracking. Every change would be accompanied by a person
responsible, a date and time, a reason, and perhaps other information.
Exactly how this would be implemented is not decided (whether
relationships would be marked as 'deleted' or whether changes would be
held in a separate table in the database), but the idea is that any
object would also contain a history of relationships. From our previous
examples, if we viewed a summary of Server1, we would see that the
connection to UPS1 was severed on a specific date due to a reason such
as "overload" and on that same date, the current connection to UPS2 was
established. Similarly, if we view the summary for HDD2 on Server2, we
would see that the object represents real-world hardware asset \#000306.
Viewing the summary for 000306 would show us that it is a 18.2 Gb SCSI
drive in a Compaq hot-swap tray, and that it was originally installed in
Server1, but moved on a certain date for a certain reason to Shelf02,
and then later moved to Server2.

The implementation of this concept would most likely come about as a
web-based PHP front-end with a MySQL database back-end. In order to
achieve good functionality, there would be a simple interface with quick
execution of common tasks. Most likely, the names I have used such as
Server1, UPS1, HDD3 on Server1, etc. would just be reference names to a
real-world hardware object, and its' data object representation,
identified by a unique ID. For example, the name HDD3 on Server1 would
really just be a reference to 000306, a Hard Drive object.

If we physically removed this drive from Server1 and placed it on
Shelf02, we would browse to the Server1 page in our web interface, and
click on "HDD3", which would bring us to a page representing 000306. We
could then click on a "Move" link, bringing us to a form. This allows us
to enter our name, date and time, reason, etc. and a new location of
"Shelf02". We click submit and the move information is entered into a
table, which references all associated objects - Server1, HDD3 on
Server1, 000306, Shelf02, etc. HDD3 on Server1 has the reference to
000306 removed, and a reference to a History object added. Shelf02 has a
reference to the History object, as well as a reference to 000306,
added.

Now, viewing HDD3 on Server1 would show that there is no physical device
associated with it (empty), but would give a reference (link) to the
000306 drive, the History entry for the removal, and the current
location of 000306 on Shelf02.
