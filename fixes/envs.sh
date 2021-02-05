#!/bin/bash
# Export environment variables for configure to enable debugging and fix linker errors
export LD_LIBRARY_PATH="/usr/lib64:$LD_LIBRARY_PATH"
export CFLAGS="-g -O0"