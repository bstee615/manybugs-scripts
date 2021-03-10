# ManyBugs scripts

Utility scripts written by Benjamin Steenhoek to work with the ManyBugs benchmark on a host machine (sans Docker).
They are meant to compile the benchmark programs on a CentOS 8 VM.

`install-deps.sh`: Install using `yum` all the dependencies needed to build the benchmarks.

## `/fixes/` folder

This contains scripts to configure and fix problems with building the benchmarks.
All are meant to be run inside the benchmark's project root, and directly modify the project files.

`configure-XXX.sh` configures the benchmark with the correct options. Notably `-g -O0`.
`fix-XXX.sh` applies patches to the benchmark to fix issues that arise from building with a modern toolchain.

## `/scripts/` folder

`dl.py`: Download ManyBugs scenarios into /bugs as .tar.gz's.
Example: `cat predicted-buggy.txt | ./dl.py`
`tar.py`: Unpack scenarios into /scenarios.
`repo.py`: Clone scenarios' code from the original repo.
This is necessary because the ManyBugs benchmarks have coverage instrumentation sprayed all up in them.
`cp.py`: Copy source files from the repo to the benchmark scenario.
