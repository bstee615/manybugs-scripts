from pathlib import Path
import subprocess

# Unpack scenarios into scenarios directory

scenarios = Path('scenarios')
if not scenarios.is_dir():
    scenarios.mkdir()

def unpack(name, bugsdir):
    subprocess.call(['tar', '-zxf', str(bugsdir / name) + '.tar.gz', '-C', scenarios], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    dst = scenarios / name
    assert(dst.is_dir())
    projectroot = dst / name.split('-')[0]
    assert(projectroot.is_dir())
    return projectroot
