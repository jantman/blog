Title: Script to easily rebuild a SRPM
Date: 2013-05-28 10:26
Author: admin
Category: Tech HowTos
Tags: lzma, packaging, rpm, rpm2cpio, rpmbuild, srpm, xz
Slug: script-to-easily-rebuild-a-srpm

Between RHEL/CentOS 5 and 6 the default RPM compression format was
changed to xz. As such, trying to build a recent Fedora or Cent6 SRPM on
Cent5 will error out with a message like
`error: unpacking of archive failed on file foo;51a4c2a5: cpio: MD5 sum mismatch`
because tar on CentOS 5 doesn't support xz.

Here's a quick and dirty little script to use `rpm2cpio` to rebuild a
SRPM using the host's native RPM compression. The latest version will
live at
[https://github.com/jantman/misc-scripts/blob/master/rebuild\_srpm.sh][]

~~~~{.bash}
#!/bin/bash
#
# Script to rebuild a SRPM 1:1, useful when you want to build a RHEL/CentOS 6
# SRPM on a RHEL/CentOS 5 system that doesn't support newer compression (cpio: MD5 sum mismatch)
#
# by Jason Antman 
# The latest version of this script will always live at:
# 
#

if [[ -z "$1" || "$1" == "-h" || "$1" == "--help" ]]
then
    echo "USAGE: rebuild_srpm.sh  "
    exit 1
fi

if [[ -z "$2" ]]
then
    OUTDIR=`pwd`
else
    OUTDIR="$2"
fi

if [[ ! -e "$1" ]]
then
    echo "ERROR: SRPM file not found: $1"
    exit 1
fi

if ! which rpmbuild &> /dev/null
then
    echo "rpmbuild could not be found. please install. (sudo yum install rpm-build)"
    exit 1
fi

if ! which rpm2cpio &> /dev/null
then
    echo "rpm2cpio could not be found. please install. (sudo yum install rpm)"
    exit 1
fi

SRPM=`dirname "$1"`"/"`basename "$1"`
TEMPDIR=`mktemp -d`
STARTPWD=`pwd`

echo "Rebuilding $SRPM..."

# copy srpm into tempdir
cp $SRPM $TEMPDIR

pushd $TEMPDIR &>/dev/null

# setup local build dir structure
mkdir -p rpm rpm/BUILD rpm/RPMS rpm/SOURCES rpm/SPECS rpm/SRPMS rpm/RPMS/athlon rpm/RPMS/i\[3456\]86 rpm/RPMS/i386 rpm/RPMS/noarch rpm/RPMS/x86_64

# setup rpmmacros file
cat /dev/null > $TEMPDIR/.rpmmacros
echo "%_topdir        $TEMPDIR/rpm" >> ~/.rpmmacros

echo "Extracting SRPM..."
pushd $TEMPDIR/rpm/SOURCES/ &>/dev/null
rpm2cpio $SRPM | cpio -idmv &>/dev/null
popd &>/dev/null

# build the SRPM from the spec and sources
# we're just building a SRPM so we can ignore dependencies
echo "Rebuilding SRPM..."
NEW_SRPM=`rpmbuild -bs --nodeps --macros=$TEMPDIR/.rpmmacros $TEMPDIR/rpm/SOURCES/*.spec | grep "^Wrote: " | awk '{print $2}'`

echo "Copying to $OUTDIR"
cp $NEW_SRPM $OUTDIR/

echo "Wrote file to $OUTDIR/`basename $NEW_SRPM`"

# cleanup
cd $STARTPWD
rm -Rf $TEMPDIR
~~~~

  [https://github.com/jantman/misc-scripts/blob/master/rebuild\_srpm.sh]:
    https://github.com/jantman/misc-scripts/blob/master/rebuild_srpm.sh
