# Write your MySQL query statement below
WITH avg_activity AS (
    SELECT
        event_type,
        AVG(occurrences) AS average_activity
    FROM Events
    GROUP BY event_type
)

SELECT
    e.business_id
FROM Events e
INNER JOIN avg_activity aa
    ON e.event_type = aa.event_type
WHERE e.occurrences > aa.average_activity
GROUP BY e.business_id
HAVING COUNT(*) > 1
;