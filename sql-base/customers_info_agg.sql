SELECT
    c.id,
    c.customer_name,
    SUM(s.amount) AS lifetime_value,
    AVG(s.amount) AS avg_spend,
    COUNT(s.id) AS no_of_orders,
    COUNT(DISTINCT s.product_id) AS unique_product_count
FROM customers AS c
LEFT JOIN sales AS s ON c.id = s.customer_id
GROUP BY 1, 2
--
HAVING SUM(s.amount) > 0 --business is only in cutomers who have spent cash
