WITH sales_summary AS (
    SELECT
        l.location_name,
        c.customer_name,
        p.product_name,
        SUM(s.quantity_sold) AS total_quantity_sold,
        SUM(s.total_amount) AS total_sales_amount
    FROM sales AS s
    INNER JOIN
        location AS l ON s.location_id = l.id
    INNER JOIN
        customer AS c ON s.customer_id = c.id
    INNER JOIN
        products AS p ON s.product_id = p.id
    GROUP BY
        l.location_name, c.customer_name, p.product_name
)

SELECT *
FROM sales_summary
ORDER BY
    location_name ASC, total_sales_amount DESC, total_quantity_sold DESC
LIMIT 10;
