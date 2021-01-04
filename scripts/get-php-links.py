from pathlib import Path
import mechanize
import shutil
from time import sleep
import os

# Load all links for php bugs
b = mechanize.Browser()
b.open('https://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/')
for link in b.links():
    if 'php' in link.text:
        print(link.url.split('.')[0])

