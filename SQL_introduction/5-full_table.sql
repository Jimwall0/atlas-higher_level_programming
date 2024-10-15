-- Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA 
FROM information_schema.COLUMNS 
WHERE TABLE_SCHEMA = 'hbtn_0c_0' 
AND TABLE_NAME = 'first_table';
