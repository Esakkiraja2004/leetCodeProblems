select e1.name as Employee from Employee e1
join Employee e2
on e2.id = e1.managerId and e1.salary > e2.salary;