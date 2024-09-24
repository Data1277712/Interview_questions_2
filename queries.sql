#second highest salary info from given table

SELECT *
FROM salaries
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
