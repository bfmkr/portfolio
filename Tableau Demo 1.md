---
    layout: default-wide
    title: Tableau Demo 1
---

# Tableau Demo 1

&nbsp;

This demo contains an example Tableau Dashboard displaying video game sales which can be downloaded from Tableau [here](https://public.tableau.com/views/VideoGameSalesdashboards/PlaystationOverview1994-2010?:language=en-GB&:display_count=n&:origin=viz_share_link).


## Playstation Video Game Sales from 1994-2010 

*Fig. 1* shows an example interactive dashboard for Video Game Sales from 1994 - 2010 made in Tableau, focussing on products by Sony (Playstation 1,2,3 and Playstation Portable). 


<div class='tableauPlaceholder' id='viz1684839151419' style='position: relative; border: 1px solid #ddd'>
<noscript>
<a href='#'>
<img alt='Playstation Overview 1994-2010 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VideoGameSalesdashboards&#47;PlaystationOverview1994-2010&#47;1_rss.png' style='border: none' />
</a>
</noscript>
<object class='tableauViz'  style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
<param name='embed_code_version' value='3' />
<param name='site_root' value='' />
<param name='name' value='VideoGameSalesdashboards&#47;PlaystationOverview1994-2010' />
<param name='tabs' value='no' />
<param name='toolbar' value='yes' />
<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VideoGameSalesdashboards&#47;PlaystationOverview1994-2010&#47;1.png' />
<param name='animate_transition' value='yes' />
<param name='display_static_image' value='yes' />
<param name='display_spinner' value='yes' />
<param name='display_overlay' value='yes' />
<param name='display_count' value='yes' />
<param name='language' value='en-GB' />
</object>
</div>
<figcaption style="text-align:center; font-style: italic; margin-top: 20px; margin-bottom: 20px;"> 
    Fig. 1 Playstation video game sales dashboard (data source: <a href="https://www.kaggle.com/datasets/gregorut/videogamesales"> kaggle.com</a>) <br>
    Clicking the full screen button (bottom right icon) is recommended for smaller displays.
</figcaption>


Creating dashboards like this is useful for interacting with and investigating data.
In this example dashboard, the **Sales by Genre** tree map (bottom right) and **Sales by Platform** bar chart (top right) can be activated as filters by clicking on them, which changes the contents of the other charts.


### Example 

For example, by using the **Publisher** drop-down menu, we can quickly discover that the top selling video game published by Electronic Arts in the Simulation genre for the PS2 console was "The Sims" with 2.77 million global sales in 2003. To verify this:

1. Filter for "Electronic Arts" by using the Publisher drop-down.
2. Click on the "PS2" vertical bar in the Sales by Platform chart.
3. Click on the "Simulation" area (coloured teal) in the Sales by Genre tree map.

After doing so, the **Top Video Games** horizontal bar chart will show "The Sims" in the top spot, and hovering over it with the mouse shows the sales information we quoted.


<script type='text/javascript'>
var divElement = document.getElementById('viz1684839151419');
var vizElement = divElement.getElementsByTagName('object')[0];
if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
else { vizElement.style.width='100%';vizElement.style.height='1477px';}
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>