# APS journal scraper

This folder contains tools that can be used for collecting publication data from [Physical Review Journals](https://journals.aps.org/).  
I will place it in its own dedicated repository at a later date.


## Dependencies

* [Python](https://www.python.org/). Any modern version will do.
* [Scrapy](https://scrapy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Requests](https://docs.python-requests.org/en/latest/index.html)


## Example Usage

To scrape and cache article metadata from all publications in Physical Review B in 2019:

```python
import pandas as pd
from scrape.data import get_issue_data

url_list = [f'https://journals.aps.org/prb/issues/{j}/' 
            + str(i+1) for j in [99,100] for i in range(24)]
df_list = []
for u in url_list:
    df_list.append(get_issue_data(url = u,force_download=True))
    time.sleep(random.randint(1,5)) # wait a bit before sending another request
    
df = pd.concat(df_list)
df.to_csv('prb_all_issues_2019_no_citation_data.csv')
```

To scrape citation numbers for papers, use the function `get_citation_data`:

```python 
import pandas as pd
from scrape.data import get_citation_data

infile = 'issue_99_5.csv'
outfile = 'citations_issue_99_5.csv'
df = get_citation_data(infile=infile,outfile=outfile,journal='prb')
```

The function `get_citation_data` scrapes and caches citation numbers given an input CSV file where the 0th column contains DOIs of research papers.


## Data fields collected

* DOI (digital object identifier)
* section
* issue
* date_published
* authors
* name
* is_highlighted
* {journal}_citations (where {journal} is one of {prl, prx, prb, etc.}. See <https://journals.aps.org/> for a full list.)


## Sample Jupyter notebooks

1. Notebook for [step-by-step details on the web scraping.](https://github.com/bfmkr/portfolio/blob/main/assets/notebooks/Web-scraping-Physical-Review-B-workbook.ipynb)
2. Notebook for [further example usage of the Python package.](https://github.com/bfmkr/portfolio/blob/main/assets/notebooks/Sample-notebook-for-scraping-publication-data-from-PRB-in-2019.ipynb)
3. Notebook for [data analysis and visualisations.](https://nbviewer.org/github/bfmkr/portfolio/blob/main/assets/notebooks/Data-Analysis-and-Visualisations-PRB-dataset.ipynb)

