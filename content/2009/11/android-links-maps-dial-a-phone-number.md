Title: Android links - maps, dial a phone number
Date: 2009-11-22 10:25
Author: admin
Category: Android
Tags: android, google, html
Slug: android-links-maps-dial-a-phone-number

If you've used Google search from an Android device to search for a
business, you've probably noticed the two interesting "buttons" to the
right of the search listing - "Get Directions" and a button for the
phone number. It turns out, these are pretty easy to implement.

The "Get Directions" link is a simple link to [Google Maps][] like [This
One][]. The links are actually pretty simple:

~~~~{.html}
Get Directions
~~~~

It just uses a regular Google Maps URL, with the destination address
encoded. When the link is clicked in the Android browser, a dialog pops
up asking the user whether he wants to open it with the browser or the
Maps application. If Maps is selected, it automatically opens with the
address from the URL in the destination input box, the phone's current
location as the start input, and gives easy access to directions and
navigation.

The telephone links are a bit more interesting. Apparently, the Android
browser uses the Phone app to handle the "tel" scheme, as defined by
[RFC 3966][].Therefore, clicking a link like:

~~~~{.html}
201-555-5555
~~~~

on Android will bring up the Phone app and pre-enter the digits for
2015555555. Luckily, it doesn't automatically dial the number. If you
want to give it a try and are using Android: [201-555-5555][].

The final step is how to implement this. I don't know if most mobile
browsers (Blackberry? iPhone?) also support the "tel" URI scheme, or how
they'll handle Google Maps links. But if you're looking to include
Android-specific content, the user agent string from my Motorola Droid
(Android 2.0) looks like:

~~~~{.text}
Mozilla/5.0 (Linux; U;Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17
~~~~

I know that there are a number of PHP classes out there to detect
browsers (like [Chris Schuld's browser.php][]) and some things to detect
mobile device capabilities (like [WURFL][] or [Tera WURFL][], both using
the [WURFL][1] data). However, if you just need to know whether your
user is on Android or not, I'd personally recommend just checking the
user agent string for "Linux", "Android" and "WebKit" until a better
browser identification system is found, as these are not likely to
change in the near future.

  [Google Maps]: http://maps.google.com
  [This One]: http://maps.google.com/maps?daddr=42+Pierce+Ave,+Midland+Park,+NJ+07432
  [RFC 3966]: http://tools.ietf.org/html/rfc3966
  [201-555-5555]: tel:2015555555
  [Chris Schuld's browser.php]: http://chrisschuld.com/projects/browser-php-detecting-a-users-browser-from-php/
  [WURFL]: http://wurfl.sourceforge.net/nphp/
  [Tera WURFL]: http://freshmeat.net/projects/tera_wurfl/
  [1]: http://en.wikipedia.org/wiki/Wurfl
