#!/bin/bash
# Fix errors in gzip. Meant to be run inside the gzip project root (gzip-bug-$version/gzip).
if [ ! "$(basename $PWD)" == 'gzip' ]
then
    echo FAIL
    exit 1
fi

. $(dirname $0)/envs.sh

export CFLAGS="-m32 $CFLAGS"
export LDFLAGS="-m32 $LDFLAGS"
export CXXFLAGS="-m32 $CXXFLAGS"

make distclean &>/dev/null
./configure &>/dev/null
