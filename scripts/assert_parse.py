import re
import os
import pandas
import shutil
import subprocess

'''
Parse Xueyuan's human readable assertions
'''

def parse(dirname, assertion):
    dirname = os.path.abspath(dirname)
    m = re.match(r'([^,]+),\s*(before|after)\s*line\s*([0-9]+).*(assert\(.*\);)', assertion)
    file_path = os.path.join(dirname, m.group(1))
    before_after = m.group(2)
    line_no = m.group(3)
    assert_stmt = m.group(4)
    assert_stmt = assert_stmt.replace('assert', '''#define my_assert(c) if (c) {} else{*((int*)0) = 0;}
    my_assert''')

    print(before_after, f'{file_path}:{line_no}')
    print()
    print(assert_stmt)
    print()

df = pandas.read_csv('notes.tsv', sep='\t')

for i, row in df.iterrows():
    name = row['Name']
    bug = row['Bug']
    buggy_version = bug.split('-')[-2]
    assertion = row['Assert']

    dirname = os.path.join('functional', bug)

    # Copy to buggy folder
    buggy_dirname = os.path.join(dirname, f'buggy.{buggy_version}')
    if not os.path.isdir(buggy_dirname):
        src_dirname = os.path.join(dirname, name)
        try:
            print('copying', src_dirname, 'to', buggy_dirname)
            shutil.copytree(src_dirname, buggy_dirname)
        except:
            print('error, trying cp -r')
            subprocess.check_call(args=['cp', '-r', src_dirname, buggy_dirname])

    parse(buggy_dirname, assertion)
