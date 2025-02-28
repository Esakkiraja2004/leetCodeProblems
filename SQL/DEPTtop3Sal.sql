-- # Write your MySQL query statement below

SELECT D.name AS Department ,E.name AS Employee ,E.salary AS Salary FROM Employee E
JOIN Department D
ON E.departmentId = D.id
WHERE
    3 > (SELECT COUNT(DISTINCT e2.salary)
        FROM Employee e2
        WHERE e2.salary > E.salary AND E.departmentId = e2.departmentId);