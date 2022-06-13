CREATE TABLE costumer (
	id_costumer INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	cpf INTEGER NOT NULL UNIQUE,
	email TEXT NOT NULL UNIQUE
);

CREATE TABLE product (
	id_product INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	price REAL NOT NULL
);

CREATE table purchase (
	id_purchase INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_costumer INTEGER NOT NULL,
	date_purchase date NOT NULL,
	FOREIGN KEY (id_costumer) REFERENCES costumer(id_costumer) on DELETE CASCADE
);

CREATE TABLE product_purchase (
	id_product_purchase INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_product INTEGER NOT NULL,
	id_purchase INTEGER NOT NULL,
	product_amount INTEGER NOT NULL,
	
	FOREIGN KEY (id_product) REFERENCES product(id_product) on DELETE CASCADE,
	FOREIGN KEY (id_purchase) REFERENCES purchase(id_purchase) on DELETE CASCADE
);