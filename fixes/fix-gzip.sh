#!/bin/bash

# Fix errors in gzip. Meant to be run inside the gzip project root (gzip-bug-$version/gzip).
if [ ! "$(basename $PWD)" == 'gzip' ]
then
    echo FAIL
    exit 1
fi

replace_macros=`grep -Rl --include '*.c' -e '_IO_ftrylockfile' -e '_IO_ferror_unlocked' lib`
echo "Replacing _IO_ftrylockfile and _IO_ferror_unlocked..."
for f in $replace_macros
do
    sed -i.bak -e 's/_IO_ftrylockfile/_IO_EOF_SEEN/g' -e 's/_IO_ferror_unlocked/_IO_EOF_SEEN/g' $f
done

echo "Adding #define _IO_IN_BACKUP 0x100 to lib/stdio.in.h..."
if ! grep -q '#define _IO_IN_BACKUP 0x100' lib/stdio.in.h
then
    echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio.in.h || quit
fi

echo "Disabling _GL_WARN_ON_USE (gets... in lib/stdio.h..."
sed -i.bak 's@^#undef gets@//#undef gets@g' lib/stdio.in.h || quit
sed -i.bak 's@^_GL_WARN_ON_USE (gets@//_GL_WARN_ON_USE (gets@g' lib/stdio.in.h || quit
