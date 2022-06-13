INSERT INTO costumer (id_costumer, name, cpf, email)
	VALUES	(NULL, "Ricardo", 111111, "ricardo@gmail.com"),
			(NULL, "José", 222, "jose@gmail.com"),
			(NULL, "Maria", 33333, "maria@gmail.com");
			
INSERT INTO product (id_product, name, price)
	VALUES	(NULL, "feijão", 5),
			(NULL, "arroz", 3.3),
			(NULL, "macarrao", 5.5),
			(NULL, "sal", .7);
			
INSERT INTO purchase (id_purchase, id_costumer, date_purchase)
	VALUES	(null, 1, "2022-06-12"),
			(null, 1, "2022-06-12"),
			(null, 2, "2022-06-13"),
			(null, 2, "2022-06-12");

INSERT INTO product_purchase (id_product_purchase, id_product, id_purchase, product_amount)
	VALUES	(null, 1, 1, 10),
			(null, 2, 1, 2),
			(null, 3, 1, 2),
			(null, 3, 2, 1),
			(null, 4, 2, 2);