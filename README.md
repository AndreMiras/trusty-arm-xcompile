# README

## Overview
Easily cross compile Debian packages for ARM in an isolated environment using Docker.

## Build
    docker build --tag=xcompile .

## Run
To cross compile a package, simply provide the package name to the --xcompile argument, e.g. cppunit.

    docker run --volume /tmp/shared:/shared xcompile --xcompile cppunit

## Consume
Freshly cross compiled deb archives will be available in the host computer /tmp/shared/ directory.

    ls /tmp/shared/
    -> libcppunit-1.13-0_1.13.1-2ubuntu1_armel.deb  libcppunit-dev_1.13.1-2ubuntu1_armel.deb  libcppunit-doc_1.13.1-2ubuntu1_all.deb

Inspect and install them using dpkg.

    dpkg --contents libcppunit-1.13-0_*_armel.deb
    sudo dpkg --install --force-architecture --path-exclude=/usr/share/* --path-exclude=/usr/include/* --path-exclude=/usr/bin/* libcppunit-dev_*_armel.deb

## Motivations
I needed such a tool because I'm still using ARM devices without Hard Float support even though Ubuntu dropped the armel arch.
