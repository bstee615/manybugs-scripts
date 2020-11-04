import mechanize
from time import sleep

b = mechanize.Browser()

b.open('https://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/')
page = b.response().read()
files = []
for link in b.links():
    if '.tar.gz' in str(link):
        print(link, 'added')
        files.append(link)

for link in files:
    sleep(1)
    with open(link.url.split('/')[-1], 'wb') as f:
        b.click_link(link)
        f.write(b.response().read())
        print(link.text, 'downloaded')
