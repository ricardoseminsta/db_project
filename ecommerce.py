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
    id = int(input("\nDigite o id do Cliente: "))
    cursor.execute(f'INSERT INTO purchase (id_purchase, id_costumer, date_purchase) VALUES (null, ?, ?);', (id, data_texto))
    connection.commit()
    cursor.execute("SELECT id_purchase from purchase ORDER BY id_purchase DESC LIMIT 1")
    last_purchase = cursor.fetchone();
    print("Selecione o produto")
    list_products()
    

connection.close()