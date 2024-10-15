-- Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT 
    COLUMN_NAME, 
    DATA_TYPE, 
    IS_NULLABLE, 
    COLUMN_DEFAULT, 
    CHARACTER_MAXIMUM_LENGTH 
FROM 
    information_schema.columns 
WHERE 
    table_schema = 'hbtn_0c_0' 
    AND table_name = 'first_table';