#!/bin/python3
import subprocess
from pathlib import Path
import re
import sys

def pretty_up(root, steps):
    print(f'Prettying up {root}')
    # Gather variables and sanity check
    original_name_file = root / 'bug-info' / 'original-name'
    assert original_name_file.exists()
    with open(original_name_file) as f:
        original_bugname = f.read()
    bugname = re.match(r'(.*)-bug-.*', original_bugname).group(1)

    # Find processing scripts
    scripts_dir = Path(__file__).parent
    fixes_dir = scripts_dir.parent / 'fixes'

    clean_sh = fixes_dir / 'clean.sh'
    assert clean_sh.exists()
    fix_sh = fixes_dir / f'fix-{bugname}.sh'
    assert fix_sh.exists()
    configure_sh = fixes_dir / f'configure-{bugname}.sh'
    assert configure_sh.exists()

    bug_root = root / bugname

    if 'clean' in steps:
        print('Cleaning...')
        with open(root / "clean.log", "w") as f:
            subprocess.run(['bash', clean_sh.absolute()], cwd=root.absolute(), stdout=f, stderr=subprocess.STDOUT, check=True)
    if 'fix' in steps:
        print('Fixing...')
        with open(root / "fix.log", "w") as f:
            subprocess.run(['bash', fix_sh.absolute()], cwd=bug_root.absolute(), stdout=f, stderr=subprocess.STDOUT, check=True)
    if 'configure' in steps:
        print('Configuring...')
        subprocess.run(['bash', configure_sh.absolute()], cwd=bug_root.absolute(), check=True)
    if 'build' in steps:
        print('Building...')
        with open(bug_root / "make.log", "w") as f:
            subprocess.run(['make', '-j', '4'], cwd=bug_root.absolute(), stdout=f, stderr=subprocess.STDOUT, shell=True, check=True)

if __name__ == '__main__':
    default_steps = 'clean,fix,configure,build'.split(',')
    steps = default_steps
    if len(sys.argv) > 1:
        glob = sys.argv[1]
        roots = Path.cwd().glob(glob)
        if len(sys.argv) > 2:
            steps = sys.argv[2].split(',')
            if any(s not in default_steps for s in steps):
                print(f'Usage: {sys.argv[0]} <glob> [instructions]. instructions is a comma-delimited list containing any of {",".join(default_steps)}.')
    else:
        roots = [Path.cwd()]
    for root in sorted(roots):
        pretty_up(root, steps)
