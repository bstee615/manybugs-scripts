#!/bin/bash

function quit()
{
    [ -z $1 ] && echo 'Error!' || echo $1
    exit
}

# Get wireshark ready for make
echo Cleaning... && make clean || quit
echo Fixing autogen.sh... && sed -i.bak 's@^python@/bin/python2@g' ./autogen.sh || quit
echo Running autogen.sh... && ./autogen.sh || quit
echo 'Configuring (with -Wno-error)...' && CFLAGS=-Wno-error ./configure || quit
printf "all: ;\nclean: ;" > doc/Makefile
