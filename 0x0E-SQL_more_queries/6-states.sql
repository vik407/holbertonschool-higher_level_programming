-- A script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- The table hbtn_0d_usa.states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
-- Fields
(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
