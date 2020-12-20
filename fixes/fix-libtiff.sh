#!/bin/bash

function quit()
{
    if [ -z $1 ]
    then
        echo 'Error!'
    else
        echo $1
    fi
    exit
}

# Gets libtiff ready for configure
echo Cleaning... && make clean &> /dev/null || quit
echo Configuring... && ./configure &> /dev/null || quit
echo Fixing test/Makefile... && sed -i.bak 's/^@am__EXEEXT_TRUE@\t/@am__EXEEXT_TRUE@:\t/g' test/Makefile || quit
echo Ready for make!
