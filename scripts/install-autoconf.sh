#!/bin/bash
# Installs autoconf-2.13, needed for php.

root="$1"
if [ ! -d $root/vendor ]
then
	echo "Supply the root of the manybugs-scripts project to install autoconf 2.13."
	exit 1
fi

cd $root/vendor
if [ ! -f autoconf-2.13.tar.gz ]; then wget https://ftp.gnu.org/gnu/autoconf/autoconf-2.13.tar.gz; fi
tar zxf autoconf-2.13.tar.gz
cd $root/vendor/autoconf-2.13
./configure --prefix=$(realpath "$root/vendor/install") && make && make install

