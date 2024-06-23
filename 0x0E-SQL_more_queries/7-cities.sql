-- creates a database and table
-- table contains columns with constraints
-- primary key and foreign key are declared
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    PRIMARY KEY(`id`),
    `id` INT NOT NULL UNIQUE AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`),
    `name` VARCHAR(256) NOT NULL
);
