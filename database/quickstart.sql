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
CREATE TABLE session_info (
	id INT NOT NULL AUTO_INCREMENT,
	num_businesses INT,
	num_houses INT,
	num_infrastructure INT,
	num_vehicles INT,
	num_solar INT,
	num_wind INT,
	session_current_time TIMESTAMP NOT NULL,
	PRIMARY KEY(id)
);

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	session_id INT NOT NULL,
	time TIMESTAMP,
	business INT,
	infrastructure INT,
	house INT,
	vehicle INT,
	PRIMARY KEY(id),
	FOREIGN KEY(session_id) REFERENCES session_info(id)
);

CREATE TABLE generators (
	id INT NOT NULL AUTO_INCREMENT,
	session_id INT NOT NULL,
	time TIMESTAMP,
	solar INT,
	wind INT,
	PRIMARY KEY(id),
	FOREIGN KEY(session_id) REFERENCES session_info(id)
);
