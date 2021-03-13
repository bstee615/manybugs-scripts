from dl_multiple import dl_multiple
from unzip_and_rename import unzip_and_rename
from pretty_up import pretty_up
import subprocess
from pathlib import Path

def do_it_all(name):
    dl_multiple(name)
    unzip_and_rename(f'{name}*')
    for root in Path.cwd().glob(f'{name}/*'):
        pretty_up(root)
    test_exes_sh = Path(__file__) / 'test-exes.sh'
    subprocess.run(str(test_exes_sh), shell=True)

if __name__ == '__main__':
    do_it_all('wireshark')
