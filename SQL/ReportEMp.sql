SELECT E.employee_id ,  E.name  , COUNT(A.employee_id ) AS reports_count , ROUND(AVG(A.age)) AS average_age
FROM Employees E
JOIN Employees A
ON E.employee_id = A.reports_to 
GROUP BY E.employee_id
ORDER BY E.employee_id