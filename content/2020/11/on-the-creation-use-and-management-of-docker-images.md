Title: On The Creation, Use, and Management of Docker Images
Date: 2020-11-10 15:11
Modified: 2020-11-10 15:11
Author: Jason Antman
Category: Software
Tags: docker, build, deploy, image, container
Slug: on-the-creation-use-and-management-of-docker-images
Summary: Some hard-earned thoughts on how to build, manage, and use Docker images.

[TOC]

# Introduction

I know that it's been ages since I've posted anything here, but frankly, I haven't had much interest to. I've been in a strange place personally for the past few years, and especially for much of 2020. I've let much of my public/professional profile languish over the past few years, and I also haven't given my open source projects the attention they deserve. I'm hoping to fix that soon, and hopefully this post is the first step. I'm also hoping to add a few posts on the non-computer-related DIY carpentry and electronics projects that I've worked on over the past year, as well as my first steps into 3D printing. Hopefully my interest in writing will hold.

For the past five years I've been working on a team that's called Release Engineering, but is best described as a tooling & automation development and consulting team (we'd likely be Developer Enablement anywhere else). Our goal is to provide tooling, consulting services, processes, documentation, and timely advice to a bunch (i.e. over 100) of software development teams. While my team is heavily involved in many aspects of software and infrastructure lifecycle, most of our work is with AWS infrastructure automation and with build/test/deploy pipelines. One common thread that connects the two is the use of Docker images, both as the environment where we run much of our tooling, build, and test processes, as well as the final artifact from our build processes - the blob of ones and zeroes that actually gets deployed and run.

It's safe to say that I don't make it through a normal work day without running a bunch of Docker containers and likely building (via automated pipelines, of course) a few. It's also safe to say that, after spending five-ish years working on Docker-heavy processes at a large Enterprise, including being intimately involved with developing many of our tools, processes, and standards around Docker, and helping in the management of multiple private Docker Registries, I have some pretty strong opinions and some advice that I find myself passing on time after time. The extreme popularity and accessibility of Docker is wonderful, and has certainly been wonderful for everyone involved in the software and operations lifecycles. However, along with this has also come a large amount of misinformation and poor examples on how to use Docker, and a striking difficulty in finding good information on the hard-earned lessons from using Docker at scale.

There are some wonderful resources, including the official Docker documentation, for how to run Docker. This post is going to focus on Docker Images and their lifecycle.

**IMPORTANT:** Please note that (1) while my language may be rather declarative, *this is just my opinion*. It's shared by many others in the industry, and it's based on hard-learned lessons, but it's still an opinion. Also, (2), if you're not doing what I describe here, *I'm not by any means saying that you're "doing Docker wrong"*. These are lessons learned from a company that builds hundreds of Docker images every day, and has thousands of them running at any given time. **In short, this is what I wish someone told us many years ago.**

# On to the topic: Docker

## Aside - Nomenclature

For those who may not be familiar with the difference, the following are taken from the [Docker Glossary](https://docs.docker.com/glossary/):

[Docker image](https://docs.docker.com/glossary/#image):

> Docker images are the basis of containers. An Image is an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime. An image typically contains a union of layered filesystems stacked on top of each other. An image does not have state and it never changes.

[Docker container](https://docs.docker.com/glossary/#container):

> A container is a runtime instance of a docker image.
>
> A Docker container consists of
>
> * A Docker image
> * An execution environment
> * A standard set of instructions
>
> The concept is borrowed from Shipping Containers, which define a standard to ship goods globally. Docker defines a standard to ship software.

## What Docker Images Are and Aren't

To begin with, I'm going to make some blanket statements about what Docker (mainly in the context of images, and containers) is and isn't:

* Docker images are **not Virtual Machines (VMs)**. While they do provide a means to isolate some data and process(es) and a way to start and stop them, they still share a kernel with the underlying operating system and are visible to it, and do not _virtualize_ anything. They're really just a way to group and (somewhat, and only if done very carefully) isolate things from the underlying Linux kernel (or the various compatibility layers for Mac, Windows, and other OSes).
* Docker images are much more analogous to **software packages**, albeit ones that also know about the environment and some networking, and can have their own storage (volumes). In so far as building and distributing software is concerned, Docker images should mostly be regarded like any other package or artifact.
* Docker containers (and images) should ideally only [run on service per image/container](https://docs.docker.com/config/containers/multi-service_container/). Most of the docker ecosystem is built around this concept. While there are many images that don't follow this pattern (especially earlier images and proprietary software), you usually wouldn't put your application, web server, and database in the same package, and they shouldn't be in the same image either. [docker-compose](https://docs.docker.com/compose/) was specifically designed to aid in this pattern.
* Docker image **tags are package versions.** No packaging system that I'm aware of doesn't have a concept of a version. With Docker images, that versioning is entirely up to you - by tagging your images. You can tag a single image multiple times, and probably should. Every docker image that's built should have at least one completely unique tag, so that same exact image can be used where needed. For versioning, tags that get updated can and should be used (i.e. if you release version X.Y.Z of your image, you can have X and X.Y tags that point to the most recent relevant image).
* The ``latest`` tag is horribly misleading. There is nothing magic or special about ``latest``; it is simply a convention. If you build and push a newer Docker image and don't tag it ``latest`` (and push that tag), your ``latest`` will still point to an older image. Using the ``latest`` tag also removes repeatability when running containers.
* If at all possible, Docker images should not write log files to disk. Docker has pluggable [logging drivers](https://docs.docker.com/config/containers/logging/configure/), the simplest being the default which is what's displayed by ``docker logs``. Ideally, all logs should go to STDOUT or STDERR of the container, and the Docker daemon should be configured to handle them appropriately.
* Many of the best practices for working with Dockerized services match up well with the [12 factor app](https://12factor.net/) guidelines.

If you're unsure about any of the prescriptive statements I've made, I'd encourage you to look at the [docker-library Official images](https://github.com/docker-library/official-images). These are the official Docker images for many popular programming languages, runtimes, and applications. Most, if not all, of them follow these guidelines. The [docker-library README](https://github.com/docker-library/official-images/blob/master/README.md) provides some very helpful information.

## What to put in an image

A Docker image should only run one service. That may mean more than one _process_ (in the case of a forking or threaded model), but there should only be one service, and ideally no real init subsystem; just a daemon, perhaps run via a wrapper script. Not only is this in line with the Docker model (see [here](https://docs.docker.com/config/containers/multi-service_container/) as an official reference), but it also provides many benefits in terms of isolation (especially if using resource limits), monitoring, modularity and management. Even in trivial cases such as a desktop or home computer, it may be desirable to upgrade or restart services separately, move them to different machines on the same network, or swap out one service for another. When multiple services are needed, they should be run as separate containers and connected via [Docker networking](https://docs.docker.com/network/). This can be made easy for inexperienced users via [docker-compose](https://docs.docker.com/compose/), but retains the flexibility desired by more experienced users with more advanced configurations.

## Configuration

Configuration should never be included in a Docker image. One of the main advantages of Docker is "build once, run anywhere", where a single image can be used anywhere it's needed (i.e. in the test environment, on a developer's laptop, and anywhere through production). I won't go into the many possibilities in configuration management, but for a general-purpose image, it's most desirable to take all configuration via environment variables with sane defaults provided as needed. For more complex scenarios (such as a web server needing many configuration files), it's preferable to provide sane defaults built-in to the container and allow overriding them by mounting a directory of configuration files to a known path in the container.

Under no circumstances should a Docker image be built multiple times for running on different systems/environments/locations.

## Logging

Logging should not be written directly to files. This is a bit more difficult if you deviate from the one-service-per-container model, but ideally all logging should be sent to the container's STDOUT and STDERR streams. This will be captured by the Docker daemon and available via the ``docker logs`` command if using the default [logging driver](https://docs.docker.com/config/containers/logging/configure/), or sent wherever the daemon is configured otherwise. Handling logging this way has a number of benefits including a unified way to view logs (``docker logs``), not bloating the container filesystem with log files, not needing to enter into the container to view logs, and compatibility with configurations that send logs to some variety of centralized aggregation, storage, or analysis.

Furthermore, the STDOUT and STDERR streams should be logically separated either by level (i.e. error messages to STDERR, normal output or info/debug to STDOUT) or by function (i.e. web server access logs to STDOUT and error logs to STDERR).

## Tagging and Versioning

Docker image tags determine which one of an unlimited number of variations of a single image is used. On the official Docker Hub images, they're used both to specify a version (i.e. ``python:2.7`` or ``python:3.8.2``) as well as to specify an optional variant with some sort of difference, often the base image use (i.e. ``python:3.8.6-buster`` vs ``python:3.8.6-alpine3.11``). On most official images, a given image has multiple tags; for example, the current _newest_ stable Python image, ``python:latest`` (what you get if you omit a tag, and just ``docker pull python``), is also tagged with ``3.9.0-buster``, ``3.9-buster``, ``3-buster``, and ``buster``. Similarly, the newest official Alpine Linux-based Python image is tagged with eight (8) tags: ``3.9.0-alpine3.12``, ``3.9-alpine3.12``, ``3-alpine3.12``, ``alpine3.12``, ``3.9.0-alpine``, ``3.9-alpine``, ``3-alpine``, ``alpine``. The first, and most specific, of these tags (``3.9.0-alpine3.12``) is generally unchanging; there will (usually) only be one ``python:3.9.0-alpine3.12`` image published ever. Running this image should always get you an identical container, without any changes from the last time you pulled and ran it, forever. The less-specific tags, however, change over time to point to the newest relevant image. In this way, image tags can be used like version specifiers in many packaging systems; you can choose to install a very specific, unchanging version of some dependency, or you can choose to install the newest version within some range.

One possible caveat in this is that I'm not sure if Docker Hub (for official images) enforces that the most specific tag will _never_ change. In general, I strongly recommend that every image built have at least one completely unique tag that will never be used on another build of that image. This makes it much easier to refer to one specific, unique image, than having to deal with the image digest hash. Many examples that I've seen build this unique tag based on some combination of source control information and timestamp; at my company, our usual practice is to build images with a tag based on the git branch or PR number, short commit SHA that's being built, and the current integer timestamp. If a build succeeds and gets released, we'll then re-tag the image with the [semver](https://semver.org/) version number.

The key point here is that (in most cases) any image that makes it past the initial image build and testing stage should be tagged multiple or many times, to suit the two different purposes of tags:

* One completely unique tag, to identify that exact image for all eternity.
* One or more (usually three or more) version tags, to allow specifying a major, major.minor, or major.minor.patch version of the image.

For images that are used solely within an automated build and deploy process, you may choose to completely ignore and never use the ``latest`` tag. For images that at any point will or may be manually pulled by humans, or any public images, the ``latest`` tag should be used and point to the most recent _stable_ version.

## Repeatable Builds

Especially since the 2020 [Docker Hub announcement](https://www.docker.com/blog/scaling-dockers-business-to-serve-millions-more-developers-storage/) that images without any activity for six months will be deleted, it is vitally important that Docker image builds be [reproducible](https://martinfowler.com/bliki/ReproducibleBuild.html). Even for personal projects or companies with private Docker registries, it is always possible that you'll need to revisit an old version, test for a regression, or simply rebuild a system that was happily running an uncommon image for a long time. **Running ``docker build`` on a given Dockerfile, with the same arguments, should produce a functionally identical image on any machine at any point in time.** As such, all version information for sources (including dependencies) outside of your repository should be either hard-coded explicitly or passed via build-time [ARG](https://docs.docker.com/engine/reference/builder/#arg) arguments in the Dockerfile. Further, nothing during the build process should ever download un-versioned URLs (i.e. clone from git master, or download the "latest" of something).

Two possible exceptions to this are the base / FROM image, and operating system packages. Ideally the base/FROM image should be defined in the Dockerfile with an immutable tag, but in some cases it's desirable to always use the latest image, or to use a less-constrained version tag. In these cases, your build tooling should resolve and record the image used in the FROM tag, and also ideally add this as a label on the final image. Similarly, when dealing with OS packages which may be updated within a given release, it's desirable to generate a listing of all installed packages before the build finishes and store this somewhere if needed at a later date.

## No Runtime Downloads

Dependencies should never be downloaded by a container when it starts up. Doing so breaks repeatability of the image, introduces significant latency to the startup process, and makes possibly-invalid assumptions about network connectivity and available bandwidth. Dependencies that need to be downloaded from the Internet should either be packaged inside the image itself, or downloaded by the user (or some system/automation) and mounted into the container.

## Everything in Source Control (Git)

Your Dockerfile, as well as any dependencies for building the image that are not part of another project/artifact/package, should be stored in source control. More often than not these days, that means git. This repository should include the Dockerfile, instructions for building and developing the image, and anything that needs to be COPY'ed or ADD'ed into the image. If at all possible, your images should be tagged or labeled with the git commit hash that was used to build them. The repository should have tags (ideally full Releases, if hosting on GitHub or a similar system) at least corresponding to every released image (i.e. X.Y.Z for projects using semver).

This process has a number of benefits for every image, but especially for public images of open-source projects:

* It's clear how to find the exact source code that was used to build a specific image, so that you or contributors can troubleshoot or modify it.
* It allows easy reproduction and regression of bugs, by running specific versions of the image.
* It enables using automated systems to build the image, such as Docker Hub automated builds.

## Labels

Docker images should make use of [LABELs](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#label) for storing metadata, passed in as build arguments (ARG). There is a label schema that's gaining acceptance at [http://label-schema.org/](http://label-schema.org/) which provides some very useful suggestions and guidelines. I recommend implementing as many of these as practical. In addition, I often find it useful to include a label with the URL to the automated build that generated the image if possible, as well as to any applicable test results. This can be quite useful when troubleshooting.

## Add a HEALTHCHECK

The Dockerfile [HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck) allows specifying a command to be executed inside running containers at a configurable interval, to check the health of the container. Unless you know for certain that any critical failure in the container will cause it to exit, you should add a health check. This is especially important in any container that uses an init system or runs multiple services. It is generally assumed that, when running Docker containers, they will exit on failure and leave it up to some external system - your service manager, the docker Daemon, etc. - to restart them and track these events.

## Testing Built Images

It is generally unwise to assume that a ``docker build`` is correct just because all commands during the build succeeded. Many times I've seen otherwise-good Dockerfiles result in broken images because a library version changed, an executable was moved to a different package, some dependency problem exists, or an exit code went unchecked somewhere deep in a script. The Dockerfile [HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck) is very important, but it only applies to running containers.

At a minimum, a script should be included in the Dockerfile and executed via ``RUN`` that performs a basic sanity/smoke test of the image before the build is complete. This can be as simple as running noop versions of important commands (such as a ``--version`` flag) to ensure that they execute without error, or adding a sanity check command to your service.

Taken a step further, if at all possible, you should actually run containers from newly-built images before pushing them to a registry. This can be as simple as ensuring that the container starts up correctly, or running some basic network/functional tests against the service running in it. As a next step, you can run something like [serverspec](https://serverspec.org/) / [testinfra](https://testinfra.readthedocs.io/en/latest/) / [goss](https://github.com/aelsabbahy/goss) against the container to verify the state of files, services, processes, listening ports, etc. Ideally, you should also run your application's test suite (what I'd usually call "acceptance tests"), or a representative subset of it, against the container.

## Updates, Rollbacks, Issue Reproduction, and Disaster Recovery

In general, assuming the service inside an image is designed correctly, deploying an update should be as simple as pulling and running a newer tag of the same image. Ideally, the service inside the container is written to gracefully handle both upgrades and downgrades (if applicable). This allows our deployment/update and rollback plan to be the same: just stop the container that's currently running, and start one of the unique tag that we want<sup>[1](#foot1)</sup><a name="foot1source"></a>. Some orchestration is required when running multiple instances of a service, but the overall concept remains the same: aside from the data we store or pass in (i.e. environment variables, volume mounts, and any external stores such as databases), we should be able to completely and identically recreate a previous state by running the previous tag of the image.

Since a Docker image is an immutable artifact with a unique identifier (tag), we can run a given image on any other system at any time in the future. This has very significant benefits for troubleshooting (issue reproduction) as well as disaster recovery. So long as we capture the state of all external data before changing the running image (i.e. dump databases, back up any filesystems mounted into the container), it should be possible to recreate a functionally identical system and state at any point in the future. Deploy an upgrade to production and find some really hard-to-troubleshoot bug? Just restore your backups (sanitized of any sensitive data, of course) to a test environment, run the same tag of your image with adjusted configuration, and reproduce the bug safely<sup>[2](#foot2)</sup><a name="foot2source"></a>.

Similarly, in a disaster recovery context, all we need to do is have a record of how our container was started/run (you're using some sort of configuration management for this, right?) and a backup of any volumes that it uses. If the machine it's running on catches fire, or gets deleted, two years from now... just restore the backed-up volumes, and pull and run the container the same way you did before. You should end up with an identical system.

## Automated Builds

Finally, while some may disagree, I'm a staunch advocate that ``docker build`` should _never_ be directly executed by a human. It is virtually impossible to follow the other guidance here reliably - especially when it comes to tags and labels - by building a ``docker build`` command by hand. Ideally, all builds will be handled by an automated system, which could be anything from Docker Hub automated builds to Jenkins or another CI system, to a shell script. At times, I've gone so far as to add a required ``ARG never_build_manually`` to the Dockerfile to make this clear. For local development a ``local_build.sh`` script can be added to the repository, which sets tags and labels appropriately to ensure that if the image is pushed to a registry it's clearly identified as a local development build.

Enforcing that only automated builds are considered "real" builds ensures that the above points - especially repeatability, proper tagging and labeling, and full testing - are always in place for each image.

# Docker Image Checklist

1. Your Dockerfile follows the [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/), and your service is as close to a [12 factor app](https://12factor.net/) as possible.
1. Your image/container [only runs one service](#what-to-put-in-an-image), ideally without any sort of init subsystem.
1. Your image takes its [configuration](#configuration) via environment variables, or if need be, via config files mounted into the running container (with sane defaults provided).
1. In no circumstances do you build different images for different environments or deployment scenarios.
1. The service running in your images [logs](#logging) to STDOUT/STDERR, to be handled by the Docker daemon, and not to files on disk. Ideally, out and err have some logical separation.
1. Your image is [tagged](#tagging-and-versioning) with both a unique/immutable tag per image as well as relevant version tags (ideally following semver, and allowing use of major or major.minor images). All images should be able to be referenced by a unique tag, for all time to come.
1. For released software or open-source projects, the ``latest`` tag points to the most recent stable release.
1. Within the constraints of base images, OS packages, etc. any given image is [repeatable](#repeatable-builds) and can be rebuilt from source control at any point in the future.
1. When run as a container, your image does not [download dependencies at runtime](#no-runtime-downloads). The image should include everything (except data) required to work.
1. Everything needed to build the image (aside from external artifacts) is [included in source control](#everything-in-source-control-git), and versioned along with the Dockerfile. It is possible to tie an image to the commit / source state that it was generated from, and to tie a tag/release in source control to the corresponding image.
1. Your image makes use of [labels](#labels) on the image to store metadata about it, its contents, and the build process.
1. Your image includes a [healthcheck](#add-a-healthcheck) so that the Docker daemon can tell if containers are in a healthy, functional state.
1. The process for building your image includes running [tests](#testing-built-images) against it, and ideally also against a running container.
1. Data used by your image is isolated in volumes, so that users can [roll back and forward, reproduce issues, and perform disaster recovery](#updates-rollbacks-issue-reproduction-and-disaster-recovery) via tags.
1. The process for building your image is [automated](#automated-builds), and manually/locally built images are easily identified as development / non-release artifacts.

## Footnotes

<a name="foot1">1</a>: This is a gross simplification, describing a lab or desktop environment or the most trivial and unimportant service. For anything else, even in the lowest environments, you'd most likely have multiple containers running of the same service, and would use a zero-downtime deployment method such as blue/green or progressive traffic shifting. But at an extremely high level, the idea is the same: that you can roll backwards and forwards through container versions. [back to source](#foot1source)

<a name="foot2">2</a>: I'll admit that this is rather optimistic, and makes a lot of assumptions. This may end up being _much_ more complicated than "just restore your backups and run it in test", but it's still much simpler than what this process looked like a decade ago. [back to source](#foot2source)
