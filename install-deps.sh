#!/bin/bash

# Install all dependencies for ManyBugs listed in deps.txt (except comments)
sudo dnf install -y $(grep -v '^#' deps.txt)
