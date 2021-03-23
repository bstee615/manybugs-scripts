#!/bin/bash

if [ ! "$(basename $PWD)" == 'lighttpd' ]
then
    echo FAIL
    exit 1
fi

cp -f $(dirname $0)/lighttpd/mod-cgi.t ./tests/mod-cgi.t
patch -p0 < $(dirname $0)/lighttpd/response.c.patch

svn upgrade
svn revert $(cat ../bug-info/bugged-program.txt)
