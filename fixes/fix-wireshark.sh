#!/bin/bash
if [ ! "$(basename $PWD)" == 'wireshark' ]
then
    echo FAIL
    exit 1
fi

patch -p1 -f < $(dirname $0)/wireshark/doc.patch
patch -p0 -f < $(dirname $0)/wireshark/faq.py.patch
svn upgrade
svn revert $(cat ../bug-info/bugged-program.txt)
