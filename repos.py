from pathlib import Path
import shutil
import subprocess

repos = Path('repos')
if not repos.is_dir():
    repos.mkdir()

def checkout(name, vcs, repo, version):
    print(f'Checking out {repo}@{version} with {vcs}...')

    projectdir = Path(repos) / name
    if projectdir.is_dir():
        print('Already checked out.')
        shutil.rmtree(projectdir)
    projectdir.mkdir()

    if vcs == 'git':
        subprocess.call(['git', 'clone', repo, str(projectdir)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        subprocess.call(['git', 'checkout', version], cwd=projectdir,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    elif vcs == 'svn':
        subprocess.call(['svn', 'checkout', f'{repo}@{version}', str(projectdir)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    elif vcs == 'mercurial':
        subprocess.call(['hg', 'clone', repo, str(projectdir)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        subprocess.call(['hg', 'update', '-r', version], cwd=projectdir,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    else:
        raise Exception(f'ERROR: unrecognized VCS {vcs} on for {name}')

    assert(projectdir.is_dir())

    return projectdir
