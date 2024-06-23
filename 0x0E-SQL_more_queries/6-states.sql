-- creates a database and table
-- id col has unique values, is auto generated, can't be null, and is a primary key
-- name col can't be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    `id` INT UNIQUE AUTO_INCREMENT DEFAULT 1,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`)
);
