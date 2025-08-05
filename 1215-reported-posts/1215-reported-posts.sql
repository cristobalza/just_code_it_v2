# Write your MySQL query statement below
WITH filter_tbl AS (
    SELECT
        extra,
        post_id
    FROM Actions
    WHERE action_date = "2019-07-04" AND action = "report"
)

SELECT
    extra AS report_reason,
    COUNT(DISTINCT post_id) AS report_count
FROM filter_tbl
GROUP BY 
    extra