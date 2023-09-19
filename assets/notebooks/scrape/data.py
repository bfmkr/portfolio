import os
import time
import random

import requests
from scrapy import Selector
import pandas as pd

# Volumes and Issues of PRB: https://journals.aps.org/prb/issues/

URL = 'https://journals.aps.org/prb/issues/99/1'


def get_issue_data(url=URL, force_download=False):
    """Scrape and cache article metadata from issues in Physical Review Journals

    Parameters
    ==========

    url : string (optional)
        Web location of the publication issue.
        By default, first issue from 2019.
    force_download : bool (optional)
        if True, force redownload of data.

    Returns
    =======

    data : pandas.DataFrame
        The issue data from the url.
        Includes columns:
        * doi
        * section
        * issue
        * date_published
        * authors
        * name
        * is_highlighted
    """

    filename = 'issue_' + '_'.join(url.split('/')[-2:]) + '.csv'

    if not force_download and os.path.exists(filename):
        return pd.read_csv(filename, index_col=[0],parse_dates=[3])


    html = requests.get(url).content
    sel = Selector(text = html)

    # Retrieve section names

    section_selectors = sel.xpath('//a[contains(@name,"sect-articles-")]')
    section_names = section_selectors.xpath('./@name').extract()

    # Retrieve DOIs and corresponding section names

    sections_dict = dict()
    doi_xpath = '..//div[@class="article panel article-result"]/@data-id'

    for sec in section_names:
        section_selector = sel.xpath('//a[@name="{}"]'.format(sec))
        dois = section_selector.xpath(doi_xpath).extract()
        sections_dict.update({doi:sec for doi in dois})

    # Initialize DataFrame

    section_series = pd.Series(sections_dict)
    df = pd.DataFrame(section_series, columns=['section'])

    # Add `issue` column to DataFrame

    issue = '/'.join(url.split('/')[-2:])
    df['issue'] = pd.Series({doi: issue for doi in sections_dict.keys()})

    # Add `date_published`, `authors`, and `name` to DataFrame

    pub_dates_dict = dict()
    authors_dict = dict()
    names_dict = dict()

    for k, v in sections_dict.items():

        sec_selector = sel.xpath(f'//a[@name="{v}"]')

        pub_info_xpath = f'..//div[@data-id="{k}"]//h6[@class="pub-info"]//text()'
        pub_info = ''.join(sec_selector.xpath(pub_info_xpath).extract())
        pub_dates_dict[k] = pub_info.split('Published ')[-1]

        authors_xpath = f'..//div[@data-id="{k}"]//h6[@class="authors"]//text()'
        authors_info = ''.join(sec_selector.xpath(authors_xpath).extract())
        authors_dict[k] = authors_info

        name = ''.join(
            sec_selector.xpath(f'..//a[@href="/prb/abstract/{k}"]//text()').extract()
        )
        names_dict[k] = name

    df['date_published'] = pd.Series(pub_dates_dict)
    df['authors'] = pd.Series(authors_dict)
    df['name'] = pd.Series(names_dict)

    # Add `is_highlighted` column to DataFrame

    selector = sel.xpath('//a[@name="sect-highlighted-articles"]')
    highlighted_xpath ='../div[@class="article panel article-result"]/@data-id'
    highlighted_articles = selector.xpath(highlighted_xpath).extract()

    is_highlighted_dict = dict()

    for i, article in enumerate(df.index):
        if article in highlighted_articles:
            is_highlighted_dict[article] = True
        else:
            is_highlighted_dict[article] = False

    is_highlighted_series = pd.Series(is_highlighted_dict)
    df["is_highlighted"] = is_highlighted_series

    print(f'Saving data to {filename}')
    df.to_csv(filename) # save data to a csv file

    return df


def get_citation_data(infile='issue_99_5.csv',
    outfile='citations_issue_99_5.csv', journal='prb', force_download=False):
    """Scrape and cache number of citations from Physical Review Journals

    Parameters
    ==========

    infile: string (optional)
        csv file with DOIs (digital object identifiers) as column 0
        Default is issue 99/5 of PRB from 2019, file provided in this
        repository.
    outfile: string (optional)
        name of the output file
    journal: string (optional)
        e.g. prb, prl, rmp etc. For a full list see https://journals.aps.org/
    force_download: bool (optional)
        if True, force redownload of data

    Returns
    =======

    df : pandas.DataFrame
        Updated DataFrame with citation numbers
    """

    article_base_url = f'https://journals.aps.org/{journal}/abstract/'

    if not os.path.exists(infile):
        print(f'File {infile} does not exist!')
        return None

    if os.path.exists(outfile) and not force_download:
        print(f'File {outfile} already exists!')
        return pd.read_csv(outfile,index_col=[0],parse_dates=[3])

    df = pd.read_csv(infile,index_col=[0])
    dois = list(df.index.values)

    citations_dict = dict()
    for doi in dois:

        article_url = article_base_url + doi
        html = requests.get(article_url).content

        time.sleep(random.randint(1,5)) # avoid flagging DDoS protective measures

        sel = Selector(text = html)
        s = sel.xpath('//a[contains(@href,"cited-by")]/text()').extract_first()
        if s == None:
            num_of_citations = 0
        else:
            num_of_citations = int(s.replace("Citing Articles ","")[1:-1])
        citations_dict[doi] = num_of_citations


    df[f'{journal}_citations'] = pd.Series(citations_dict)
    print(f'Saving data to {outfile}')
    df.to_csv(outfile)

    return df