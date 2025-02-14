# Write your MySQL query statement below
SELECT d.name as Department , e.name AS Employee , e.salary AS Salary from Employee e
JOIN Department d
ON e.departmentId  = d.id 
WHERE (e.departmentId , e.salary) IN (
    SELECT departmentId , MAX(salary) from Employee 
    GROUP BY departmentId
)