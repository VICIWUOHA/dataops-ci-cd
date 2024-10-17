--

SELECT
    l.loaction_name,
    SUM(s.amount) AS sales
FROM locations AS l
LEFT JOIN sales AS s
    ON l.id = s.location_id
GROUP BY l.loaction_name
