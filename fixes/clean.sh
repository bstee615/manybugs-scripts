rm -rf fixed-program.txt \
    *.cache \
    *~ \
    compile.pl \
    coverage.* \
    coverage \
    configuration-* \
    sanity \
    preprocessed \
    *debug* \
    tests \
    local-root \
    fixed \
    .Indicator_Makefiles \
    repair.debug.0
mv fix-failures bug-info
mv bug-failures bug-info
mv fix.lines bug-info
mv fault.lines bug-info
mv bugged-program.txt bug-info

cp test.sh.back test.sh
if [ -d test.sh ]
then
    sed -i.back "s@/root/mountpoint-genprog/genprog-many-bugs/$(cat bug-info/original-name)/@../@g" test.sh
fi
