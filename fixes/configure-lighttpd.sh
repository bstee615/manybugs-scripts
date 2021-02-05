#!/bin/bash
. $(basename $0)/envs.sh
# https://github.com/squaresLab/ManyBugs/issues/9
./configure --with-ldap --with-bzip2 --with-openssl --with-gdbm --with-memcache --with-webdav-props --with-webdav-locks
