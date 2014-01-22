Title: A Quick Review of Mint.com - from both a user and programmer perspective
Date: 2011-07-03 22:03
Author: admin
Category: Miscellaneous
Tags: finance, mint, review
Slug: a-quick-review-of-mint-com-from-both-a-user-and-programmer-perspective

For those of you who are unfamiliar with [Mint.com][], it's a free
online personal finance site that allows you to track spending across
all of your bank accounts and manage budgets and financial goals. Once
upon a time it was a nice little Web 2.0 startup, now it's owned by
Intuit. The service is free, but it's ad supported, albeit in an
unintrusive way - "partner" services (credit cards, savings accounts,
etc.) are recommended. I've been using it for about two weeks now, with
a goal of tracking my spending, developing a budget and getting a better
handle on my present and future finances. So here are some of my
impressions, considering that the service is still growing but has been
around for a while.

**The Good:**

-   **Account Sync** - Some things I've read online suggest that Mint
    now uses the [Yodlee][] service to sync transactions from your
    financial institutions. Whatever they use, they seem to be able to
    sync transactions and account balances from all of my accounts, even
    ones at a few small investment companies. The sync is fast, and they
    do push notifications (low balance, large deposits, etc.) very well.
    They even seem to support many more institutions than Quicken last
    time I used it (2010 I think).
-   **Budgets** - Mint has a very nice, clean, simple monthly budget
    implementation. You tell it how much you want to spend in a given
    category in a month, and it shows a nice horizontal bar graph of how
    far through your allotment you are. It even makes some suggestions,
    and sets baseline budgets by category based on previous spending.
    About the only problem is when my bi-weely pay checks fall on odd
    weeks in the month. Most of my bills are due near the end of the
    month, and if my pay check happens to be around the same time my
    bills are due, I'll have quite a bit less cash on hand at the
    beginning of the next month than the budgets reflect.
-   **Categorization** - they do it very well. One of their big selling
    points is their categorization engine, and it seemed to get about
    80% of my purchases right, from day one. That's much better than
    anything else I've seen. The only down side is that they only look
    at the Vendor name, not the description - so when I use my debit
    card and the vendor name is "NYCE Transaction" but the store
    name/address is in the description, Mint is hopelessly lost. They
    offer rules to put transactions in category, but only exact matching
    on the vendor name, so there's no way to tell it to look at a
    description that includes "123 Main St". From a programmer's
    perspective, they should allow rules based on either vendor name
    *or* description, and maybe they should let the user highlight or
    specify the part that matches (or a RegEx?).
-   **Apps** - I haven't tried the iOS ones, but the Android app is
    pretty nice. It gives a nice quick picture of your spending and
    account balances, how you're doing with your monthly budget, and any
    alerts/messages. Transaction history isn't easily accessible and is
    per-account only, so it's hard to answer "hmmm, how much did it cost
    last time I was here?" or "where did I get lunch last Tuesday?", but
    it's still handy enough to tell me how much I have left in my
    Entertainment budget, or whether I should put this big purchase on
    my credit or debit card.
