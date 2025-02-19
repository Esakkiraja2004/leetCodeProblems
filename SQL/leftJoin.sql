SELECT EI.unique_id  , E.name From Employees E
LEFT JOIN EmployeeUNI EI
ON E.id = EI.id 
