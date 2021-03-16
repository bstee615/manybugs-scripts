if [ ! -f 'bug-info/original-name' ]
then
    echo FAIL
    exit 1
fi

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

# Fix occurrences of manybugs VM paths sprayed throughout the benchmark program
manybugs_dir="/root/mountpoint-genprog/genprog-many-bugs/$(cat bug-info/original-name)"
cp test.sh.back test.sh
if [ -f test.sh ]
then
    sed -i.back "s@$manybugs_dir@../@g" test.sh
fi

for b in `grep --include='*.back' -Rl $manybugs_dir`
do
    echo "Restoring $b"
    cp $b ${b%%.back}
done
for f in `grep --exclude='*.back' -Rl $manybugs_dir`
do
    echo "Replacing $f: $manybugs_dir -> $PWD"
    sed -i.back "s@$manybugs_dir@$PWD@g" $f
done
