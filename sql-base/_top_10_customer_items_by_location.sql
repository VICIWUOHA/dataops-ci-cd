WITH sales_summary AS (
    SELECT 
        l.location_name,
        c.customer_name,
        p.product_name,
        SUM(s.quantity_sold) as total_quantity_sold,
        SUM(s.total_amount) as total_sales_amount
    FROM 
        sales s
    JOIN 
        location l ON s.location_id = l.id
    JOIN 
        customer c ON s.customer_id = c.id
    JOIN 
        products p ON s.product_id = p.id
    GROUP BY 
        l.location_name, c.customer_name, p.product_name
)
SELECT *
FROM sales_summary
ORDER BY 
    location_name, total_sales_amount DESC, total_quantity_sold DESC
LIMIT 10;

