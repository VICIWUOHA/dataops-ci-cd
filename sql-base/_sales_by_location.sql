--

-- to get sales by loc
SELECT l.location_name, SUM(s.amount) sales
FROM locations l
LEFT JOIN sales s
ON l.id = s.location_id
GROUP BY l.location_name