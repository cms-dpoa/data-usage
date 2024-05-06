import json
import urllib.request
import io

from dateutil.parser import parse
from time import gmtime, strftime

def get_dataset(references):

    dois_referenced = []
    
    for r in references:
        if 'dois' in r['reference']:
            if '/OPENDATA.CMS' in r['reference']['dois'][0]:
                doi = r['reference']['dois'][0]
                dois_referenced.append(doi)

    return dois_referenced
                
inspire_url = 'https://inspirehep.net/api'

'''
Get the information on papers that contain 
CMS open data DOIs in the references
'''

record_type = 'literature'

search_query = 'q=references.reference.dois:10.7483/OPENDATA.CMS*'
sort_order = 's=mostrecent'
n_results = 'size=500'

query_string = f'{n_results}&{sort_order}&{search_query}'

query = f'{inspire_url}/{record_type}?{query_string}'

results = json.load(
    urllib.request.urlopen(query)
)

papers = []
ofile = open('inspire.json', 'w')

hits = results['hits']['hits']

for hi, hit in enumerate(hits):
    
    metadata = hit['metadata']
    
    title = metadata['titles'][0]['title']
    date = str(parse(hit['created']).date())
    hid = metadata['control_number']
    abstract = metadata['abstracts'][0]['value']
    authors = [a['full_name'] for a in metadata['authors']]

    dois_referenced = get_dataset(metadata['references'])
    
    try: 
        keywords = [m['value'] for m in metadata['keywords']]
    except KeyError:
        keywords = []
    
    try:
        doi = metadata['dois'][0]['value']
    except KeyError:
        doi = ''
        
    obj = {}

    obj['title'] = title
    obj['abstract'] = abstract
    obj['date'] = date
    obj['url'] = f'https://inspirehep.net/literature/{hid}'
    obj['doi'] = doi
    obj['authors'] = authors
    obj['keywords'] = keywords
    obj['dois_referenced'] = dois_referenced
    
    papers.append(obj)

ofile.write(
    json.dumps(
        papers,
        sort_keys=True,
        indent=4
    )
)

ofile.close()
