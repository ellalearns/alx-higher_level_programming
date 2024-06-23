-- uses a subquery to get ...
-- ... cities that are in a state
-- cities and states tables are different
-- 'cities' has a foreign key which is 'states' primary key
-- db name is arg in ext command
SELECT `id`, `name`
FROM `cities`
WHERE `state_id`
= (SELECT `id`
FROM `states`
WHERE `name` = 'California');
