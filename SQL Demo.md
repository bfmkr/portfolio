---
layout: default
title: SQL Demo
---

# SQL Demo

&nbsp;

In this demo I answer the question "Who defeated Manchester United in the 2013/2014 season?" using SQL and the [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer?resource=download).


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

To answer our question we only two of the seven tables: `Match` and `Team`
Their relationship and some column names of interest are show in *Fig. 2*.

<div>
<img src="{{ "/assets/images/schema.png" | prepend: site.baseurl }}" alt="details-of-tables">
<figcaption style="text-align: center; font-style:italic; margin-top:2px;">
    Fig. 2 Schema for the <code>Match</code> and <code>Team</code> tables.
    Only columns of interest from the  <code>Match</code> table are shown.
</figcaption>
</div>

<!-- <https://app.datacamp.com/workspace/w/382a2788-6a90-4fc4-a950-a25d43a39f05/edit#explore-datasets> -->
An sample slice of the `Match` table to show the data we are working with is as follows

```sql
SELECT id, date, home_team_api_id, away_team_api_id, home_team_goal, away_team_goal, season
FROM Match
LIMIT 3;
```

| id | date                |  home_team_api_id |  away_team_api_id | home_team_goal | away_team_goal | season    |
| -- | ------------------- | ----------------  | ----------------- | -------------- | -------------- | --------- |
| 1  | 2008-08-17 00:00:00 | 9987              | 9993              | 1              | 1              | 2008/2009 |
| 2  | 2008-08-16 00:00:00 | 10000             | 9994              | 0              | 0              | 2008/2009 |
| 3  | 2008-08-16 00:00:00 | 9984              | 8635              | 0              | 3              | 2008/2009 |

And similarly, for the `Team` table:

```sql
SELECT  id, team_api_id, team_fifa_api_id, team_long_name, team_short_name
FROM Team
LIMIT 3;
```

| id |  team_api_id | team_fifa_api_id | team_long_name   | team_short_name |
| -- | -----------  | ---------------- | ---------------- | --------------- |
| 1  | 9987         | 673              | KRC Genk         | GEN             |
| 2  | 9993         | 675              | Beerschot AC     | BAC             |
| 3  | 10000        | 15005            | SV Zulte-Waregem | ZUL             |


## Building the query

We will need to scan through every match played by Manchester United in the `Match` table and identify who they were playing against using the match `id`, by doing a `LEFT JOIN` to the `Team` table.
We will need to evaluate if they won, lost, or tied, by comparing the `home_team_goal` and `away_team_goal` quantities.

...

## Putting it all together

```sql
-- Set up the home team CTE
WITH home AS (
  SELECT m.id, t.team_long_name,
      CASE WHEN m.home_team_goal > m.away_team_goal THEN 'MU Win'
           WHEN m.home_team_goal < m.away_team_goal THEN 'MU Loss' 
           ELSE 'Tie' END AS outcome
  FROM Match AS m
  LEFT JOIN Team AS t ON m.home_team_api_id = t.team_api_id),
-- Set up the away team CTE
away AS (
  SELECT m.id, t.team_long_name,
      CASE WHEN m.home_team_goal > m.away_team_goal THEN 'MU Win'
           WHEN m.home_team_goal < m.away_team_goal THEN 'MU Loss' 
           ELSE 'Tie' END AS outcome
  FROM Match AS m
  LEFT JOIN Team AS t ON m.away_team_api_id = t.team_api_id)
-- Select team names, the date and goals
SELECT DISTINCT
    date,
    home.team_long_name AS home_team,
    away.team_long_name AS away_team,
    m.home_team_goal,
    m.away_team_goal
-- Join the CTEs onto the match table
FROM Match AS m
INNER JOIN home ON m.id = home.id
INNER JOIN away ON m.id = away.id
WHERE m.season = '2014/2015'
      AND (home.team_long_name = 'Manchester United' 
           OR away.team_long_name = 'Manchester United');
```

## Result


## Extensions

There are many further interesting things to be found in this dataset...

## Acknowledgements

