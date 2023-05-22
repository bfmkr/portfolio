---
layout: default
title: Tableau Demo 1
---

# Tableau Demo 1

## Mean years spent in school data set

The `mean_years_school.csv` data set in Fig. 1 shows the average number of years men and women stay in school for different age brackets for 187 countries from 1970 until 2015.

![mean-years-school](/assets/images/mean_years_school.png)
*Fig.1 Mean years spent in school data set (source:  <https://www.gapminder.org/data>)*

Using Tableau, we will narrow it down to just the 19 different member countries of G20, investigate how the numbers have changed over time, and answer the questions:

* Is the number of years spent in school always increasing, or has it declined for some nations? 
  Has progress plateaued?
* Which countries have had the greatest shift towards equality between men and women?



## Average data for the 25-34 age bracket for G20 countries

By focussing on a specific age bracket we can get a good first idea about the average number of years spent in school. 
The most relevant age bracket to check is the 25 - 34 age group. 
First let us look at the average across all years of available data (Fig. 2).

![g20-average-25-34](/assets/images/g20-countries-average.png)
*Fig. 2 Investigating the 25-34 age bracket among G20 countries. Across all available data, the USA has the largest average number of years spent in school at 13.40 years, and Australia places 5th with 11.51 years.*

* To narrow it down to the 19 countries of interest, I applied a filter to the `Country` field.
* To get an estimate, I created a calculated field: `[25-34] = ([Men 25-34] + [Women 25-34]) /2`

    It is important to note that this isn't a weighted average.
    To make the calculation more accurate, we would need the country's population data for each gender and age group in the data set.
    We could then alter the calculated field's formula to have weighted proportions.

On first glance of Fig. 2, it appears the USA has the largest average years spent in school.
However, if we look with more granularity, it turns out that this is due to an early lead.
 In fact, the USA is the *only* country with a plateau in the data, which occurs in the 1990s, during which Canada and then later Japan overtook them, Fig. 3. 

![usa-plateau](assets/images/usa-plateau.png)
*Fig. 3 In 1993, Canada overtook the USA for top spot for the mean number of years spent in school in the 25-34 age group. Apart from the USA, which has a plateau here for around 10 years, all other countries follow a roughly linear growth.* 

TODO: make figure labels larger.


### Rolling averages

To see how the average years spent in school has evolved over time to reach the values in Fig. 2, we can check the rolling average.
This is a useful technique in general for investigating trends in time series data.

* Plot Avg 25-34 versus year for each country.
* Also plot cumulative average, and the 5 year rolling average.


### Ratio

To get an idea about equality between men and women we can investigate the ratio, and similarly look at the rolling averages.