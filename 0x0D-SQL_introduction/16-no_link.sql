-- This script lists all records of the table second_table excluding rows without a name value
-- Results display the score and the name (in this order), listed by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
