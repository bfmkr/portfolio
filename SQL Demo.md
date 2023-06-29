---
    layout: default
    title: SQL Demo
---

# SQL Demo

&nbsp;

In this demo I answer the question "Who defeated Manchester United in the 2014/2015 season?" using SQL and the [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer?resource=download).
Click to [skip to the results](#results).


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

To answer the question we only need two out of the seven tables: `Match` and `Team`.
Their relationship and some relevant column names are shown in *Fig. 2*.

<div>
<img src="{{ "/assets/images/schema.png" | prepend: site.baseurl }}" alt="details-of-tables">
<figcaption style="text-align: center; font-style:italic; margin-top:2px;">
    Fig. 2 Schema for the <code>Match</code> and <code>Team</code> tables. Only a few relevant columns from the  <code>Match</code> table are displayed. <br>
    The <code>team_api_id</code> fields map to each other between the tables as shown.
</figcaption>
</div>

An sample of the `Match` table is as follows

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

We will need to scan through every match played by Manchester United in the `Match` table, identify who they were playing against, limit it to the `2014/2015` season, and further narrow it down to just the games where they lost.

Since some of the time they will be the home team, and some of the time the away team, we will actually need to scan through the `Match` table twice.
In a first step, it will be useful to obtain the `team_api_id` and `team_short_name` for Manchester United in order to hardcode this into future queries:

```sql
SELECT team_short_name, team_api_id AS MU_team_api_id 
FROM Team 
WHERE team_long_name = 'Manchester United';
```

| team_short_name | MU_team_api_id |
|-----------------|----------------|
| MUN             | 10260          |

### Home team games vs Away team games

To retrieve the match IDs in 2014/2015 where MU are the home team, as well as the outcome of the football match, we can do the following query:

```sql
SELECT m.id AS match_id,
    CASE WHEN m.home_team_goal > m.away_team_goal THEN 'MU Win'
         WHEN m.home_team_goal < m.away_team_goal THEN 'MU Loss' 
         ELSE 'Tie' END AS outcome_home_games
FROM Match AS m
LEFT JOIN Team AS t ON m.home_team_api_id = t.team_api_id
WHERE m.season = '2014/2015' AND t.team_api_id = 10260;
```
The first few results are:

| match_id | outcome_home_games |
|----------|--------------------|
| 4013     | MU Loss            |
| 4031     | MU Win             |
| 4051     | MU Win             |

A similar query retrieves the match IDs for when MU are the away team, where we would instead use `m.away_team_api_id` in the left join.


### Combining into CTEs

By using common table expressions (CTEs) for the home and away games obtained above, we can do further joins back onto the `Match` table in order to extract **all** of the records for the different football games played by MU.

```sql
-- Set up the home team CTE
WITH home AS (
  SELECT m.id, t.team_long_name
  FROM Match AS m
  LEFT JOIN Team AS t ON m.home_team_api_id = t.team_api_id),
-- Set up the away team CTE
away AS (
  SELECT m.id, t.team_long_name
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
The first few results:

|        date         |      home_team       |      away_team       | home_team_goal | away_team_goal |
|---------------------|----------------------|----------------------|----------------|----------------|
| 2014-08-16 00:00:00 | Manchester United    | Swansea City         | 1              | 2              |
| 2014-11-02 00:00:00 | Manchester City      | Manchester United    | 1              | 0              |
| 2014-11-08 00:00:00 | Manchester United    | Crystal Palace       | 1              | 0              |

A few notes:

* This time we successively used `INNER JOIN` on the match IDs from the `Match` table onto those collected from the `home` and `away` CTEs.
 This ensures that only relevant results are retained.
* By removing the hardcoded `t.team_api_id = 10260`, and replacing it with the `WHERE` clause at the very end of the query, we can now easily investigate any other football team's results in the dataset, e.g. `'Manchester United'` can be replaced by `'FC Bayern Munich'` if we are interested more in the Bundesliga than the English Premier League.


## Putting it all together

The most recent query above returns 38 records in total -- comprising all of the games played by MU in that Premier League season. 
This is few enough that we could simply go through them and read off which teams defeated Manchester United.

However, what if many more games were played per season? Or what if we were instead interested in results across *every* season in the dataset?
In either case it would be unrealistic to read through every fixture. 
We can add a `CASE` statement to the main query with a corresponding `WHERE` clause to list just the outcomes which were losses for Manchester United:


```sql
WITH home AS (
  SELECT m.id, t.team_long_name, t.team_short_name
  FROM Match AS m
  LEFT JOIN Team AS t ON m.home_team_api_id = t.team_api_id),
away AS (
  SELECT m.id, t.team_long_name, t.team_short_name
  FROM Match AS m
  LEFT JOIN Team AS t ON m.away_team_api_id = t.team_api_id)
SELECT DISTINCT
    date,
    home.team_long_name AS home_team,
    away.team_long_name AS away_team,
    m.home_team_goal,
    m.away_team_goal,
        CASE 
          WHEN (
            (m.home_team_goal > m.away_team_goal AND home.team_short_name = 'MUN')
            OR (m.home_team_goal < m.away_team_goal AND away.team_short_name = 'MUN')
          )
          THEN 'MU Win'
          WHEN (
            (m.home_team_goal < m.away_team_goal AND home.team_short_name = 'MUN')
            OR (m.home_team_goal > m.away_team_goal AND away.team_short_name = 'MUN')
          )
          THEN 'MU Loss' 
          ELSE 'Tie' 
        END AS outcome
FROM Match AS m
INNER JOIN home ON m.id = home.id
INNER JOIN away ON m.id = away.id
WHERE m.season = '2014/2015'
      AND (home.team_long_name = 'Manchester United' 
           OR away.team_long_name = 'Manchester United')
      AND outcome = 'MU Loss';
```



## Results

|        date         |     home_team     |      away_team       | home_team_goal | away_team_goal | outcome |
|---------------------|-------------------|----------------------|----------------|----------------|---------|
| 2014-08-16 00:00:00 | Manchester United | Swansea City         | 1              | 2              | MU Loss |
| 2014-11-02 00:00:00 | Manchester City   | Manchester United    | 1              | 0              | MU Loss |
| 2015-01-11 00:00:00 | Manchester United | Southampton          | 0              | 1              | MU Loss |
| 2015-02-21 00:00:00 | Swansea City      | Manchester United    | 2              | 1              | MU Loss |
| 2015-04-18 00:00:00 | Chelsea           | Manchester United    | 1              | 0              | MU Loss |
| 2015-04-26 00:00:00 | Everton           | Manchester United    | 3              | 0              | MU Loss |
| 2015-05-02 00:00:00 | Manchester United | West Bromwich Albion | 0              | 1              | MU Loss |
| 2014-09-21 00:00:00 | Leicester City    | Manchester United    | 5              | 3              | MU Loss |

<a name="results"></a>
In conclusion, in the 2014/2015 season Manchester United were defeated by seven teams: Southampton, Swansea City (twice), Manchester City, Chelsea, Everton, West Bromwich Albion, and Leicester City.

<!-- 
## Extensions

There are many further interesting things to be found in this dataset...

## Acknowledgements

 -->