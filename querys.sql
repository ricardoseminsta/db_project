SELECT * FROM costumer;

SELECT id_costumer FROM costumer WHERE cpf = 55555;

SELECT pur.id_purchase as compra,pur.date_purchase as data_compra, cos.name, sum(prod.price * pp.product_amount) as soma from purchase pur
JOIN costumer cos ON pur.id_costumer = cos.id_costumer
JOIN product_purchase pp on pp.id_purchase = pur.id_purchase
JOIN product prod on prod.id_product = pp.id_product
GROUP BY pur.id_purchase

SELECT pp.id_purchase, pur.date_purchase, count(id_product)  FROM product_purchase pp
JOIN purchase pur on pur.id_purchase = pp.id_purchase
WHERE pp.id_purchase = 1

SELECT pur.id_purchase as compra,cos.name, pur.date_purchase as data_compra, sum(prod.price * pp.product_amount) as soma from purchase pur
JOIN costumer cos ON pur.id_costumer = cos.id_costumer
JOIN product_purchase pp on pp.id_purchase = pur.id_purchase
JOIN product prod on prod.id_product = pp.id_product
WHERE cos.cpf = 55555
GROUP BY pur.id_purchase

SELECT pro.name as nome_produto, pp.product_amount as qtd, pro.price, sum(pp.product_amount * pro.price) as subtotal FROM product pro
JOIN product_purchase pp on pp.id_product = pro.id_product
JOIN purchase pur on pur.id_purchase = pp.id_purchase
WHERE pur.id_purchase = 1
GROUP BY pro.id_product
