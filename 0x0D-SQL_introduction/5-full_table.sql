/* 
Prints the full description of the table first_table from the specified database
Note: Replace 'your_database_name' with the actual database name.
*/

SELECT table_name, CREATE_TABLE
FROM information_schema.tables
WHERE table_schema = 'your_database_name' AND table_name = 'first_table';

