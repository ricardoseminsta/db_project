from multiprocessing import Condition
import sqlite3
from tabulate import tabulate
from datetime import datetime

connection = sqlite3.connect('ecommerce.db')
cursor = connection.cursor()

# função que lista os clientes
def list_costumers():
    cursor.execute("SELECT * FROM costumer;")
    print("\nLISTA DE CLIENTES")
    costumers = cursor.fetchall()
    return print(tabulate(costumers, headers=["id", "Nome", "CPF", "Email"]))

# função que cadastra os clientes
def set_costumer():
    print("\n\n\nCadastro de Clientes:\n")
    name = input("Digite um nome: ")
    cpf = int(input("Digite o cpf (apenas numeros): "))
    email = input("Digite o email: ")

    cursor.execute(f'INSERT INTO costumer (id_costumer, name, cpf, email) VALUES (NULL, ?, ?, ?);', (name, cpf, email))
    connection.commit()
    list_costumers()

# função que lista os produtos
def list_products():
    cursor.execute("SELECT * FROM product;")
    print("\n\nLISTA DE PRODUTOS")
    products = cursor.fetchall()
    return print(tabulate(products, headers=["ID", "Nome", "Preço"]))

# função que cadastra produtos
def set_product():
    print("\n\n\nCadastro de Produtos:\n")
    name = input("Digite um nome: ")
    price = float(input("Digite o preco (apenas numeros ex: 12.3): "))

    cursor.execute(f'INSERT INTO product (id_product, name, price) VALUES (NULL, ?, ?);', (name, price))
    connection.commit()
    list_products()

# função que atualiza um produto selecionando pelo id
def update_product():
    list_products()
    id = int(input("\n escolha um id para atualizar: "))
    new_price = float(input("\nEscolha um novo preço: "))
    cursor.execute(f'UPDATE product SET price = {new_price} WHERE id_product = {id};')
    connection.commit()
    list_products()

#função que set uma compra a um cpf com uma data (só será utilizada pelo set_order)
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


# função adiciona vários produtos a uma compra aberta (set_purchase)
def set_order():
    set_purchase()

    # saída do loop out e num
    out = False
    num = 0
    # lista de produtos prods
    prods = []
    while out is False:
        if num == 0:
            list_products()
            id_product = int(input("\nDigite o id do produto: "))
            amount = int(input("\nDigite a quantidade: "))
            
            # pega o id da compra mais recente setada no set_purchase inicial
            cursor.execute("SELECT id_purchase from purchase ORDER BY id_purchase DESC LIMIT 1;")
            last_purchase = cursor.fetchone();

            # monta a tupla
            data = (id_product, last_purchase[0], amount)
            # adiciona na lista
            prods.append(data)
            num = int(input("\nDigite 0 para continuar adicionando itens: "))
        else:
            cursor.executemany(f'INSERT INTO product_purchase (id_product_purchase, id_product, id_purchase, product_amount) VALUES (null, ?, ?, ?);', prods)
            connection.commit()
            out = True

def report_order():
    list_costumers()
    cpf = int(input('\n\nDigite o CPF do cliente: '))
    cursor.execute(f"SELECT pur.id_purchase as compra,cos.name, pur.date_purchase as data_compra, sum(prod.price * pp.product_amount) as soma from purchase pur JOIN costumer cos ON pur.id_costumer = cos.id_costumer JOIN product_purchase pp on pp.id_purchase = pur.id_purchase JOIN product prod on prod.id_product = pp.id_product WHERE cos.cpf = {cpf} GROUP BY pur.id_purchase")
    orders = cursor.fetchall()
    return print(tabulate(orders, headers=["id compra", "Nome do Cliente", "Data da compra", "Valor da Compra"]))

def detail_order():
    report_order()
    id = int(input("\n\nEscolha o id de um Pedido: "))
    cursor.execute(f"SELECT pro.name as nome_produto, pp.product_amount as qtd, pro.price, sum(pp.product_amount * pro.price) as subtotal FROM product pro JOIN product_purchase pp on pp.id_product = pro.id_product JOIN purchase pur on pur.id_purchase = pp.id_purchase WHERE pur.id_purchase = {id} GROUP BY pro.id_product")
    order = cursor.fetchall()
    return print(tabulate(order, headers=["id Produto", "Nome do Produto", "Preço", "SubTotal"]))

def start_menu():
    print("\n\n ECOMMERCE DO MAL:\n")
    op = [
        (1, "CADASTRAR CLIENTE"),
        (2, "CADASTRAR PRODUTO"),
        (3, "ATUALIZAR PREÇO PRODUTO"),
        (4, "COMPRAR"),
        (5, "DETALHAMENTO DE PEDIDOS")
    ]
    print(tabulate(op, headers = ["CÓD", "OPERAÇÃO"]))

    operation = int(input("\n SELECIONE A OPERAÇÃO: "))

    if(operation == 1):
        set_costumer()
    elif(operation == 2):
        set_product()
    elif(operation == 3):
        update_product()
    elif(operation == 4):
        set_order()
    elif(operation == 5):
        detail_order()
    else:
        print("\n saindo ...")

start_menu()
connection.close()