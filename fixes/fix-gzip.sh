#!/bin/bash

# Fix errors in gzip. Meant to be run inside the gzip project root (gzip-bug-$version/gzip).

function quit()
{
    if [ -z "$1" ]
    then
        echo 'Error!'
    else
        echo $1
    fi
    exit 1
}

function fix_it()
{
    replace_macros="$(grep -Rl --include '*.c' -e '_IO_ftrylockfile' -e '_IO_ferror_unlocked' lib)"
    echo "Replacing _IO_ftrylockfile and _IO_ferror_unlocked in $replace_macros..."
    for f in $replace_macros
    do
        sed -i.bak -e 's/_IO_ftrylockfile/_IO_EOF_SEEN/g' -e 's/_IO_ferror_unlocked/_IO_EOF_SEEN/g' $f || quit
    done

    echo "Adding #define _IO_IN_BACKUP 0x100 to lib/stdio.h..."
    if ! grep -q '#define _IO_IN_BACKUP 0x100' lib/stdio.h
    then
        echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio.h || quit
    fi

    echo "Disabling _GL_WARN_ON_USE (gets... in lib/stdio.h..."
    sed -i.bak 's@^#undef gets@//#undef gets@g' lib/stdio.h || quit
    sed -i.bak 's@^_GL_WARN_ON_USE (gets@//_GL_WARN_ON_USE (gets@g' lib/stdio.h || quit

    # https://lists.gnu.org/archive/html/bug-gzip/2010-10/msg00004.html
    sed -i.bak 's@if (gl_futimens (ofd, ofname, timespec)@if (/*gl_futimens (ofd, ofname, timespec)*/0@g' gzip.c || quit
}

if [ ! -d lib ] || [ ! -f gzip.c ]
then
    echo 'Meant to be run inside the gzip project root (gzip-bug-$version/gzip).'
    exit
fi

#echo Running ./configure...
echo Running make clean...
make clean || quit "ERROR running make clean!"
echo Running make and fixing library problems...
./configure
make &>/dev/null || fix_it

echo "Now we're cookin. Ready to run 'make'!"
