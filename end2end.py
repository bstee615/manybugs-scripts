import csv
import pandas
from pathlib import Path

# End-to-end prepare all ManyBugs benchmarks

df = pandas.read_csv('versions.csv', header=0)
# print(df)

from .cp import cprepo
from .repos import checkout
from .dl import download
from .tar import unpack

bugsdir = download(list(df['name']))

for index, row in df.iterrows():
    try:
        projectdir = checkout(row['name'], row['vcs'], row['repo'], row['version'])
        scenariodir = unpack(row['name'], bugsdir)
        cprepo(projectdir, scenariodir)
    except Exception as ex:
        print('Failure!', ex)
