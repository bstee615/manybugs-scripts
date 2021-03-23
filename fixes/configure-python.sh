#!/bin/bash

if [ ! "$(basename $PWD)" == 'python' ]
then
    echo FAIL
    exit 1
fi

. $(dirname $0)/envs.sh

./configure &>configure.log
