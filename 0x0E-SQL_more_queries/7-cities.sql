-- SDAFLKASDFNSLDKF


CREATE DATABASE IF NOT EXITS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id int UNIQUE NOT NULL AUTO_INCREMENT,
	state_id int NOT NULL,
	name varchar(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
	);

