-- lists all records in a table in a db
-- lists their scores and names
-- ordered by scores (top first)
-- db name is arg in ext command
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
