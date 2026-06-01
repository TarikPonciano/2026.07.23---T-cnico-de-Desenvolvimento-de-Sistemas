# Lista que armazena os elementos
loja_informatica = [
    {"nome": "Notebook", "preço": 3500.00, "quantidade": 10},
    {"nome": "Smartphone", "preço": 1999.90, "quantidade": 25},
    {"nome": "Monitor 24", "preço": 850.00, "quantidade": 15},
    {"nome": "Teclado Mecânico", "preço": 299.90, "quantidade": 40},
    {"nome": "Mouse Gamer", "preço": 150.00, "quantidade": 50},
    {"nome": "Fone de Ouvido Bluetooth", "preço": 199.00, "quantidade": 30},
    {"nome": "Cadeira Ergonômica", "preço": 1200.00, "quantidade": 8},
    {"nome": "Webcam Full HD", "preço": 349.90, "quantidade": 12},
    {"nome": "Roteador Wi-Fi 6", "preço": 450.00, "quantidade": 20},
    {"nome": "SSD 1TB NVMe", "preço": 420.00, "quantidade": 18}
]


# ---- Funções Ferramentas ----
def validar_nome(nome_produto):
    if nome_produto == "":
        return False
    else:
        return True


def validar_preco(preco_produto):
    if preco_produto > 0:
        return True
    else:
        return False


# ---- Funcionalidades Específicas do Tema ----
def produtos_promocao():
    print("PRODUTOS EM PROMOÇÃO")
    
    for p in loja_informatica:
        if p['preço'] < 200:
           print(f"{p['nome']} | {p['preço']}")
    else:
        return 'Nenhum produto em promoção'

def calcular_estoque():
  total_estoque = 0
  print("ESTOQUE DE PRODUTOS")
  print("NOME | QUANTIDADE")
  for p in loja_informatica:
    estoque = p["preço"] * p["quantidade"]
    total_estoque += estoque
    print(f"{p["nome"]} | {p["quantidade"]}")
    
  print(f"Estoque total: {total_estoque:.2f}")

# ---- Operações CRUD ----
def cadastrar_produto():
    print("CADASTRAR PRODUTOS")
    
    while True:
        nome_produto = input("Digite o nome do produto: ")
        if not validar_nome(nome_produto):
            print("PREENCHA O CAMPO NOME!")
            continue
        else:
            break
        
    while True:
        preco_produto = input("Digite o preço do produto: ")
        preco_produto = float(preco_produto)
        
        if validar_preco(preco_produto) > 0:
            break
        else:
            print("PREÇO INVÁLIDO!")
            continue
        
    qtd_produto = input("Digite a quantidade do produto: ")

    novo_produto = {
        "nome": nome_produto,
        "preço": preco_produto,
        "quantidade": qtd_produto
    }

    loja_informatica.append(novo_produto)


def ver_produtos():
    print("VISUALIZAR PRODUTOS")
    for i, produto in enumerate(loja_informatica):
        print(f"{i+1}. {produto['nome']} | {produto['preço']} | {produto['quantidade']}")
    print()

def alterar_produtos():
    ver_produtos()

    num_produto = int(input("Digite o número do produto que deseja alterar: "))

    produto_escolhido = loja_informatica[num_produto - 1]

    novo_nome = input(f"Digite o novo nome ({produto_escolhido['nome']}): ")
    if novo_nome:
        produto_escolhido["nome"] = novo_nome

    novo_preco = input("Digite o novo preço : ")
    if novo_preco:
        produto_escolhido["preço"] = novo_preco

    nova_qtd = input("Digite a nova quantidade: ")
    if nova_qtd:
        produto_escolhido["quantidade"] = nova_qtd

    print(f"""
        INFORMAÇÕES DO PRODUTO:

        NOME: {produto_escolhido["nome"]}
        PREÇO: R${produto_escolhido['preço']}
        QUANTIDADE: {produto_escolhido['quantidade']}
    """)


def remover_produtos():
    ver_produtos()

    num_produto = int(input("Digite o numero do produto que você quer remover:"))

    produto_escolhido = loja_informatica[num_produto - 1]

    loja_informatica.remove(produto_escolhido)

    print(f"""
          Nome : {produto_escolhido["nome"]}
          Preço : {produto_escolhido["preço"]}
          Estoque : {produto_escolhido["quantidade"]}
    """)

    print("PRODUTO REMOVIDO COM SUCESSO!")
while True:

    print("""
        BEM VINDOS A LOJA DE INFORMÁTICA T&S

        1. CADASTRAR PRODUTOS
        2. VER PRODUTOS
        3. VER PRODUTOS EM PROMOÇÃO
        4. VER ESTOQUE
        5. ALTERAR PRODUTOS
        6. REMOVER PRODUTOS
        
        0. SAIR
    """)

    opcao = input("Digite a opcao desejada:")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        ver_produtos()

    elif opcao == "3":
        produtos_promocao()

    elif opcao == "4":
        calcular_estoque()
        
    elif opcao == "5":
        alterar_produtos()
        
    elif opcao == "6":
        remover_produtos()
        
    elif opcao == "0":
        print("Encerrando O Programa!")
        break
    
    input("TECLE ENTER PARA CONTINUAR")
    