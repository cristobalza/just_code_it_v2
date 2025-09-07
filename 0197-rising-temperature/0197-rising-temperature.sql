# Write your MySQL query statement below
SELECT
    id
FROM (
    SELECT 
        id,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) AS diff_recordDate
    FROM Weather
) w
WHERE temperature > prev_temp and diff_recordDate = 1
;