-- displays all records with score >= 10 
-- selects score and name columns
-- orders by score (top first)
-- db name is arg in ext command
SELECT score, `name`
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
