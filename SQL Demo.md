---
layout: default
title: SQL Demo
---

# SQL Demo

&nbsp;

In this demo I answer the question "Who defeated Manchester United in the 2013/2014 season?" using PostgreSQL and the [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer?resource=download).


## Details of the database

The European Soccer Database contains information from >25k matches, including names of >10k players, player and team attributes (such as the team line up and squad formation) sourced from EA Sports' FIFA video game series, as well as historic betting odds from up to 10 providers, and details of match events (such as the number of fouls and corner kicks), across 11 European countries with their lead championships from seasons 2008-2016. 
The data is spread across 7 tables, *Fig. 1*.

<div>
<img src="{{ "/assets/images/EU-soccer-db-details.jpg" | prepend: site.baseurl }}" alt="EU-soccer-db-details" style="border: 1px solid #ddd">
<figcaption style="text-align:center; font-style:italic;">
    Fig. 1 Details of the database we will investigate. Data source: <a href="https://www.kaggle.com/datasets/hugomathien/soccer?resource=download" title="">kaggle</a>
</figcaption>  
</div>

## Acknowledgements

...