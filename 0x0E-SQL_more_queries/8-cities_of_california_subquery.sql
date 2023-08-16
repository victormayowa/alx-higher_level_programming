-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- List cities of California using a subquery
SELECT * FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id;
