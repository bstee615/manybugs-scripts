#!/bin/bash
# Find all executables of a given name and run with the given arguments.
# Used to test that we the programs we built run correctly.

exe_name=$1
args=$@

for exe in $(find . -executable -type f -name $exe_name)
do
    $exe $args &> /dev/null
    echo $exe exited $?
done