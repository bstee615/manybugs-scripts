#!/bin/bash

# Get a new system ready to build these benchmarks.
# This only installs the most recent/general packages.
# Special case libraries (like old versions of glib) will usually be installed from source
# to prevent interrupting other users' service.

sudo yum groupinstall -y "Development tools"
sudo yum install -y epel-release dnf-plugins-core
sudo yum config-manager --set-enabled powertools

# Install all dependencies for ManyBugs listed in deps.txt (except comments)
sudo yum install -y $(grep -v '^#' $(dirname $0)/deps.txt)

# Install glibconfig.h
# sudo cp /usr/lib64/glib-2.0/include/glibconfig.h /usr/include/glib-2.0/glibconfig.h
