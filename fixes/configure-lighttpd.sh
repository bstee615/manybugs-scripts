#!/bin/bash
# https://github.com/squaresLab/ManyBugs/issues/9
PKG_CONFIG_PATH="/usr/lib64/pkgconfig" ./configure --with-ldap --with-bzip2 --with-openssl --with-gdbm --with-memcache --with-webdav-props --with-webdav-locks
