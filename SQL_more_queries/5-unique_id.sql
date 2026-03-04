-- Creates MySQL user user_0d_1 with all privileges.
CREATE DATABASE IF NOT EXISTS unique_id
(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
