#!/bin/bash

function quit()
{
    [ -z $1 ] && echo 'Error!' || echo $1
    exit
}

# Get wireshark ready for make
echo Cleaning... && make clean || quit
printf "all: ;\nclean: ;" > doc/Makefile
