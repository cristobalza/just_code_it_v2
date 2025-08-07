# Write your MySQL query statement below
WITH count_tbl AS (
    SELECT
        customer_number,
        COUNT(*) AS count_orders
    FROM Orders
    GROUP BY customer_number
)

SELECT
    customer_number
FROM count_tbl
ORDER BY count_orders DESC
LIMIT 1
;