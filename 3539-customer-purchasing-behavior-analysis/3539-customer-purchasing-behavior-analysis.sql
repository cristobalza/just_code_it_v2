# Write your MySQL query statement below
/*
Loyalty score = (Number of transactions * 10) + (Total amount spent / 100).

The total amount spent. -> SUM(amount) over the customer
The number of transactions. -> COUNT(transaction_id) over the customer  
The number of unique product categories purchased. COUNT(DISTINCT category) over the customer
The average amount spent. AVG(amount) over the customer
The most frequently purchased product category (if there is a tie, choose the one with the most recent transaction).

1) JOIN tx and products together over product_id
2) Calculate above metrics
3) Find most frequently purchased category with tie-breaking
4) Return results ordered by loyalty score
*/

WITH tx_products_tbl AS (
    SELECT
        t.transaction_id,
        t.customer_id,
        t.product_id,
        t.transaction_date,
        t.amount, 
        p.category,
        p.price
    FROM Transactions t
    INNER JOIN Products p
        ON t.product_id = p.product_id
),

calculations_tbl AS (
    SELECT
        customer_id,
        ROUND(SUM(amount), 2) AS total_amount,
        COUNT(transaction_id) AS transaction_count,
        COUNT(DISTINCT category) AS unique_categories,
        ROUND(AVG(amount), 2) AS avg_transaction_amount,
        ROUND((COUNT(transaction_id) * 10) + (SUM(amount) / 100), 2) AS loyalty_score
    FROM tx_products_tbl
    GROUP BY customer_id
),

category_frequency AS (
    SELECT
        customer_id,
        category,
        COUNT(*) as category_count,
        MAX(transaction_date) as latest_transaction_date,
        RANK() OVER (
            PARTITION BY customer_id 
            ORDER BY COUNT(*) DESC, MAX(transaction_date) DESC
        ) as rn
    FROM tx_products_tbl
    GROUP BY customer_id, category
),

top_category AS (
    SELECT
        customer_id,
        category as top_category
    FROM category_frequency
    WHERE rn = 1
)

SELECT
    c.customer_id,
    c.total_amount,
    c.transaction_count,
    c.unique_categories,
    c.avg_transaction_amount,
    t.top_category,
    c.loyalty_score
FROM calculations_tbl c
LEFT JOIN top_category t
    ON c.customer_id = t.customer_id
ORDER BY 
    c.loyalty_score DESC, 
    c.customer_id ASC;