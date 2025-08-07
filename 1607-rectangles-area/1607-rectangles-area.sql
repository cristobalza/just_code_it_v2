# Write your MySQL query statement below
WITH area_tbl AS (
    SELECT
        tbl1.id AS p1,
        tbl2.id AS p2, 
        ABS(tbl1.x_value - tbl2.x_value) * ABS(tbl1.y_value - tbl2.y_value) AS area
    FROM Points AS tbl1
    CROSS JOIN Points AS tbl2
)

SELECT
    p1,
    p2,
    area
FROM area_tbl
WHERE 
    area != 0
    AND p1 < p2
ORDER BY
    area DESC, p1, p2