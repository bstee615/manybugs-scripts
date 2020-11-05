# ManyBugs scripts

Utility scripts written by Benjamin Steenhoek to work with the ManyBugs benchmark on a host machine (sans Docker).

`dl.py`: Download ManyBugs scenarios into /bugs as .tar.gz's.
Example: `cat predicted-buggy.txt | ./dl.py`
`tar.py`: Unpack scenarios into /scenarios.
`repo.py`: Clone scenarios' code from the original repo.
This is necessary because the ManyBugs benchmarks have coverage instrumentation sprayed all up in them.
`cp.py`: Copy source files from the repo to the benchmark scenario.
