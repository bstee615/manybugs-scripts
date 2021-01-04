#!/bin/bash
patch -p0 < $(dirname $0)/lighttp/response.c.patch
make clean
