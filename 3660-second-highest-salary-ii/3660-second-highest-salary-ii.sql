# Write your MySQL query statement below
/*
1) Create a RANK over dept and emp_id ORDER BY salary
2) Filter WHERE the rank is 2
*/

WITH rank_tbl AS (
    SELECT
        emp_id,
        salary,
        dept,
        DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank_salary
    FROM employees
)
SELECT  
    emp_id,
    dept
FROM rank_tbl
WHERE rank_salary = 2
ORDER BY 
    emp_id ASC
;