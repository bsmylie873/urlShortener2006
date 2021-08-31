SET GLOBAL sql_mode = '';

USE urlshortener;

CREATE TABLE IF NOT EXISTS`urls` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `original_url` TEXT(100) NOT NULL,
  `clicks` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`))