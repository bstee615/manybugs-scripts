#!/bin/bash
source "$(dirname $0)/common.sh"

if [ ! -d lib ] || [ ! -f gzip.c ]
then
    echo 'Meant to be run inside the gzip project root (gzip-bug-$version/gzip).'
    exit
fi

cat ../../../libxml.patch | patch -p0 || quit
./configure || quit
make clean || quit
