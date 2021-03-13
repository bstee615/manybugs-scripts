#!/bin/bash
# Fix errors in gzip. Meant to be run inside the gzip project root (gzip-bug-$version/gzip).

. $(basename $0)/envs.sh

export CFLAGS="-m32 $CFLAGS"
export LDFLAGS="-m32 $LDFLAGS"
export CXXFLAGS="-m32 $CXXFLAGS"

make distclean
./configure
