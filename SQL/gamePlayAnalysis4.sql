SELECT
ROUND(SUM(CASE
WHEN A2.event_date = DATE_ADD(A1.first_login_date, INTERVAL 1 DAY) THEN 1
ELSE 0 END) * 1.0 / COUNT(DISTINCT A1.player_id), 2) AS fraction
FROM
(SELECT player_id, MIN(event_date) AS first_login_date
FROM Activity
GROUP BY player_id) A1
LEFT JOIN
Activity A2
ON
A1.player_id = A2.player_id;