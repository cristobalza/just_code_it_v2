# Write your MySQL query statement below

/*

ProductPurchases\

                 product_id | user_id | quantity | category | price
ProductInfo. /


 product_id | user_id | quantity | category | price 
    1           001.       2          elec.     300
    2.          001


*/

WITH user_category AS (
    SELECT DISTINCT 
        PPUR.user_id, 
        PINFO.category
    FROM ProductPurchases as PPUR
    INNER JOIN ProductInfo as PINFO
        ON PPUR.product_id = PINFO.product_id
),
category_pairs AS (
    SELECT 
        tbl_a.user_id,
        tbl_a.category AS category1,
        tbl_b.category AS category2
    FROM user_category as tbl_a
    INNER JOIN user_category as tbl_b
        ON tbl_a.user_id = tbl_b.user_id 
        AND tbl_a.category < tbl_b.category
)
SELECT 
    category1,
    category2,
    COUNT(DISTINCT user_id) AS customer_count
FROM category_pairs
GROUP BY category1, category2
HAVING customer_count >= 3
ORDER BY customer_count DESC, category1 ASC, category2 ASC;