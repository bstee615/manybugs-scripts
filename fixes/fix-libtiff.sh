#!/bin/bash

# Fix errors in gzip. Meant to be run inside the gzip project root (gzip-bug-$version/gzip).
if [ ! "$(basename $PWD)" == 'libtiff' ]
then
    echo FAIL
    exit 1
fi

git checkout $(cat ../bug-info/bugged-program.txt)

# Gets libtiff ready for configure
echo Fixing test/Makefile.in...
sed -i.bak 's/^@am__EXEEXT_TRUE@\t/@am__EXEEXT_TRUE@:\t/g' test/Makefile.in
