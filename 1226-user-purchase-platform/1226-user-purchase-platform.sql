# Write your MySQL query statement below

-- Create all possible combinations of dates and platforms
WITH all_combinations AS (
    SELECT DISTINCT spend_date, 'desktop' AS platform FROM Spending
    UNION ALL
    SELECT DISTINCT spend_date, 'mobile' AS platform FROM Spending  
    UNION ALL
    SELECT DISTINCT spend_date, 'both' AS platform FROM Spending
),

-- Categorize each user's spending by date
user_platform AS (
    SELECT 
        spend_date,
        user_id,
        CASE 
            WHEN COUNT(DISTINCT platform) = 1 THEN MIN(platform)  -- Only one platform
            WHEN COUNT(DISTINCT platform) = 2 THEN 'both'         -- Both platforms
        END AS platform,
        SUM(amount) AS amount
    FROM Spending
    GROUP BY spend_date, user_id
)

-- Join and aggregate
SELECT 
    ac.spend_date,
    ac.platform,
    COALESCE(SUM(up.amount), 0) AS total_amount,
    COUNT(up.user_id) AS total_users
FROM all_combinations ac
LEFT JOIN user_platform up 
    ON ac.spend_date = up.spend_date 
    AND ac.platform = up.platform
GROUP BY ac.spend_date, ac.platform
ORDER BY ac.spend_date, ac.platform;