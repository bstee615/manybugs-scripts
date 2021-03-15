#!/bin/bash
bugs_root=$(dirname ${BASH_SOURCE[0]})

PATH="$bugs_root/scripts:$PATH"
export PATH

PYTHONPATH="$bugs_root/scripts:$PYTHONPATH"
export PYTHONPATH
