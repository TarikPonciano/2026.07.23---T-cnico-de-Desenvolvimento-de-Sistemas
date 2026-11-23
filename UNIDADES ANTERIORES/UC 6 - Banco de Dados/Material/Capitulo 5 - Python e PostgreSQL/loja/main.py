# Capítulo 5 · Prática guiada · main.py · Sistema da Loja Conecta
#
# Requisito 1 · CRUD completo da tabela produtos:
#     Ver produtos, Ver detalhes, Cadastrar, Alterar e Apagar
# Requisito 2 · Fluxo de venda:
#     escolher o cliente, montar a lista de itens e gravar o pedido e os itens
#     com o método registrarVenda da classe Banco (uma transação só)

from classBanco import Banco

banco = Banco()


# ---------------- Requisito 1 · CRUD de produtos ----------------

def verCategorias():
    print("CATEGORIAS")
    for cod, nome in banco.consultar("SELECT * FROM categorias ORDER BY cod_categoria;"):
        print(f"{cod} | {nome}")


def verProdutos():
    print("LISTA DE PRODUTOS")

    produtos = banco.consultar('''
        SELECT p.cod_produto, p.nome_produto, p.preco, p.estoque, c.nome_categoria
        FROM produtos p
        LEFT JOIN categorias c ON c.cod_categoria = p.cod_categoria
        ORDER BY p.cod_produto;
    ''')

    if (len(produtos) == 0):
        print("NÃO HÁ PRODUTOS CADASTRADOS")
        return

    print("Código | Produto | Preço | Estoque | Categoria")
    for cod, nome, preco, estoque, categoria in produtos:
        # LEFT JOIN: produto sem categoria chega com None
        if (categoria is None):
            categoria = "sem categoria"
        print(f"{cod} | {nome} | R$ {preco:,.2f} | {estoque} | {categoria}")


def escolherProduto():
    verProdutos()

    cod_escolhido = int(input("Digite o código do produto desejado: "))

    consulta = banco.consultar('''
        SELECT p.cod_produto, p.nome_produto, p.preco, p.estoque, p.cod_categoria, c.nome_categoria
        FROM produtos p
        LEFT JOIN categorias c ON c.cod_categoria = p.cod_categoria
        WHERE p.cod_produto = %s;
    ''', (cod_escolhido,))

    if (len(consulta) == 0):
        print("Produto não encontrado!")
        return None

    produto = consulta[0]

    print(f'''
    Ficha do Produto:

    Código: {produto[0]}
    Nome: {produto[1]}
    Preço: R$ {produto[2]:,.2f}
    Estoque: {produto[3]}
    Categoria: {produto[5] if produto[5] else "sem categoria"}
    ''')

    return produto


def cadastrarProduto():
    print("CADASTRO DE NOVO PRODUTO")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    estoque = int(input("Digite o estoque: "))

    verCategorias()
    categoria = input("Digite o código da categoria (vazio = sem categoria): ").strip()

    # Vazio vira None, e o banco grava NULL: a FK aceita
    cod_categoria = None
    if (categoria):
        cod_categoria = int(categoria)

    try:
        banco.manipular('''
            INSERT INTO produtos
            VALUES (default, %s, %s, %s, %s);
        ''', (nome, preco, estoque, cod_categoria))
        print("PRODUTO CADASTRADO COM SUCESSO!")
    except Exception as error:
        print("ERRO AO CADASTRAR PRODUTO")


def alterarProduto():
    print("ATUALIZAÇÃO DE PRODUTO")

    produto = escolherProduto()

    if (not produto):
        print("Não é possível alterar o produto. Cheque o código escolhido...")
        return

    continuar = input("Deseja alterar as informações do produto? (S/N) ")

    if (continuar != "S"):
        return

    cod, nome, preco, estoque, cod_categoria, nome_categoria = produto

    print("ALTERAR DADOS:")
    print("(Deixe vazio para manter o original)")

    novo_nome = input(f"Digite o novo nome ({nome}): ").strip()
    if (novo_nome):
        nome = novo_nome

    novo_preco = input(f"Digite o novo preço (R$ {preco:,.2f}): ").strip()
    if (novo_preco):
        preco = float(novo_preco)

    novo_estoque = input(f"Digite o novo estoque ({estoque}): ").strip()
    if (novo_estoque):
        estoque = int(novo_estoque)

    verCategorias()
    nova_categoria = input(f"Digite o código da nova categoria ({cod_categoria}): ").strip()
    if (nova_categoria):
        cod_categoria = int(nova_categoria)

    try:
        banco.manipular('''
            UPDATE produtos
            SET nome_produto = %s,
                preco = %s,
                estoque = %s,
                cod_categoria = %s
            WHERE cod_produto = %s;
        ''', (nome, preco, estoque, cod_categoria, cod))
        print("PRODUTO ATUALIZADO!")
    except Exception as error:
        print("Ocorreu um erro na atualização!")


