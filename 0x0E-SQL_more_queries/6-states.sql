-- Create database hbtn_0d_usa if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create table states if not exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
