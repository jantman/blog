Title: RPM Spec Files for nodejs 0.9.5 and v8 on CentOS 6
Date: 2013-01-31 14:13
Author: admin
Category: Software
Tags: build, centos, node, nodejs, package, packaging, redhat, RHEL, rpm, specfile
Slug: rpm-spec-files-for-nodejs-0-9-5-and-v8-on-centos-5

The latest version of nodejs that I could find as an RPM for CentOS was
0.6.16, from
[http://patches.fedorapeople.org/oldnode/stable/](http://patches.fedorapeople.org/oldnode/stable/).
That's the one that puppetlabs currently uses in their
[puppetlabs-nodejs](https://github.com/puppetlabs/puppetlabs-nodejs)
module. There is, however, a nodejs 0.9.5 RPM in the Fedora Rawhide (19)
repository. Below are some patches to that specfile, and the specfile
for its v8 dependency, to get them to build on CentOS 6. You can also
find the full specfiles on my [github specfile
repository](https://github.com/jantman/specfiles). I had originally
wanted to get them built on CentOS 5 as well, but after following the
dependency tree from nodejs to http-parser to gyp, and then finding
issues in the gyp source that are incompatible with CentOS 5's python
2.4, I gave up on that target.

**nodejs.spec**, diff from Fedora Rawhide nodejs-0.9.5-9.fc18.src.rpm,
buildID=377755 ([full
specfile](https://raw.github.com/jantman/specfiles/master/nodejs.spec))

~~~~{.diff}
diff --git a/nodejs.spec b/nodejs.spec
index 050ed86..86c0f4b 100644
--- a/nodejs.spec
+++ b/nodejs.spec
@@ -1,6 +1,6 @@
 Name: nodejs
 Version: 0.9.5
-Release: 9%{?dist}
+Release: 10%{?dist}
 Summary: JavaScript runtime
 License: MIT and ASL 2.0 and ISC and BSD
 Group: Development/Languages
@@ -25,7 +25,7 @@ Source6: nodejs-fixdep
 BuildRequires: v8-devel >= %{v8_ge}
 BuildRequires: http-parser-devel >= 2.0
 BuildRequires: libuv-devel
-BuildRequires: c-ares-devel
+BuildRequires: c-ares-devel >= 1.9.0
 BuildRequires: zlib-devel
 # Node.js requires some features from openssl 1.0.1 for SPDY support
 BuildRequires: openssl-devel >= 1:1.0.1
@@ -165,9 +165,13 @@ cp -p common.gypi %{buildroot}%{_datadir}/node
 
 %files docs
 %{_defaultdocdir}/%{name}-docs-%{version}
-%doc LICENSE
 
 %changelog
+* Thu Jan 31 2013 Jason Antman  - 0.9.5-10
+- specify build requirement of c-ares-devel >= 1.9.0
+- specify build requirement of libuv-devel 0.9.4
+- remove duplicate %doc LICENSE that was causing cpio 'Bad magic' error on CentOS6
+
 * Sat Jan 12 2013 T.C. Hollingsworth  - 0.9.5-9
 - fix brown paper bag bug in requires generation script
~~~~

**v8.spec**, diff from Fedora Rawhide 3.13.7.5-2 ([full
specfile](https://raw.github.com/jantman/specfiles/master/v8.spec))

~~~~{.diff}
--- v8.spec.orig       2013-01-26 16:03:18.000000000 -0500
+++ v8.spec     2013-01-31 09:04:51.068029459 -0500
@@ -21,9 +21,11 @@
 
 # %%global svnver 20110721svn8716
 
+%{!?python_sitelib: %define python_sitelib %(%{__python} -c "import distutils.sysconfig as d; print d.get_python_lib()")}
+
 Name:          v8
 Version:       %{somajor}.%{sominor}.%{sobuild}.%{sotiny}
-Release:       2%{?dist}
+Release:       5%{?dist}
 Epoch:         1
 Summary:       JavaScript Engine
 Group:         System Environment/Libraries
@@ -32,7 +34,7 @@
 Source0:       http://commondatastorage.googleapis.com/chromium-browser-official/v8-%{version}.tar.bz2
 BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
 ExclusiveArch: %{ix86} x86_64 %{arm}
-BuildRequires: scons, readline-devel, libicu-devel
+BuildRequires: scons, readline-devel, libicu-devel, ncurses-devel
 
 %description
 V8 is Google's open source JavaScript engine. V8 is written in C++ and is used 
@@ -51,8 +53,13 @@
 %setup -q -n %{name}-%{version}
 
 # -fno-strict-aliasing is needed with gcc 4.4 to get past some ugly code
-PARSED_OPT_FLAGS=`echo \'$RPM_OPT_FLAGS -fPIC -fno-strict-aliasing -Wno-unused-parameter -Wno-error=strict-overflow -Wno-error=unused-local-typedefs -Wno-unused-but-set-variable\'| sed "s/ /',/g" | sed "s/',/', '/g"`
+%if 0%{?el5}
+PARSED_OPT_FLAGS=`echo \'$RPM_OPT_FLAGS -fPIC -fno-strict-aliasing -Wno-unused-parameter -lncurses\'| sed "s/ /',/g" | sed "s/',/', '/g"`
+sed -i "s|'-O3',|$PARSED_OPT_FLAGS,|g" SConstruct
+%else
+PARSED_OPT_FLAGS=`echo \'$RPM_OPT_FLAGS -fPIC -fno-strict-aliasing -Wno-unused-parameter -Wno-error=strict-overflow -Wno-unused-but-set-variable\'| sed "s/ /',/g" | sed "s/',/', '/g"`
 sed -i "s|'-O3',|$PARSED_OPT_FLAGS,|g" SConstruct
+%endif
 
 # clear spurious executable bits
 find . \( -name \*.cc -o -name \*.h -o -name \*.py \) -a -executable   
@@ -198,6 +205,17 @@
 %{python_sitelib}/j*.py*
 
 %changelog
+* Thu Jan 31 2013 Jason Antman  - 1:3.13.7.5-5
+- remove -Werror=unused-local-typedefs on cent6
+
+* Wed Jan 30 2013 Jason Antman  - 1:3.13.7.5-4
+- define python_sitelib if it isn't already (CentOS 5)
+
+* Wed Jan 30 2013 Jason Antman  - 1:3.13.7.5-3
+- pull 3.13.7.5-2 SRPM from Fedora 19 Koji most recent build
+- add ncurses-devel BuildRequires
+- modify PARSED_OPT_FLAGS to work with g++ 4.1.2 on CentOS 5
+ 
 * Sat Jan 26 2013 T.C. Hollingsworth  - 1:3.13.7.5-2
 - rebuild for icu-50
 - ignore new GCC 4.8 warning
~~~~
