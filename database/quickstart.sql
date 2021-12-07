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
	session_id INT NOT NULL,
	user_type varchar(16) NOT NULL,
	power_used INTEGER not NULL,
	time TIMESTAMP,
	PRIMARY KEY(id),
	FOREIGN KEY(session_id) REFERENCES session_info(id)
);

CREATE TABLE generators (
	id INT NOT NULL AUTO_INCREMENT,
	session_id INT NOT NULL,
	generator_type varchar(16) NOT NULL,
	power_generated INTEGER not NULL,
	time TIMESTAMP,
	PRIMARY KEY(id),
	FOREIGN KEY(session_id) REFERENCES session_info(id)
);

CREATE TABLE session_info (
  id INT NOT NULL AUTO_INCREMENT,
  num_businesses INT,
  num_houses INT,
  num_infrastructure INT,
  num_vehicles INT,
  num_solar INT,
  num_wind INT,
  current_time TIMESTAMP NOT NULL
);