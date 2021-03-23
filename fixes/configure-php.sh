#!/bin/bash

if [ ! "$(basename $PWD)" == 'php' ]
then
    echo FAIL
    exit 1
fi

. $(dirname $0)/envs.sh

./buildconf &>buildconf.log
./configure &>configure.log
