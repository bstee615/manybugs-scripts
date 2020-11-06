#!/bin/bash

function quit()
{
    if [ -z $1 ]
    then
        echo 'Error!'
    else
        echo $1
    fi
    exit
}
