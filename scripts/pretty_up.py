import subprocess
from pathlib import Path
import re
import sys

def pretty_up(root):
    print(f'Cleaning, fixing, configuring, and building {root}')

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

    subprocess.run(['bash', clean_sh.absolute()], cwd=root.absolute())
    subprocess.run(['bash', fix_sh.absolute()], cwd=(root / bugname).absolute())
    subprocess.run(['bash', configure_sh.absolute()], cwd=(root / bugname).absolute())
    subprocess.run(['make'], cwd=(root / bugname).absolute())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        glob = sys.argv[1]
        roots = Path.cwd().glob(glob)
    else:
        roots = [Path.cwd()]
    for root in roots:
        pretty_up(root)
