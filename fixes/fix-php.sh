#!/bin/bash

function quit()
{
    [ -z $1 ] && echo 'Error!' || echo $1
    exit
}

if [ ! -f php.gif ]
then
    echo 'Meant to be run inside the php project root (php-bug-$version/php).'
    exit 1
fi

cp $(dirname $0)/README.GIT-RULES .
cat $(dirname $0)/libxml.patch | patch -p0 --forward
./configure || quit
make clean || quit
