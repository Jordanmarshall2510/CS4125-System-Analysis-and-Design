-- Create database
CREATE DATABASE smart_city;

-- Create user for simulation
CREATE USER "SimUser" IDENTIFIED BY "!Sim_Password21";

-- Switch to database
USE smart_city;

-- Grant user correct permissions
GRANT ALL PRIVILEGES ON smart_city.* TO "SimUser";
FLUSH PRIVILEGES;

-- create tables
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	user_type varchar(16) NOT NULL,
	power_used INTEGER not NULL,
	time TIMESTAMP,
	PRIMARY KEY(id)
);

CREATE TABLE generators (
	id INT NOT NULL AUTO_INCREMENT,
	generator_type varchar(16) NOT NULL,
	power_generated INTEGER not NULL,
	time TIMESTAMP,
	PRIMARY KEY(id)
);