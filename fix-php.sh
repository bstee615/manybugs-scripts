#!/bin/bash
source "$(dirname $0)/common.sh"

if [ ! -f php.gif ]
then
    echo 'Meant to be run inside the php project root (php-bug-$version/php).'
    exit 1
fi

cp ../../../README.GIT-RULES .
cat ../../../libxml.patch | patch -p0 --forward
./configure || quit
make clean || quit
