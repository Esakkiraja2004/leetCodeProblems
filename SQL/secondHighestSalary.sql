SELECT MAX(salary) AS SecondHighestSalary from Employee 
WHERE salary < (SELECT MAX(salary) FROM Employee) ;