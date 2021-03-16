#!/bin/bash
# Run all tests

benchmark_name="$1"
option="$2"

for tester in $(find . -type f -name "$benchmark_name-run-tests.pl" -o -name "$benchmark_name-run-tests.sh" -o -name "$benchmark_name-run-tests")
do
    dir=`dirname $tester`
    project="$dir/$benchmark_name"
    tester_rel="../`basename $tester`"
    pushd $project &>/dev/null
        pwd

        if [ $option == 'all' ]
        then
            # Run all
            length=`$tester_rel length`
            echo $length tests
            for i in `seq $length`
            do
                $tester_rel $i
            done
        fi

        # Run buggy failed
        if [ $option == 'bug-failures' ]
        then
            for i in `cat ../bug-info/bug-failures`
            do
                $tester_rel $i
            done
        fi

        # Run buggy failed
        if [ $option == 'bug-failures' ]
        then
            for i in `cat ../bug-info/bug-failures`
            do
                $tester_rel $i
            done
        fi

        # Run those that should be fixed by the fixed version
        if [ $option == 'bug-fixed' ]
        then
            for i in `diff --new-line-format="" --unchanged-line-format="" ../bug-info/bug-failures ../bug-info/fix-failures`
            do
                $tester_rel $i
            done
        fi
    popd &>/dev/null
done