#!/bin/bash
. $(basename $0)/envs.sh
sed -i.bak 's@^python@/bin/python2@g' ./autogen.sh || exit 1
./autogen.sh || exit 1
CFLAGS=-Wno-error ./configure || exit 1
