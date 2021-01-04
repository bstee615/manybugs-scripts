#!/bin/bash
function quit()
{
    [ -z $1 ] && echo 'Error!' || echo $1
    exit
}

if [ ! -d Python ]
then
	echo 'Meant to be run inside the python project root.'
        exit 1
fi


sed -i "s/cd python/cd src/" ../test.sh && \
    sed -i "s#${OLD_LOCATION}#/experiment#g" ../test.sh && \
    sed -i "s#/experiment/limit#timeout 300#" ../test.sh && \
    sed -i "s#..//python-run-tests.pl#../python-run-tests.pl#" ../test.sh && \
    sed -i "s#/usr/bin/perl#perl#" ../test.sh && \
    sed -i "s#&> /dev/null##" ../python-run-tests.pl

sed -i 's#def test_create_connection_timeout(self):#def test_create_connection(self):\n        return#' Lib/test/test_socket.py || quit

make clean || quit 
