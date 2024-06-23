-- creates a table containing an id column 
-- id col has both default and unique constraints
-- db name is arg in ext command
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256)
);
