#!/bin/bash

if [ ! "$(basename $PWD)" == 'libtiff' ]
then
    echo FAIL
    exit 1
fi

. $(dirname $0)/envs.sh

# The ManyBugs repo compiles libtiff for 32-bit
export CFLAGS="-m32 $CFLAGS"
export LDFLAGS="-m32 $LDFLAGS"
export CXXFLAGS="-m32 $CXXFLAGS"

./configure &>configure.log
