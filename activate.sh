#!/bin/bash
bugs_root=$(realpath $(dirname ${BASH_SOURCE[0]}))

PATH="$bugs_root/scripts:$PATH"
PATH="$bugs_root/fixes:$PATH"
export PATH

PYTHONPATH="$bugs_root/scripts:$PYTHONPATH"
export PYTHONPATH
