DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS employee;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,

	income REAL NOT NULL DEFAULT 0.0,
	employee_salary REAL NOT NULL DEFAULT 0.0
);

CREATE TABLE employee (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	employer_id INTEGER NOT NULL,

	name TEXT UNIQUE NOT NULL,
	salary REAL DEFAULT NULL,

	FOREIGN KEY (employer_id) REFERENCES user (id)
);

