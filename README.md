# data-usage
[![DOI](https://zenodo.org/badge/788452745.svg)](https://doi.org/10.5281/zenodo.15078670)

CMS open data usage tools

## Install
```
virtualenv dpoa
source dpoa/bin/activate
pip install -r requirements.txt
```
## Usage
Create the `arxiv.json` and `inspire.json`:
```
> cd data
> python3 query_inspire.py
> python3 query_arxiv.py
```

Open `publications.ipynb` and analyze:
```
> cd ../
> jupyter lab
```

Create html:
```
> jupyter nbconvert publications.ipynb --to html --no-input --output index.html
```

## Links
* [INSPIRE API](https://github.com/inspirehep/rest-api-doc)
* [ARXIV API](https://info.arxiv.org/help/api/basics.html)
* Inspire query: [papers that cite CMS open data DOIs](https://inspirehep.net/literature?sort=mostrecent&size=25&page=1&q=references.reference.dois%3A10.7483%2FOPENDATA.CMS%2A)
* [Inspire API query results](https://inspirehep.net/api/literature?sort=mostrecent&size=25&page=1&q=references.reference.dois%3A10.7483%2FOPENDATA.CMS*)
* arXiv query: [papers that contain "CMS Open Data" in abstract](https://arxiv.org/search/?query=%22CMS+Open+Data%22&searchtype=all&source=header)
* [arXiv API query results](https://export.arxiv.org/api/query?search_query="CMS+Open+Data"&searchtype=all&source=header) (returns atom xml file)
* [feedparser docs](https://feedparser.readthedocs.io/en/latest/)
* [DOI resolution API](https://www.doi.org/the-identifier/resources/factsheets/doi-resolution-documentation)
* [cernopendata-client](https://cernopendata-client.readthedocs.io/en/latest/index.html)
