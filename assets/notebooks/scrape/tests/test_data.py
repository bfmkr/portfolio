import pandas as pd
import pandas.api.types as ptypes

from scrape.data import get_issue_data

def test_issue_data():

    data = get_issue_data()
    assert all(data.columns == ['section', 'issue', 'date_published', 'authors', 'name',
           'is_highlighted'])
    assert ptypes.is_datetime64_any_dtype(data['date_published'])