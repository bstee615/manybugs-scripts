#!/bin/bash

patch -p1 -f < $(dirname $0)/wireshark/doc.patch
svn upgrade
svn revert $(cat ../bug-info/bugged-program.txt)
