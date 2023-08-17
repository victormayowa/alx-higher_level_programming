-- List all cities with state names using a JOIN
SELECT cities.id, cities.name, states.name
	FROM cities INNER JOIN states
		ON cities.state_id = states.id
ORDER BY cities.id;
