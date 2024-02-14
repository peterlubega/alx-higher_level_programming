-- Root user
-- creating user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- granting all privilages
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- flush
FLUSH PRIVILEGES;
