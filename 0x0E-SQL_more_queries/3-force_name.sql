-- create a mysql table with constraints
-- db name is arg in ext command
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT,
    `name` VARCHAR(256) NOT NULL
);
