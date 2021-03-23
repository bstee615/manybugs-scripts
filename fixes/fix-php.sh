#!/bin/bash

if [ ! "$(basename $PWD)" == 'php' ]
then
    echo FAIL
    exit 1
fi

git checkout $(cat ../bug-info/bugged-program.txt)

cp $(dirname $0)/php/README.GIT-RULES .
cat $(dirname $0)/php/libxml.patch | patch -p0 -f --forward

exit 0
