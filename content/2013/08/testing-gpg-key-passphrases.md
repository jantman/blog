Title: Testing GPG Key Passphrases
Date: 2013-08-26 06:00
Author: admin
Category: Software
Tags: encryption, gnupg, gpg, key, passphrase, pgp
Slug: testing-gpg-key-passphrases

So hypothetically, you have a GPG public/private keypair (from a backup
or old computer), but you don't remember the passphrase. Here's a
relatively simple way to find it from a number of possible options. This
*requires* that you have a computer secure enough to store the possible
options in a text file. I'd recommend storing that file on a
ramdisk/tmpfs, and using a temporary VM for this, which you'll wipe away
when you're done.

**Preparation:**

1.  You have an appropriately secure place to do this with GPG
    installed, and a safe place to store a text file of sample
    passphrases (i.e. a ramdisk).
2.  Copy your backed up public and private keys to `~/.gnupg` on that
    host. Let's assume they're called `TestUser_public.key` and
    `TestUser_private.key`. We're assuming that you KNOW, BEYOND A DOUBT
    that these are your keys (i.e. you got them from a secure offline
    backup medium, you've verified against a printed key fingerprint,
    you've verified the fingerprints against a
    [keyserver](http://pgp.mit.edu/) that you know is authoritative for
    your keys, etc.).
3.  First, we import the public and private keys to GPG:

        :::console
        testuser:~$ cd .gnupg
        testuser:~/.gnupg$ gpg --import TestUser_public.key 
        gpg: keyring `/home/testuser/.gnupg/secring.gpg` created
        gpg: key 17AD8D3D: public key "Test User (Test User) " imported
        gpg: Total number processed: 1
        gpg:               imported: 1  (RSA: 1)
        
        testuser:~/.gnupg$ gpg --allow-secret-key-import --import TestUser_secret.key 
        gpg: key 17AD8D3D: secret key imported
        gpg: key 17AD8D3D: "Test User (Test User) " not changed
        gpg: Total number processed: 1
        gpg:              unchanged: 1
        gpg:       secret keys read: 1
        gpg:   secret keys imported: 1

4.  Check that the keys are there:

        :::console
        testuser:~/.gnupg$ gpg --list-keys
        /home/testuser/.gnupg/pubring.gpg
        --------------------------------
        pub   2048R/17AD8D3D 2013-08-24
        uid                  Test User (Test User) 
        sub   2048R/40D9F35E 2013-08-24
        
        testuser:~/.gnupg$ gpg --list-secret-keys
        /home/testuser/.gnupg/secring.gpg
        --------------------------------
        sec   2048R/17AD8D3D 2013-08-24
        uid                  Test User (Test User) 
        ssb   2048R/40D9F35E 2013-08-24
        
        testuser:~/.gnupg$ 

5.  Note the fingerprint of the key which is, in this case, `17AD8D3D`.

**Testing Passphrases:**

1.  Now that we have the keys imported, we're ready to test some
    passphrases. Enter your passphrases, one per line, in a text file.
    We're assuming that we're working on a totally secured host
    (ideally, a VM running on a standalone, non-networked machine) that
    will be destroyed when we're done. For added security, I'd put this
    file on a ramdisk. In this example, the actual passphrase for the
    key is "test". Here's our text file:

        :::console
        testuser:~/.gnupg$ cat /tmp/passphrases 
        bad
        notgood
        notright
        test

2.  Next, create a test data file to try to sign/encrypt:

        :::console
        testuser:~/.gnupg$ echo "test input" > /tmp/test.in

3.  Now we run the actual test (see below for more information...)

        :::console
        testuser:~/.gnupg$ for p in `cat /tmp/passphrases`; do echo "$p" | gpg -q --sign --local-user 17AD8D3D --passphrase-fd 0 --output /dev/null --yes /tmp/test.in && (echo "CORRECT passphrase: $p" && break); done
        Reading passphrase from file descriptor 0    
        
        You need a passphrase to unlock the secret key for
        user: "Test User (Test User) "
        2048-bit RSA key, ID 17AD8D3D, created 2013-08-24
        
        gpg: skipped "17AD8D3D": bad passphrase
        gpg: signing failed: bad passphrase
        Reading passphrase from file descriptor 0    
        
        You need a passphrase to unlock the secret key for
        user: "Test User (Test User) "
        2048-bit RSA key, ID 17AD8D3D, created 2013-08-24
        
        gpg: skipped "17AD8D3D": bad passphrase
        gpg: signing failed: bad passphrase
        Reading passphrase from file descriptor 0    
        
        You need a passphrase to unlock the secret key for
        user: "Test User (Test User) "
        2048-bit RSA key, ID 17AD8D3D, created 2013-08-24
        
        gpg: skipped "17AD8D3D": bad passphrase
        gpg: signing failed: bad passphrase
        Reading passphrase from file descriptor 0    
        
        You need a passphrase to unlock the secret key for
        user: "Test User (Test User) "
        2048-bit RSA key, ID 17AD8D3D, created 2013-08-24
        
        CORRECT passphrase: test
        testuser:~/.gnupg$ 

4.  And there we have it, the working passphrase. I'm sure there's a
    more efficient way to do this, and probably a more secure way, but
    I'm not trying to brute-force someone's GPG key, I'm trying to
    remember which one of my (many, many) passwords I used for a GPG key
    that I generated a decade ago.

The actual command that we ran, rewritten with some linebreaks for
legibility, is:

    :::bash
    for p in `cat /tmp/passphrases`
    do
        echo "$p" | gpg -q --sign --local-user 17AD8D3D --passphrase-fd 0 --output /dev/null --yes /tmp/test.in && (echo "CORRECT passphrase: $p" && break)
    done

This loops over each line in the passphrases file (each passphrase that
we want to try), and for each one, echoes the password and pipes it to
STDIN of `gpg`, which tries to sign /tmp/test.in (sending the output
to /dev/null) using the key with ID `17AD8D3D` (from #5 in the
Preparation steps above) and a password provided on STDIN. If the GPG
command succeeds, we echo the passphrase and stop looping through the
passphrases file.

I hope I wouldn't have to say this for anyone who's reading my blog, but
this information (as easy as it is to be figured out), is not to be used
for unethical purposes.
