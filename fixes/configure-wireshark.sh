#!/bin/bash
if [ ! "$(basename $PWD)" == 'wireshark' ]
then
    echo FAIL
    exit 1
fi

. $(dirname $0)/envs.sh

# This aliases python to python2
python() {
    /usr/bin/python2 "$@"
}
export -f python

make distclean &>/dev/null
./autogen.sh &>/dev/null
./configure --disable-warnings-as-errors PYTHON=/usr/bin/python2 &>/dev/null
