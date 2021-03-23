#!/bin/python3
"""
Unzip and rename all the bug scenarios in the given directory to this directory
"""

import subprocess
from pathlib import Path
import os
import sys
import shutil

script_dir = Path(__file__).parent
fix_dir = script_dir.parent / 'fixes'

def unzip_and_rename(glob, root, dest_root):
    zips = [z for z in root.glob(glob) if z.is_file()]
    for z in sorted(zips):
        bug_name = z.name.split('.')[0]
        
        # Prepare destination name
        program_name, *_, buggy, fixed = bug_name.split('-')
        new_name = dest_root / program_name / f'{buggy}-{fixed}'

        if not Path(bug_name).exists() and not new_name.exists():
            print(f'Unzipping {z}')
            subprocess.run(f'tar zxf {z}'.split(), check=True)

        # Rename unzipped folder
        if not new_name.exists():
            print('renaming', bug_name, 'to', new_name)
            os.makedirs(program_name, exist_ok=True)
            os.rename(bug_name, new_name)

        # Save original folder name
        bug_info = new_name / 'bug-info'
        if not bug_info.exists():
            bug_info.mkdir()
        original_name = new_name / 'bug-info' / 'original-name'
        if not original_name.exists():
            with open(original_name, 'w') as f:
                f.write(bug_name)

        # Copy fix scripts
        # scripts = [
        #     fix_dir / f'clean.sh',
        #     fix_dir / f'fix-{program_name}.sh',
        #     fix_dir / f'configure-{program_name}.sh',
        # ]
        # for s in scripts:
        #     assert s.exists(), f'{s} does not exist'
        #     d = new_name / s.name
        #     if not d.exists():
        #         shutil.copyfile(s, d)

if __name__ == '__main__':
    root = Path.cwd()
    dest_root = Path.cwd()
    if len(sys.argv) > 1:
        glob = sys.argv[1]
    else:
        glob = '*-bug-*.tar.gz'
    if len(sys.argv) > 2:
        root = Path(sys.argv[2])
    if len(sys.argv) > 3:
        dest_root = Path(sys.argv[3])
    print(glob, root, dest_root)
    unzip_and_rename(glob, root, dest_root)
