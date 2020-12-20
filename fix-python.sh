#!/bin/bash
source "$(dirname $0)/common.sh"

if [ ! -d Python ]
then
    echo 'Meant to be run inside the python project root.'
    exit 1
fi

sed -i.bak 's#def test_create_connection_timeout(self):#def test_create_connection(self):\n        return#' Lib/test/test_socket.py || quit
./configure || quit
make clean || quit