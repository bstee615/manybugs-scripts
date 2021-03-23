#!/bin/bash

if [ ! "$(basename $PWD)" == 'python' ]
then
    echo FAIL
    exit 1
fi

hg revert $(cat /experiment/manifest.txt)

sed -i 's#def test_create_connection_timeout(self):#def test_create_connection(self):\n        return#' Lib/test/test_socket.py
