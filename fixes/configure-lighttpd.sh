#!/bin/bash

if [ ! "$(basename $PWD)" == 'lighttpd' ]
then
    echo FAIL
    exit 1
fi

. $(dirname $0)/envs.sh

# https://github.com/squaresLab/ManyBugs/issues/9
./configure --with-ldap --with-bzip2 --with-openssl --with-gdbm --with-memcache --with-webdav-props --with-webdav-locks \
    &> configure.log
