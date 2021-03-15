#!/bin/bash
# Usage: prep.sh <test-command> <scripts-dir e.g. manybugs-scripts/scripts> <base-dir outside of the bug name e.g. manybugs-scripts/scenarios/ which contains php-bug-XXX-YYY>
# Prepares a scenario for debugging with GDB
# Not maintained

mkdir -p ../program-input

echo "$1" > ../program-input/run-test.sh
bash ../program-input/run-test.sh | tee ../program-input/run-test.sh.log

scriptsdir="$2"
basedir="$3"

pattern="s@/root/mountpoint-genprog/genprog-many-bugs@$basedir@g"
bash -x $1 2>&1 | grep '+ ' | sed 's@+ @@g' | sed $pattern > ../program-input/run.sh
bash ../program-input/run.sh | tee ../program-input/run.sh.log
bash -x $1 2>&1 | grep '+ ' | sed "s@+ @gdb -x $scriptsdir/run.sh.gdb --args @g" | sed $pattern > ../program-input/run-gdb.sh

