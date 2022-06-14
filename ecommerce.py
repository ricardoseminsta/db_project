from multiprocessing import Condition
import sqlite3
from tabulate import tabulate
from datetime import datetime

connection = sqlite3.connect('ecommerce.db')
cursor = connection.cursor()

def list_costumers():
    cursor.execute("SELECT * FROM costumer;")
    print("\nLISTA DE CLIENTES")
    costumers = cursor.fetchall()
    return print(tabulate(costumers, headers=["id", "Nome", "CPF", "Email"]))

def set_costumer():
    print("\n\n\nCadastro de Clientes:\n")
    name = input("Digite um nome: ")
    cpf = int(input("Digite o cpf (apenas numeros): "))
    email = input("Digite o email: ")

    cursor.execute(f'INSERT INTO costumer (id_costumer, name, cpf, email) VALUES (NULL, ?, ?, ?);', (name, cpf, email))
    connection.commit()
    list_costumers()

def list_products():
    cursor.execute("SELECT * FROM product;")
    print("\n\nLISTA DE PRODUTOS")
    products = cursor.fetchall()
    return print(tabulate(products, headers=["ID", "Nome", "Preço"]))

def set_product():
    print("\n\n\nCadastro de Produtos:\n")
    name = input("Digite um nome: ")
    price = float(input("Digite o preco (apenas numeros ex: 12.3): "))

    cursor.execute(f'INSERT INTO product (id_product, name, price) VALUES (NULL, ?, ?);', (name, price))
    connection.commit()
    list_products()

def update_product():
    list_products()
    id = int(input("\n escolha um id para atualizar: "))
    new_price = float(input("\nEscolha um novo preço: "))
    cursor.execute(f'UPDATE product SET price = {new_price} WHERE id_product = {id};')
    connection.commit()
    list_products()

def set_purchase():
    data_atual = datetime.now()
    data_texto = data_atual.strftime("%Y-%m-%d")
    list_costumers()
    print("\nEscolha um cliente pelo nuemro do cpf")
    cpf = int(input("\nDigite o cpf do Cliente (apenas numeros): "))
    cursor.execute(f'SELECT id_costumer FROM costumer WHERE cpf = {cpf};')
    id = cursor.fetchone()
    cursor.execute(f'INSERT INTO purchase (id_purchase, id_costumer, date_purchase) VALUES (null, ?, ?);', (id[0], data_texto))
    connection.commit()

def set_order():
    set_purchase()

    out = False
    num = 0
    prods = []
    while out is False:
        if num == 0:
            list_products()
            id_product = int(input("\nDigite o id do produto: "))
            amount = int(input("\nDigite a quantidade: "))
            cursor.execute("SELECT id_purchase from purchase ORDER BY id_purchase DESC LIMIT 1;")
            last_purchase = cursor.fetchone();

            data = (id_product, last_purchase[0], amount)
            prods.append(data)

            num = int(input("\nDigite 0 para continuar adicionando itens: "))
        else:
            cursor.executemany(f'INSERT INTO product_purchase (id_product_purchase, id_product, id_purchase, product_amount) VALUES (null, ?, ?, ?);', prods)
            connection.commit()
            out = True

set_order()

connection.close()