---
layout: default
title: Tableau Demo 2
---

# Tableau Demo 2


&nbsp;

Here is an example Tableau Dashboard which can be downloaded from my [Tableau Public profile](https://public.tableau.com/views/VideoGameSalesdashboards/PlaystationOverview1994-2010?:language=en-GB&:display_count=n&:origin=viz_share_link).
Clicking the full screen button on the dashboard (icon at the bottom right of Fig. 1) is recommended.


## Playstation Video Game Sales from 1994-2010 

Fig. 1 shows an example interactive dashboard for Video Game Sales from 1994 - 2010 made in Tableau, focussing on products by Sony (Playstation 1,2,3 and Playstation Portable). 

Creating dashboards like this is really useful for interacting with and investigating data.
For example, in this case I have designed it so the **Sales by Genre** tree map (bottom right) and **Sales by Platform** bar chart (top right) can be activated as filters by clicking on them. 
By using this in combination with the **Publisher** drop-down menu, we can quickly discover that the top selling video game published by Electronic Arts in the Simulation genre for the PS2 console was "The Sims" with 2.77 million global sales in 2003. 

* To do this, filter for "Electronic Arts" in the Publisher drop-down, click on the "PS2" vertical bar in the Sales by Platform chart, and click on the "Simulation" area (coloured teal) in the Sales by Genre tree map.
  After doing so, the Top Video Games bar horizontal bar chart will show "The Sims" in the top spot, and hovering over it shows the sales information in the pop-up.

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
<figcaption style="text-align:center; font-style: italic;"> 
    Fig. 1 Playstation video game sales dashboard, Data Source: <a href="https://www.kaggle.com/datasets/gregorut/videogamesales"> kaggle</a>
</figcaption>

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

