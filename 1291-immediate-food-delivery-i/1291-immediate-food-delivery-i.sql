# Write your MySQL query statement below

WITH immediate_scheduled_tbl AS (
    SELECT
        delivery_id, 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        CASE
            WHEN order_date = customer_pref_delivery_date
            THEN "immediate"
            ELSE "scheduled"
        END AS delivery_type
    FROM Delivery
)

, quantify_tbl AS (
    SELECT
        delivery_id, 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        delivery_type,
        CASE 
            WHEN delivery_type = "immediate"
            THEN 1
            ELSE 0
        END AS delivery_type_int
        
    FROM immediate_scheduled_tbl
    
)

SELECT 
    ROUND((SUM(delivery_type_int) / COUNT(*)) * 100, 2) AS immediate_percentage
FROM quantify_tbl
;


