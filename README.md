# ManyBugs scripts

Utility scripts written by Benjamin Steenhoek to work with the ManyBugs benchmark on a host machine (sans Docker).

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
