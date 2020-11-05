#!/bin/python3

# Copy all .c files from src to dst.
# This is necessary because the ManyBugs benchmarks have coverage instrumentation sprayed all up in them.

from pathlib import Path
import shutil
import sys

def cprepo(src, dst):
    cs = Path(src).glob('**/*.c')
    to_copy = {}
    for c in cs:
        print(f'{c}:', end='')
        dst_dir = dst / c.parent.relative_to(src)
        if not dst_dir.is_dir():
            print(f'parent directory {dst_dir} not present...')
            continue
        if 'lib/' not in str(c) and 'gnulib/' not in str(c) and '._bootmp' not in str(c):
            dst_file = dst_dir / c.name
            to_copy[c] = dst_file
            print(f'copying to {dst_file}...')
        else:
            print('skipping...')

    for srcf, dstf in to_copy.items():
        shutil.copy(srcf, dstf)
        pass

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} <src-root> <dst-root>')
        exit(1)
    else:
        src = Path(sys.argv[1])
        dst = Path(sys.argv[2])
        assert(src.is_dir())
        assert(dst.is_dir())
        cprepo(src, dst)
