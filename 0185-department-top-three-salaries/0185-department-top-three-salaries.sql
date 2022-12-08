# Write your MySQL query statement below
select d.name Department, e.name Employee, e.salary Salary from employee e join department d on e.departmentId = d.id
where e.salary in (select * from (select distinct(salary) from employee where departmentId = e.departmentId order by salary desc limit 3) as _
)