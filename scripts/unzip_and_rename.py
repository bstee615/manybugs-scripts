"""
Unzip and rename all the bug scenarios in the given directory to this directory
"""

import subprocess
from pathlib import Path
import os
import sys

def unzip_and_rename(glob):
    root = Path.cwd()
    destroot = Path.cwd()
    zips = [z for z in root.glob(glob) if z.is_file()]
    for z in sorted(zips):
        bug_name = z.name.split('.')[0]
        
        # Prepare destination name
        program_name, *_, buggy, fixed = bug_name.split('-')
        new_name = destroot / program_name / f'{buggy}-{fixed}'
        if new_name.exists():
            print(new_name, 'already exists')
            continue

        if not Path(bug_name).exists():
            print(f'Unzipping {z}')
            subprocess.run(f'tar zxf {z}'.split(), check=True)

        # Rename unzipped folder
        print('renaming', bug_name, 'to', new_name)
        os.makedirs(program_name, exist_ok=True)
        os.rename(bug_name, new_name)

        # Save original folder name
        with open(new_name / 'bug-info' / 'original-name', 'w') as f:
            f.write(bug_name)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        glob = sys.argv[1]
    else:
        glob = '*-bug-*.tar.gz'
    unzip_and_rename(glob)
