WITH activity_totals AS (
    SELECT 
        ag.age_bucket,
        ac.activity_type,
        SUM(ac.time_spent) as total_time
    FROM Activities ac 
    INNER JOIN Age ag ON ac.user_id = ag.user_id
    WHERE ac.activity_type IN ('send', 'open')
    GROUP BY ag.age_bucket, ac.activity_type
),

age_bucket_totals AS (
    SELECT 
        age_bucket,
        SUM(total_time) as bucket_total_time
    FROM activity_totals
    GROUP BY age_bucket
)

SELECT 
    abt.age_bucket,
    ROUND(
        COALESCE(send_time.total_time, 0) * 100.0 / abt.bucket_total_time, 2
    ) as send_perc,
    ROUND(
        COALESCE(open_time.total_time, 0) * 100.0 / abt.bucket_total_time, 2
    ) as open_perc
FROM age_bucket_totals abt
LEFT JOIN activity_totals send_time 
    ON abt.age_bucket = send_time.age_bucket 
    AND send_time.activity_type = 'send'
LEFT JOIN activity_totals open_time 
    ON abt.age_bucket = open_time.age_bucket 
    AND open_time.activity_type = 'open'
ORDER BY abt.age_bucket;