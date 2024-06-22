-- lists the number of records with the same score
-- together with new column named number
-- sorted by number of records descending
-- db name is arg in ext command
SELECT `score`, COUNT(`score`) AS `number`
FROM second_table
GROUP BY `number`
ORDER BY `number` DESC;
