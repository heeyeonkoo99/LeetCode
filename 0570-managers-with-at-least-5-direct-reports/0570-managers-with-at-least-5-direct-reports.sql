# Write your MySQL query statement below
SELECT m.name
FROM Employee e
JOIN Employee m
    on m.id=e.managerId
GROUP BY m.id,m.name
HAVING COUNT(m.id)>=5