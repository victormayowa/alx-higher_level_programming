-- List cities of California using a subquery
SELECT id, name, cities
FROM cities
WHERE state_id = (
    SELECT id
	FROM states
    WHERE name = 'California'
)
ORDER BY id;
