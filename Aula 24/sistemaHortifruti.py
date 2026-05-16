# 6 — 🌱 Estoque de Hortifruti
# Atributos: produto, unidade (kg/unidade), quantidade em estoque, preço, fornecedor

# Funcionalidade extra: alertar quais produtos estão abaixo de uma quantidade mínima informada pelo usuário

produtos = [
    {
        "Nome": "Tomate",
        "Preço": 8.50,
        "Estoque": 120,
        "Unidade": "kg",
        "Fornecedor": "Verde Vida Hortifruti"
    },
    {
        "Nome": "Banana Prata",
        "Preço": 5.99,
        "Estoque": 200,
        "Unidade": "kg",
        "Fornecedor": "Frutas do Vale"
    },
    {
        "Nome": "Alface Americana",
        "Preço": 3.50,
        "Estoque": 80,
        "Unidade": "un",
        "Fornecedor": "Horta Natural"
    },
    {
        "Nome": "Batata Inglesa",
        "Preço": 6.75,
        "Estoque": 150,
        "Unidade": "kg",
        "Fornecedor": "Campo Fresco"
    },
    {
        "Nome": "Cenoura",
        "Preço": 4.20,
        "Estoque": 100,
        "Unidade": "kg",
        "Fornecedor": "Raízes da Terra"
    },
    {
        "Nome": "Maçã Gala",
        "Preço": 9.90,
        "Estoque": 90,
        "Unidade": "kg",
        "Fornecedor": "Pomar Central"
    },
    {
        "Nome": "Cebola",
        "Preço": 7.30,
        "Estoque": 130,
        "Unidade": "kg",
        "Fornecedor": "Sabor do Campo"
    },
    {
        "Nome": "Mamão Formosa",
        "Preço": 6.10,
        "Estoque": 60,
        "Unidade": "kg",
        "Fornecedor": "Frutas Tropicais"
    },
    {
        "Nome": "Cheiro Verde",
        "Preço": 2.80,
        "Estoque": 70,
        "Unidade": "molho",
        "Fornecedor": "Horta Feliz"
    },
    {
        "Nome": "Laranja Pera",
        "Preço": 4.99,
        "Estoque": 180,
        "Unidade": "kg",
        "Fornecedor": "Citrus Brasil"
    }
]

while True:
    print("BEM VINDO AO SISTEMA DE GERENCIAMENTO HORTIFRUTI SEU PEREIRA")

    print(f"""

MENU DE OPÇÕES:
          
    1. Cadastrar um produto
    2. Ver lista de produtos
    3. Ver produto específico
    4. Ver produtos pelo estoque mínimo

    0. Sair 
""")
    op = input("Digite a opção desejada: ")

    if op == "1":
        print("CADASTRO DE PRODUTO")

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        unidade = input("Digite o tipo de unidade (kg/und): ")
        estoque = int(input("Digite a quantidade do produto: "))
        fornecedor = input("Digite o fornecedor: ")

        novo_produto = {
            "Nome": nome,
            "Preço": preco,
            "Estoque": estoque,
            "Unidade": unidade,
            "Fornecedor": fornecedor
        }

        produtos.append(novo_produto)

        print("PRODUTO CADASTRADO COM SUCESSO")
        print(f"Produtos no Catálogo: {len(produtos)}")

        
    elif op == "2":
        print("VER PRODUTOS")
        contador = 1
        for produto in produtos:
            print(f"{contador}. {produto["Nome"]} | {produto["Estoque"]}")
            contador += 1

    elif op == "3":
        print("ESCOLHER PRODUTO")
        contador = 1
        for produto in produtos:
            print(f"{contador}. {produto["Nome"]} | {produto["Estoque"]}")
            contador += 1
        
        numero = int(input("Digite o número do produto que deseja visualizar: "))
        if numero == 0:
            print("CANCELANDO OPERAÇÃO")
        elif numero >= 1 and numero <= len(produtos):

            produto_escolhido = produtos[numero-1]

            print(f"""
    INFORMAÇÕES DO PRODUTO
        
        Nome: {produto_escolhido["Nome"]}
        Preço: R$ {produto_escolhido["Preço"]:,.2f}
        Estoque: {produto_escolhido["Estoque"]} {produto_escolhido["Unidade"]} 
        Fornecedor: {produto_escolhido["Fornecedor"]}

    """)
        else:
            print("DIGITE UM NÚMERO VÁLIDO")
        
    elif op == "4":
        print("VER PRODUTOS POR ESTOQUE")
        estoque_minimo = int(input("Digite o estoque mínimo: "))

        print("Nº | Nome | Estoque | Unidade")
        for i, produto in enumerate(produtos):
            if produto["Estoque"] <= estoque_minimo:
                print(f"{i+1} | {produto["Nome"]} | {produto["Estoque"]} | {produto["Unidade"]}")

                

    elif op == "0":
        print("ENCERRANDO PROGRAMA...")
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA")

    input("DIGITE ENTER PARA CONTINUAR...")