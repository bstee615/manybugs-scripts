#!/bin/bash
. $(dirname $0)/envs.sh

# This aliases python to python2
python() {
    /usr/bin/python2 "$@"
}
export -f python

make distclean &>/dev/null
./autogen.sh &>/dev/null
./configure --disable-warnings-as-errors &>/dev/null