-   **Goals** - Mint has a good idea with goals - it includes a number
    of pre-configured financial goals like paying off credit card debt,
    saving for retirement, or stashing away some emergency cash. But in
    order to function correctly, you must have a specific, dedicated
    account for each goal. I guess this is where Mint makes money - they
    suggest accounts with specific attributes (high interest, high
    liquidity, whatever) from their partners. But there doesn't appear
    to be a way to set up a Goal without associating it with a dedicated
    account, and (as per some forum posts I read, I haven't tried this)
    you can't associate a cash asset account with a goal, so there's no
    way to track my progress on building the Depression fund I keep
    under my mattress.

**The Bad/Room for Improvement:**

-   **Customer Service** - I don't know when Mint was bought up by
    Intuit, but to me, they have the feel of an agile Web 2.0 property
    that was bought up by a slow-moving bureaucratic company unable to
    keep up with customer demands or the amount of support requests.
    They use [GetSatisfaction][], a new-age forum-based customer
    "community" provider, for customer service. But their forums are
    filled with feature request threads that have "we'll bring it up to
    Product Development and get back to you" responses over half a year
    old. There appears to be very little follow-through or feedback on
    feature requests, and poor announcement/communication surrounding
    the one feature that was recently brought in to an invitation-only
    beta. Unfortunately, I get the general feeling (and I've found this
    far too many times lately) that they were originally a cutting-edge,
    agile, fast-paced, "cool" service, developed by a team that probably
    stayed up all night coding a cool feature their users were asking
    for, that's now been swallowed up by a behemoth that wants a
    6-month-long risk assessment before writing a line of code.
-   **Cash Tracking** - I understand that Mint makes money from
    recommending the services of lenders, banks, etc. But if you want to
    monetize every single feature, you're bound to fail. In this
    respect, Mint's total lack of cash accounting is a serious failure
    for many of their users (and the forums are filled with threads to
    this effect). The site allows users to manually input cash
    transactions, but that's about it. You can deduct the amount from an
    automatically-synced ATM withdrawal (just your last ATM withdrawal,
    no choice if you have multiple ATM accounts, or you and your
    partner/spouse both use the same Mint account), but that just
    complicates things further. There's also no logic of tracking cash
    on hand - you can create a "Asset" (cash) account, but you have to
    manually update the balance. If you're like me and use cash for
    small purchases, or often get meals at local places that only accept
    cash, this becomes quite a bit of a hassle. Even more so if, like
    me, you've ever lost an ATM card on a holiday weekend, and now keep
    some actual cash in the house. Honestly, I think this is my biggest
    complaint about Mint, and the one that's most likely to keep me
    looking for alternatives. More importantly, this has been requested
    and voted for over and over on their support forums for over a year,
    with no informational response. For a company whose developers
    aggregate and analyze data from thousands of banks, I'd think that
    letting users type in a series of dollar amounts and then totaling
    it up would be pretty easy.
-   **Scheduled Transactions** - On the plus side, Mint parses the "next
    payment due" date out of credit card and loan account information,
    so it gives you nice (email, SMS, and web) alerts a configurable
    number of days before. However, it doesn't even have a feature to
    set calendar reminders for when bills are due, so I'm still stuck
    opening Mint and Google Calendar if I need to figure out whether I
    can make that big purchase today or if I should wait until my next
    pay check. This was also a very commonly requested feature on their
    forums, and apparently they have an invitation-only beta running.
    But I responded to the thread a few days late, so I wasn't given an
    invitation. As far as I can tell, there was never an announcement of
    the beta, and I never got a chance to check a "please let me beta
    test" box.
-   **Forecasting** - This is my \#2 biggest issue with Mint, after the
    lack of cash tracking. And the other one most likely to drive me
    either to another service, to write my own software (again), or to
    go back to a spreadsheet. Mint is great at tracking your transaction
    history, your account balances and net worth, and your current
    monthly budget. But it has absolutely no concept of financial
    forecasting or balance predictions. If you're on a tight budget,
    this can be a problem. At the moment, I have a spreadsheet were I
    keep a list of all of my regularly recurring expenses (in date order
    over the month), my pay dates, and the combined balance of my
    checking/savings accounts. I can easily see what (within reason, not
    counting discretionary expenses) my cash on hand will be at any time
    in the month. This seems like a no-brainer necessary feature for a
    site like Mint, and combined with its great budgeting features,
    could provide a wonderful picture of what to expect in the next
    month or two, and when I should plan on making that unusually large
    purchase.
-   **Couples/Families** - My girlfriend and I both use Mint, and have
    somewhat combined finances (but not accounts). It doesn't make sense
    for us to have two Mint accounts, since it would be a real pain to
    keep track of. But, on the other hand, having all of our accounts in
    one Mint isn't an ideal solution either. I can categorize
    transactions, but there's no easy way to track *who* the purchase
    was for, short of duplicating (or triplicating - Me, Her, Both) all
    of the categories. I'm trying something with tags, but it's a real
    kludge in Mint's search interface to get a list of transactions
    filtered by category *and* tag. Also, the account name doesn't show
    up in the transactions list unless you pull down the Detail box for
    a transaction, so it's troublesome to look through a list and sort
    out whose cards everything was on.

**Miscellaneous:**

-   **Passwords.** In order to sync data from my banks, I have to supply
    mint.com with all of my login credentials. I understand that, until
    banks enter the 21st century (and be smart about it - even a less
    likely possibility) this is just the way it is, and I can't blame
    Mint for a system imposed by the banks. But still, I'm not too happy
    about the idea of Mint storing in plain text (I assume, since they
    need to pass them on to the bank) my username and password for all
    of my banking sites. I got some comfort knowing that the site is
    owned by Intuit - a company that, if not totally security-minded, is
    at least big enough not to fold overnight after a breach. Maybe one
    day, banks and credit card companies will let me specify separate
    credentials specific to third-party software and websites, which I
    could then revoke with my "master" password. Until then, I guess
    this is just a risk I have to live with.
-   **Importing Transactions** - Mint only supports importing up to 3
    months of transaction data per account. Some institutions provide
    less than that. Obviously Intuit doesn't want people switching from
    their paid software, so the two YEARS of transactions I meticulously
    categorized in Quicken are now useless to me in Mint. However, I
    guess I can't really fault them too much on this one. Firstly, that
    would be a LOT of data for them to store. It would also be much more
    of a headache to try and ensure that the export formats of whatever
    software packages they support are properly parsed.

**Conclusions:**

Mint does a lot of things well. And it's a nice clean interface. But
there are also some key features missing, which I feel like I really
need. So, for the time being, I'm going to keep using mint, but also
explore what other options are available, and look into anyone who
offers an API for pulling transaction data that might actually be
powerful enough for me to use to write my own web-based app (since my
attempts at pulling [OFX][] feeds only worked for about half my
accounts). If you don't care as much about tracking cash spending/cash
on hand, and are financially stable enough that you don't need to
forecast the next month or two, Mint is wonderful.

  [Mint.com]: http://www.mint.com
  [Yodlee]: http://yodlee.com
  [GetSatisfaction]: http://getsatisfaction.com/
  [OFX]: http://en.wikipedia.org/wiki/OFX
