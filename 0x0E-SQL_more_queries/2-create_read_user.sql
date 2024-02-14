-- Read user Concept
-- Creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creating User if not existing
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Granting only SELECT ACCESS
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
