import json
import requests

import feedparser as fp

from dateutil.parser import parse
from time import gmtime, strftime

'''
  Default seems to be 10
'''
max_results = 100

arxiv_url = 'http://export.arxiv.org/api/query?search_query='
query=f'"CMS+Open+Data"&searchtype=all&source=header&max_results={max_results}'

results = requests.get(f'{arxiv_url}{query}')
feed = fp.parse(results.text)

entries = feed['entries']

papers = []
ofile = open('arxiv.json', 'w')

for e in entries:

    title = e.title
    abstract = e.summary
    date = str(parse(e.published).date())
    url = e.link
    doi = e.links[0].href
    authors = [a.name for a in e.authors]
    
    obj = {}

    obj['title'] = title
    obj['abstract'] = abstract
    obj['date'] = date
    obj['url'] = url
    obj['doi'] = doi
    obj['authors'] = authors
    
    papers.append(obj)

ofile.write(
    json.dumps(
        papers,
        sort_keys=True,
        indent=4
    )
)

ofile.close()
