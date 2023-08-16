-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- List all cities with state names using a JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
