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

All figures in this demo are interactive/clickable and embedded from the workbook hosted on Tableau public, which is available to download [here]().


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
  outline: solid 1px black;">
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

In this part we we answer the second question.

> Which countries have the largest and smallest ratio of men:women across all years?

To get an idea about equality between men and women we can investigate the ratio, and similarly look at the rolling averages.






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