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

./autogen.sh &>autogen.sh.log
./configure --disable-warnings-as-errors PYTHON=/usr/bin/python2 &>configure.log
