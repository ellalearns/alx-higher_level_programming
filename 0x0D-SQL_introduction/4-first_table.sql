-- creates table if it doesn't exist yet
-- db name is passed as arg in ext command 
-- has two columns: id and name
CREATE TABLE IF NOT EXISTS `first_table` (
    `id` INT,
    `name` VARCHAR(256)
);
