from pathlib import Path
import pandas as pd
import subprocess
from dl import download
import shutil

df_tsv = Path('notes.tsv')
df = pd.read_csv(df_tsv, delimiter='\t')
# print(df)

FUNCTIONAL_BASE = Path('functional')
assert(FUNCTIONAL_BASE.is_dir())

def unzip(bugs, gz_base, dst_base):
    for bug in bugs:
        if (dst_base / bug).is_dir():
            print(bug, 'already present')
        else:
            subprocess.check_call(['tar', 'zxf', (gz_base / bug).with_suffix('.tar.gz'), '-C', dst_base])

bugs = list(df['Bug'])

TAR_GZ_BASE = download(bugs)
assert(TAR_GZ_BASE.is_dir())
unzip(bugs, TAR_GZ_BASE, FUNCTIONAL_BASE)

for bug in bugs:
    base = FUNCTIONAL_BASE / bug
    projectname = bug.split('-')[0]
    project = base / projectname

    assert (base.is_dir() and project.is_dir())

    is_reset = base / 'is_reset'
    if is_reset.is_file():
        print(bug, 'already reset')
    else:
        if (project / '.git').is_dir():
            subprocess.check_call(['git', 'reset', '--hard'], cwd=project)

        if (project / '.hg').is_dir():
            subprocess.check_call(['hg', 'revert', '--all'], cwd=project)

        if (base / 'diffs').is_dir():
            diffs = base / 'diffs'
            rev_name = bug.split('-')[-2]
            for c in diffs.glob(f'**/*.c-{rev_name}'):
                rpath = c.relative_to(diffs)
                dst = project / rpath.with_suffix('.c')
                assert(dst.is_file())
                shutil.copy(c, dst)
    
        is_reset.touch()
