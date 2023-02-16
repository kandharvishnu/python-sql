--https://www.youtube.com/watch?v=qyAgWL066Vo
use sql_study;
create table icc_world_cup
(
Team_1 Varchar(20),
Team_2 Varchar(20),
Winner Varchar(20)
);
INSERT INTO icc_world_cup values('India','SL','India');
INSERT INTO icc_world_cup values('SL','Aus','Aus');
INSERT INTO icc_world_cup values('SA','Eng','Eng');
INSERT INTO icc_world_cup values('Eng','NZ','NZ');
INSERT INTO icc_world_cup values('Aus','India','India');

select * from icc_world_cup;

WITH winner_list AS (
SELECT team_1 AS team_name, CASE WHEN team_1=winner THEN 1 ELSE 0 END AS win_flag
FROM icc_world_cup
UNION ALL
SELECT team_2 AS team_name, CASE WHEN team_2=winner THEN 1 ELSE 0 END AS win_flag
FROM icc_world_cup
)
SELECT team_name, COUNT(1) AS no_of_matches_played,
SUM(win_flag) AS no_of_matches_won,
COUNT(1)-SUM(win_flag) AS no_of_matches_lost
FROM winner_list
GROUP BY team_name 
ORDER BY no_of_matches_won desc,
no_of_matches_lost
;
