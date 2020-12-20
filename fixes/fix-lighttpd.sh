patch -p0 < $(dirname $0)/response.c.patch
./configure
make clean
