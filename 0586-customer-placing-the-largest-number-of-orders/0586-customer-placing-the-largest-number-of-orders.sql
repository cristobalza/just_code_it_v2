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
WHERE count_orders = (SELECT MAX(count_orders) FROM count_tbl)
;