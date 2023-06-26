---
layout: default
title: SQL Demo
---

# SQL Demo

&nbsp;

In this demo I answer the question "Who defeated Manchester United in the 2013/2014 season?" using PostgreSQL and the [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer?resource=download).


## Details of the database

The European Soccer Database contains information from >25k matches, including names of >10k players, various attributes of the players and teams (such as the team line up and squad formation), as well as historic betting odds from up to 10 providers, and details of match events (such as the number of fouls and corner kicks).
The data spans 11 European countries with their lead championships from seasons 2008-2016, and is contained in 7 tables, *Fig. 1*.

<div>
<img src="{{ "/assets/images/EU-soccer-db-details.jpg" | prepend: site.baseurl }}" alt="EU-soccer-db-details" style="border: 1px solid #ddd">
<figcaption style="text-align:center; font-style:italic; margin-top:2px;">
    Fig. 1 Details of the database we will investigate. Data source: <a href="https://www.kaggle.com/datasets/hugomathien/soccer?resource=download" title="">kaggle</a>
</figcaption>  
</div>

## Tables of interest

To answer our question we only need a subset of the 7 tables.
The relations between the relevant tables we will use and their column names are show in *Fig. 2*.

<div>
<img src="{{ "assets/images/soccer-tables.png" | prepend: site.baseurl }}" alt="EU-soccer-db-details" style="border: 1px solid #ddd">
<figcaption style="text-align: center; font-style:italic; margin-top:2px;">
    Fig. 2 Details of columns in the "match" and "team" tables, after some considerable pruning of the dataset.  TODO: fix!
</figcaption>
</div>

<https://app.datacamp.com/workspace/w/382a2788-6a90-4fc4-a950-a25d43a39f05/edit#explore-datasets>

## Building the query



## Putting it all together

```sql
-- Set up the home team CTE
WITH home AS (
  SELECT m.id, t.team_long_name,
      CASE WHEN m.home_goal > m.away_goal THEN 'MU Win'
           WHEN m.home_goal < m.away_goal THEN 'MU Loss' 
           ELSE 'Tie' END AS outcome
  FROM soccer.match AS m
  LEFT JOIN soccer.team AS t ON m.hometeam_id = t.team_api_id),
-- Set up the away team CTE
away AS (
  SELECT m.id, t.team_long_name,
      CASE WHEN m.home_goal > m.away_goal THEN 'MU Win'
           WHEN m.home_goal < m.away_goal THEN 'MU Loss' 
           ELSE 'Tie' END AS outcome
  FROM soccer.match AS m
  LEFT JOIN soccer.team AS t ON m.awayteam_id = t.team_api_id)
-- Select team names, the date and goals
SELECT DISTINCT
    date,
    home.team_long_name AS home_team,
    away.team_long_name AS away_team,
    m.home_goal,
    m.away_goal
-- Join the CTEs onto the match table
FROM soccer.match AS m
INNER JOIN home ON m.id = home.id
INNER JOIN away ON m.id = away.id
WHERE m.season = '2014/2015'
      AND (home.team_long_name = 'Manchester United' 
           OR away.team_long_name = 'Manchester United');
```

## Result





## Acknowledgements

