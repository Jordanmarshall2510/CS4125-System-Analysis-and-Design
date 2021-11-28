-- create
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	user_type varchar(16) NOT NULL,
	power_used INTEGER not NULL,
	time TIMESTAMP,
	PRIMARY KEY(id)
);

CREATE TABLE generators (
	id INT NOT NULL AUTO_INCREMENT,
	user_type varchar(16) NOT NULL,
	power_used INTEGER not NULL,
	time TIMESTAMP,
	PRIMARY KEY(id)
);