def removerProduto():
    print("REMOÇÃO DE PRODUTO")

    produto = escolherProduto()

    if (not produto):
        print("Produto não encontrado!")
        return

    continuar = input("DESEJA REALMENTE APAGAR ESSE PRODUTO? (S/N) ")

    if (continuar != "S"):
        print("Cancelando operação...")
        return

    try:
        banco.manipular('''
            DELETE FROM produtos
            WHERE cod_produto = %s;
        ''', (produto[0],))
        print("Produto removido com sucesso!")
    except Exception as error:
        # Produto que já foi vendido não sai: a FK fk_item_produto recusa
        print("Não foi possível remover o produto! Ele já foi vendido?")


# ---------------- Requisito 2 · Fluxo de venda ----------------

def verClientes():
    print("CLIENTES")
    for cod, nome in banco.consultar("SELECT cod_cliente, nome_cliente FROM clientes ORDER BY cod_cliente;"):
        print(f"{cod} | {nome}")


def cadastrarVenda():
    print("NOVA VENDA")

    # 1. O cliente
    verClientes()
    cod_cliente = int(input("Digite o código do cliente: "))

    # 2. Os itens: montados numa lista, antes de gravar qualquer coisa
    itens = []
    verProdutos()

    while (True):
        cod_produto = int(input("Código do produto (0 para fechar a venda): "))

        if (cod_produto == 0):
            break

        consulta = banco.consultar('''
            SELECT cod_produto, nome_produto, preco FROM produtos
            WHERE cod_produto = %s;
        ''', (cod_produto,))

        if (len(consulta) == 0):
            print("Produto não encontrado!")
            continue

        cod, nome, preco = consulta[0]
        qtd = int(input(f"Quantidade de {nome}: "))

        # O preço do dia vai junto: é o preco_unit do item
        itens.append((cod, qtd, preco))
        print(f"{qtd} x {nome} na venda.")

    if (len(itens) == 0):
        print("Venda sem itens. Nada foi gravado.")
        return

    # 3. Gravar: o pedido e os itens juntos, pelo método da classe
    try:
        cod_pedido = banco.registrarVenda(cod_cliente, itens)
        print(f"VENDA {cod_pedido} REGISTRADA COM {len(itens)} ITEM(NS)!")
    except Exception as error:
        print("Não foi possível registrar a venda. Nada foi gravado.")


def verVenda():
    print("DETALHES DA VENDA")

    cod_pedido = int(input("Digite o código da venda: "))

    consulta = banco.consultar('''
        SELECT p.cod_pedido, c.nome_cliente, p.data_pedido, p.status
        FROM pedidos p
        JOIN clientes c ON c.cod_cliente = p.cod_cliente
        WHERE p.cod_pedido = %s;
    ''', (cod_pedido,))

    if (len(consulta) == 0):
        print("Venda não encontrada!")
        return

    cod, cliente, data, status = consulta[0]
    print(f"Venda {cod} | {cliente} | {data:%d/%m/%Y} | {status}")

    itens = banco.consultar('''
        SELECT pr.nome_produto, i.qtd, i.preco_unit, i.qtd * i.preco_unit
        FROM itens_pedido i
        JOIN produtos pr ON pr.cod_produto = i.cod_produto
        WHERE i.cod_pedido = %s
        ORDER BY i.cod_item;
    ''', (cod_pedido,))

    total = 0
    for nome, qtd, preco_unit, subtotal in itens:
        print(f"  {qtd} x {nome} (R$ {preco_unit:,.2f}) = R$ {subtotal:,.2f}")
        total = total + subtotal

    if (len(itens) == 0):
        print("  (sem itens)")

    print(f"TOTAL: R$ {total:,.2f}")


while (True):
    print('''
    LOJA CONECTA

    MENU:

    1. Ver Produtos
    2. Ver Detalhes do Produto
    3. Cadastrar Produto
    4. Alterar Produto
    5. Apagar Produto

    11. Nova Venda
    12. Ver Venda

    0. Sair
    ''')

    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA: ")

    if (op == "1"):
        verProdutos()
    elif (op == "2"):
        escolherProduto()
    elif (op == "3"):
        cadastrarProduto()
    elif (op == "4"):
        alterarProduto()
    elif (op == "5"):
        removerProduto()
    elif (op == "11"):
        cadastrarVenda()
    elif (op == "12"):
        verVenda()
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")

    input("TECLE ENTER PARA CONTINUAR")
