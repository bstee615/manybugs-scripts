# ManyBugs scripts

Utility scripts written by Benjamin Steenhoek to work with the ManyBugs benchmark on a host machine (sans Docker).
They are meant to compile the benchmark programs on a CentOS 8 VM.

`install-deps.sh`: Install using `yum` all the dependencies needed to build the benchmarks.

## `/fixes/` folder

This contains scripts to configure and fix problems with building the benchmarks.
All are meant to be run inside the benchmark's project root, and directly modify the project files.

`configure-XXX.sh` configures the benchmark with the correct options. Notably `-g -O0`.

`fix-XXX.sh` applies patches to the benchmark to fix issues that arise from building with a modern toolchain.
These fixes are adapted from the Dockerfiles included with the [ManyBugs](https://github.com/squaresLab/ManyBugs) bugzoo repo.

## `/scripts/` folder

`activate.sh` adds `scripts/` to your `PYTHONPATH` so that you can import scripts between eachother freely.

## Useful scripts in `scripts/`
`dl.py <bugname>`: Download bug scenarios into /bugs as .tar.gz's.
`dl_multiple.py <bugname-regex>`: Download multiple scenarios by a regex matching the bug name.
`unzip_and_rename.py [glob]`: Unzip scenarios and rename them to a friendlier name. Default unzips all .tar.gz's in the current directory.
`pretty_up.py <glob>`: Clean, fix, configure, and build bugs.
`test-exes.sh <program-name> <args>`: Test executables with a given name using args

## Old scripts in `scripts/`
`tar.py`: Unpack scenarios into /scenarios.
`repo.py`: Clone scenarios' code from the original repo.
This is necessary because the ManyBugs benchmarks have coverage instrumentation sprayed all up in them.
`cp.py`: Copy source files from the repo to the benchmark scenario.

## Example flow for downloading ManyBugs

```
source activate.sh
mkdir bugs
cd bugs
python ../scripts/dl_multiple.py 'gzip|wireshark'
python ../scripts/unzip_and_rename.py
python ../scripts/pretty_up.py 'gzip/*'
bash ../scripts/test-exes.sh gzip -h
```
