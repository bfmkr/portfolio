# notes

## mean years school portfolio

The `mean_years_school.csv` data file shows the number of years men and women stay in school for different age brackets for 187 countries from 1970 until 2015.

Using Tableau, we will narrow it down to just the 19 G20 countries and investigate the following questions:

* How does the number of countries change over the years for Women in the 25-34 age bracket who spend more than 10 years in school? 
    * Does this number of years always increase for individual countries over time?

* Which countries have the largest and smallest ratio of men:women across all years?


### Avg 25-34 for G20 countries

This sub-task involved creating a calculated field.

Remember, this isn't a weighted average.
To make the calculation more accurate, we would need the country's population data for each gender and age group in the data set.
Then, we could alter the calculated field's formula to have weighted proprtions.


## Gapminder Health data set

### Symbol maps

* We looked at lung cancer and stomach cancer with symbol maps.
  The size of the circles indicates the total cases of cancer recorded in the corresponding countries.
* I used a diverging color scale for the fill of the circles according to population growth.
  This makes it easy to see at a glance if the population is growing on average (blue) or not (orange).

  This is useful because the World Health Organisation should focus not just on the countries with the highest number of cases, but also should take into account which populations are growing, in order to prevent health risks due to overpopulation.

  