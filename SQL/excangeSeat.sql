-- # Write your MySQL query statement below
SELECT 
CASE WHEN id = (SELECT MAX(id) FROM Seat) AND id % 2 = 1 THEN id 
WHEN id % 2 = 1 Then id+1
ELSE id -1 
END AS id, student
FROM Seat
ORDER BY id


-- # Write your MySQL query statement below

SELECT ROW_NUMBER() OVER() id, student
FROM seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)