-- A script that lists all records of the table second_table
SELECT score, name FROM second_table
-- Don’t list rows without a name value
WHERE name IS NOT NULL
ORDER BY score DESC;