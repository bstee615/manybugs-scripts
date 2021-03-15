#!/bin/bash

# Install all dependencies for ManyBugs listed in deps.txt (except comments)
sudo dnf install -y $(grep -v '^#' $(dirname $0)/deps.txt)

# Install glibconfig.h
sudo cp /usr/lib64/glib-2.0/include/glibconfig.h /usr/include/glib-2.0/glibconfig.h
