make clean
sed -i.bak -e 's/^AM_C_PROTOTYPES/dnl AM_C_PROTOTYPES/g' -e 's/^AM_INIT_AUTOMAKE/dnl AM_INIT_AUTOMAKE/g' configure.in