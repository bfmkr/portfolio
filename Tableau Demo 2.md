---
    layout: default
    title: Tableau Demo 2
---

# Tableau Demo 2

&nbsp;

This demo investigates the average number of years people spend in school among the G20 countries.
I answer the questions:

1. Is the number of years spent in school always increasing, or has it declined for some nations? 
  Has growth plateaued?
1. Which countries have had the greatest shift towards equality between men and women?

All figures in this demo are interactive/clickable and embedded from the workbook hosted on Tableau public, which is available to download [here](https://public.tableau.com/app/profile/ben.mckeever/viz/MeanYearsinSchool/average).


## The mean years spent in school dataset

The `mean_years_school.csv` dataset in *Table 1* shows the average number of years men and women stay in school for different age brackets for 187 countries from 1970 until 2015, comprising ~6800 rows of data.
This is a useful indicator of social and economic development.

![mean-years-school](/assets/images/mean_years_school.png)
*Table 1 Sample of the "mean years spent in school" dataset (source:  <https://www.gapminder.org/data>)*




## Part 1: the mean number of years in school in G20 countries

In this part we will answer the first question.


### Averaging across all years

By focussing on on the 25-34 age bracket across the 45 years of data we can get a good idea about the answers to our questions. 
This is sensible because the amount of time people spend in formal education decreases with age, so the youngest age bracket available should still contain the bulk of the interesting information.

*Fig. 1* shows the years spent in school for the G20 countries averaged across all years in the dataset.


<div style="
  width: 100%;
  padding: 10px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: auto auto">
  <div class='tableauPlaceholder' id='viz1688091487986' style='position: relative;width: 550px;'>
    <noscript>
      <a href='#'><img alt='G20 Countries Average (1970-2015) ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;average&#47;1_rss.png' style='border: none' /></a>
    </noscript>
    <object class='tableauViz'  style='width:550px;padding: 10px;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
      <param name='embed_code_version' value='3' /> 
      <param name='site_root' value='' />
      <param name='name' value='MeanYearsinSchool&#47;average' />
      <param name='tabs' value='no' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;average&#47;1.png' /> 
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-GB' />
      <param name='filter' value='publish=yes' />
    </object>
  </div>
  <div class='tableauPlaceholder' id='viz1688093659513' style='position: relative;width: 430px;'>
    <noscript>
      <a href='#'>
        <img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;averagetreemap&#47;1_rss.png' style='border: none' />
      </a>
    </noscript>
    <object class='tableauViz'  style='width:430px;padding: 10px;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
      <param name='embed_code_version' value='3' /> 
      <param name='site_root' value='' />
      <param name='name' value='MeanYearsinSchool&#47;averagetreemap' />
      <param name='tabs' value='yes' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;averagetreemap&#47;1.png' /> 
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-GB' />
    </object>
  </div>
</div>
<figcaption style="text-align:center; font-style:italic; margin-top: 20px; margin-bottom:20px">
    Fig. 1 Left: the years spent in school for the 25-34 age bracket for just the G20 countries. 
    The USA has the largest average number of years spent in school at 13.40 years. 
    Australia places 5th with 11.51 years.
    Right: same data now in a tree map. The area of each country's rectangle is proportional to the number of years spent in school.
</figcaption>


Some details:

* To narrow it down to just the nineteen G20 countries, I applied a filter to the `Country` field.
* A calculated field `[25-34] = ([Men 25-34] + [Women 25-34])/2` estimates the average across both genders. <br> <br> 
    This isn't a weighted average -- each group will have different amounts of people, and different amounts for each year. 
    To make the calculation more accurate, we would also need this population data, and then we could then alter the calculated field's formula to have weighted proportions. 
    Since this data is not available, this is a rough estimate assuming equal amounts of men and women.


### Average years spent in school across the years

On first glance of *Fig. 1*, it appears the USA has the largest average years spent in school.
However, as shown in *Fig. 2*, it turns out that this is only due to an early lead; in fact, the USA is in fact the *only* G20 country which shows any kind of plateau in the dataset. 
This occurs in the 1990s, during which Canada and then later Japan overtakes the US for 1st and 2nd place respectively.

<div style="
  width: 100%;
  padding: 10px;">
  <div class='tableauPlaceholder' id='viz1688360651008' style='position: relative'>
    <noscript>
      <a href='#'>
        <img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;averageovertime&#47;1_rss.png' style='border: none' />
      </a>
    </noscript>
    <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
      <param name='embed_code_version' value='3' /> 
      <param name='site_root' value='' />
      <param name='name' value='MeanYearsinSchool&#47;averageovertime' />
      <param name='tabs' value='yes' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;averageovertime&#47;1.png' /> 
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-GB' />
      <param name='filter' value='publish=yes' />
    </object>
  </div>
</div>

<figcaption style="text-align:center;font-style:italic; margin-top: 20px; margin-bottom:20px">
  Fig. 2 In 1993, Canada overtook the USA for top spot for the mean number of years spent in school in the 25-34 age group. <br> 
  All countries follow a roughly linear growth apart from the USA which had a plateau for a span of ~10 years starting around 1990.
  (Individual country lines can be clicked on to highlight them)
</figcaption>


### Conclusion

In conclusion, yes, the average number of years spent in school is generally increasing for the G20 countries, however, progress stalled in one country -- the USA -- during a 10 year period in the 1990s, after which it began to increase again.


## Part 2: Differences between genders over time

In this part we answer the second question. 
Just as in part 1, we can focus on the 25-34 years age bracket to get a good sense of the answers to our questions.


### Ratio over time

To get an idea about equality between men and women we could investigate either the difference or the ratio between men and women's mean years in school and similarly look at how this has changed over time.

<div style="
  width: 100%;
  padding: 10px;">
  <div class='tableauPlaceholder' id='viz1688704511539' style='position: relative'>
    <noscript>
      <a href='#'>
        <img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;Ratio&#47;1_rss.png' style='border: none' />
      </a>
    </noscript>
    <object class='tableauViz'  style='display:none;'>
      <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
      <param name='embed_code_version' value='3' /> 
      <param name='site_root' value='' />
      <param name='name' value='MeanYearsinSchool&#47;Ratio' />
      <param name='tabs' value='yes' />
      <param name='toolbar' value='yes' />
      <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Me&#47;MeanYearsinSchool&#47;Ratio&#47;1.png' /> 
      <param name='animate_transition' value='yes' />
      <param name='display_static_image' value='yes' />
      <param name='display_spinner' value='yes' />
      <param name='display_overlay' value='yes' />
      <param name='display_count' value='yes' />
      <param name='language' value='en-GB' />
      <param name='filter' value='publish=yes' />
    </object>
  </div>
</div>

<figcaption style="text-align:center;font-style:italic;margin-top:20px; margin-bottom:20px;">
  Fig. 3 Investigating the ratio of men:women average years spent in school for the 25-34 age bracket. <br>
  Countries show a general downward trend overall with a close to linear behaviour. 
  A handful of countries even dip below 1 which indicates the average years spent in school for women is higher than men.
</figcaption>

Some notes:

* To achieve *Fig. 3* a new calculated field `[Men:Women (25-34)] = [Men 25-34] / [Women 25-34]` was used.
* If we wish to be able to better distinguish between the bottom grouping of countries, which are very close together, we can simply exclude the top 5 countries from this plot. 
    In the figure embedded above this can be done interactively -- simply click on the country to remove in the legend on the right, and then click `exclude`.


### Conclusion

From *Fig. 3* we can immediately see that India and Saudi Arabia have had the most dramatic changes, with their ratios dropping by nearly 1 across all years of data.
These countries also especially stand out from the others by their significantly larger negative gradients across the initial half of the data, from 1970 to around 1995.

To be more specific, by comparing their absolute numbers side by side, we can further quantify that India has had the largest change out of the two:

|                | India | Saudi Arabia | 
|----------------|-------|--------------|
| 1970           | 2.454 | 2.253        |
| 2015           | 1.473 | 1.301        |
| **Difference** | 0.981 | 0.952        |


By 2015 Indian men have an average of 1.47 years of schooling for every year of schooling Indian women have, down from 2.45 years in 1970.
It is notable, however, that India is still the furthest country away from equality, and that its negative gradient has become flatter over time which indicates a slowing of progress somewhat.

In conclusion, we therefore can confidently answer the question with "India and Saudi Arabia stand out as having the greatest shifts towards equality between men and women, and India had the greatest shift overall"


<script type='text/javascript'>
var divElement = document.getElementById('viz1688091487986');
var vizElement = divElement.getElementsByTagName('object')[0];
vizElement.style.width='100%';
vizElement.style.height=(divElement.offsetWidth*1.06)+'px';
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<script type='text/javascript'>
  var divElement = document.getElementById('viz1688093659513');
  var vizElement = divElement.getElementsByTagName('object')[0];
  vizElement.style.width='100%';
  vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

<script type='text/javascript'>
    var divElement = document.getElementById('viz1688360651008');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width='100%';
    vizElement.style.height=(divElement.offsetWidth*0.5)+'px';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>


<script type='text/javascript'>
  var divElement = document.getElementById('viz1688704511539');
  var vizElement = divElement.getElementsByTagName('object')[0];
  vizElement.style.width='100%';
  vizElement.style.height=(divElement.offsetWidth*0.5)+'px';
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>