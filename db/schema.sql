CREATE DATABASE IF NOT EXISTS urlshortener;

SET GLOBAL sql_mode = '';

USE urlshortener;

CREATE TABLE IF NOT EXISTS`urls` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created` TIMESTAMP(2) NOT NULL,
  `original_url` TEXT(100) NOT NULL,
  `clicks` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`))