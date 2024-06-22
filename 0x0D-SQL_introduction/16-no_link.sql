-- lists all records in a table
-- doesn't display rows without a name value
-- displays score and name
-- ordered by desc score
-- db name is arg in ext command
SELECT score, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY score DESC;
