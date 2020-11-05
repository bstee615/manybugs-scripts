#!/bin/bash

scenario_directory="$1"
bug_name="$2"
project_name="$(echo $bug_name | cut -d '-' -f 1)"
project_directory="$scenario_directory/$bug_name/$project_name"

if [ -z $bug_name ] || [ ! -d $scenario_directory ] || [ ! -d $project_directory ]
then
    echo "Usage: $0 <scenario_directory> <bug_name>"
    exit
fi

codesonar analyze $project_directory -project "/benjis/manybugs/$bug_name" make -C $project_directory
