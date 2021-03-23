#!/bin/python3
import requests
import json

with open('wireshark-cves.txt') as f:
    cve_ids = [c.strip() for c in f.readlines()]

store = 'wireshark-store.txt'
with open(store) as f:
    done = json.load(f)

try:
    for cve_id in sorted(cve_ids):
        if cve_id in done:
            cve_json = done[cve_id]
        else:
            url_fmt = 'https://cve.circl.lu/api/cve/{id}'
            url = url_fmt.format(id=cve_id)
            r = requests.get(url)
            cve_json = r.text
            done[cve_id] = cve_json

        cve_info = json.loads(cve_json)
        vuln = [p.split(':')[5] for p in cve_info["vulnerable_product"] if 'wireshark' in p]
        print(cve_id, ','.join(vuln))
finally:
    with open(store, 'w') as f:
        json.dump(done, f)
