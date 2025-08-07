# Write your MySQL query statement below
-- volume = W * H * L
/*
1) JOIN tables to get warehouse and products measurements
2) CALCULATE volume
3) GROUP BY warehouse and SUM(volume) of each product id
*/

WITH warehouse_x_products AS (
    SELECT
        w.name AS warehouse_name,
        p.product_name,
        (p.Width * p.Length * p.Height) * w.units AS volume
    FROM Warehouse w
    LEFT JOIN Products p
        ON w.product_id = p.product_id
    
)

SELECT 
    warehouse_name,
    SUM(volume) AS volume
FROM warehouse_x_products
GROUP BY 
    warehouse_name
;