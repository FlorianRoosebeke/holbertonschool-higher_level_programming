-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2
-- Usage: cat 0-privileges.sql | mysql -hlocalhost -uroot -p
SHOW GRANT for user_0d_1, user_0d_2 FROM localhost;