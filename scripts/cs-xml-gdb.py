#!/bin/python3
import xmltodict
from pathlib import Path

"""
Run in a scenario folder to parse the CodeSonar warning XML and print out GDB breakpoints
for the fault location and the function where the warning path starts
"""

for f in Path().glob('*.xml'):

    with f.open('r') as fd:
        root = xmltodict.parse(fd.read())

    warning = root['warning']

    print(f"b {Path(warning['@filename']).name}:{warning['@line_number']}")
    print(f"b {warning['@start_procedure']}")

