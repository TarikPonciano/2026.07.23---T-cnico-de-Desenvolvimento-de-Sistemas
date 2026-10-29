# Capítulo 5 · Prática guiada · main.py · Sistema da Loja Conecta
# Passos 3 a 6: CRUD de produtos, novo pedido (RETURNING + transação) e consultas.
# Antes de rodar: setup_loja.py já rodou e o .env está nesta pasta.

import psycopg
from classBanco import Banco

banco = Banco()


# ---- Funções ferramentas ----

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Preencha este campo.")


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números inteiros.")


def ler_decimal(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite apenas números.")


def ler_inteiro_ou_vazio(mensagem):
    # Devolve um número, ou None se a pessoa deixar vazio (None vira NULL no banco)
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            return None
        try:
            return int(texto)
        except ValueError:
            print("Digite um número inteiro ou deixe vazio.")


# ---- Produtos (Passos 3 e 4) ----

def ver_categorias():
    for cod, nome in banco.consultar("SELECT cod_categoria, nome_categoria FROM categorias ORDER BY cod_categoria"):
        print(f"  {cod}. {nome}")


def ver_produtos():
    print("PRODUTOS")
    linhas = banco.consultar("""
        SELECT p.cod_produto, p.nome_produto, p.preco, p.estoque, c.nome_categoria
        FROM produtos p
        LEFT JOIN categorias c ON c.cod_categoria = p.cod_categoria
        ORDER BY p.cod_produto
    """)
    for cod, nome, preco, estoque, categoria in linhas:
        if categoria is None:
            categoria = "sem categoria"
        print(f"{cod}. {nome} - R$ {preco:,.2f} - estoque {estoque} - {categoria}")


def buscar_produto(cod_produto):
    # Devolve (cod, nome, preco, estoque) ou None se o produto não existe
    linhas = banco.consultar(
        "SELECT cod_produto, nome_produto, preco, estoque FROM produtos WHERE cod_produto = %s",
        (cod_produto,),
    )
    if len(linhas) == 0:
        return None
    return linhas[0]


def cadastrar_produto():
    print("CADASTRO DE PRODUTO")
    nome = ler_texto("Nome: ")
    preco = ler_decimal("Preço: R$ ")
    estoque = ler_inteiro("Estoque: ")
    print("Categorias:")
    ver_categorias()
    cod_categoria = ler_inteiro_ou_vazio("Código da categoria (vazio = sem categoria): ")

    try:
        cod = banco.inserir(
            """INSERT INTO produtos (nome_produto, preco, estoque, cod_categoria)
               VALUES (%s, %s, %s, %s)
               RETURNING cod_produto""",
            (nome, preco, estoque, cod_categoria),
        )
        print(f"Produto cadastrado com o código {cod}.")
    except psycopg.errors.ForeignKeyViolation:
        print("Essa categoria não existe.")
    except psycopg.errors.CheckViolation:
        print("Preço e estoque não podem ser negativos.")


def alterar_produto():
    print("ALTERAR PREÇO E ESTOQUE")
    ver_produtos()
    produto = buscar_produto(ler_inteiro("Código do produto: "))
    if produto is None:
        print("Produto não encontrado.")
        return
    cod, nome, preco, estoque = produto

    print("Deixe vazio para manter o valor atual.")
    novo_preco = input(f"Preço [{preco}]: ").strip()
    novo_estoque = input(f"Estoque [{estoque}]: ").strip()
    try:
        if novo_preco != "":
            preco = float(novo_preco.replace(",", "."))
        if novo_estoque != "":
            estoque = int(novo_estoque)
    except ValueError:
        print("Preço e estoque precisam ser números. Nada foi alterado.")
        return

    try:
        banco.executar(
            "UPDATE produtos SET preco = %s, estoque = %s WHERE cod_produto = %s",
            (preco, estoque, cod),
        )
        print(f"{nome} atualizado.")
    except psycopg.errors.CheckViolation:
        print("Preço e estoque não podem ser negativos.")


def remover_produto():
    print("REMOVER PRODUTO")
    ver_produtos()
    cod = ler_inteiro("Código do produto: ")
    try:
        quantidade = banco.executar("DELETE FROM produtos WHERE cod_produto = %s", (cod,))
        if quantidade == 0:
            print("Produto não encontrado.")
        else:
            print("Produto removido.")
    except psycopg.errors.ForeignKeyViolation:
        print("Esse produto já foi vendido: ele fica no cadastro, por causa dos pedidos.")


# ---- Pedidos (Passos 5 e 6) ----

def ver_clientes():
    for cod, nome in banco.consultar("SELECT cod_cliente, nome_cliente FROM clientes ORDER BY cod_cliente"):
        print(f"  {cod}. {nome}")


def novo_pedido():
    print("NOVO PEDIDO")
    print("Clientes:")
    ver_clientes()
    cod_cliente = ler_inteiro("Código do cliente: ")

    # 1) Montar a lista de itens na memória, antes de gravar qualquer coisa
    itens = []
    while True:
        cod_produto = ler_inteiro("Código do produto (0 para fechar o pedido): ")
        if cod_produto == 0:
            break
        produto = buscar_produto(cod_produto)
        if produto is None:
            print("Produto não encontrado.")
            continue
        qtd = ler_inteiro(f"Quantidade de {produto[1]}: ")
        itens.append((cod_produto, qtd, produto[2]))

    if len(itens) == 0:
        print("Pedido sem itens: nada foi gravado.")
        return

    # 2) Gravar tudo numa transação só: pedido, itens e baixa no estoque
    conexao = banco.conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO pedidos (cod_cliente) VALUES (%s) RETURNING cod_pedido",
            (cod_cliente,),
        )
        cod_pedido = cursor.fetchone()[0]

        for cod_produto, qtd, preco in itens:
            cursor.execute(
                """INSERT INTO itens_pedido (cod_pedido, cod_produto, qtd, preco_unit)
                   VALUES (%s, %s, %s, %s)""",
                (cod_pedido, cod_produto, qtd, preco),
            )
            cursor.execute(
                "UPDATE produtos SET estoque = estoque - %s WHERE cod_produto = %s",
                (qtd, cod_produto),
            )

        conexao.commit()
        print(f"Pedido {cod_pedido} gravado com {len(itens)} item(ns).")

    except psycopg.errors.ForeignKeyViolation:
        conexao.rollback()
        print("Cliente não encontrado. Nada foi gravado.")
    except psycopg.errors.CheckViolation as erro:
        conexao.rollback()
        if erro.diag.constraint_name == "ck_estoque":
            print("Estoque insuficiente. Nada foi gravado.")
        else:
            print("A quantidade precisa ser maior que zero. Nada foi gravado.")
    except psycopg.errors.UniqueViolation:
        conexao.rollback()
        print("O mesmo produto entrou duas vezes: some as quantidades. Nada foi gravado.")
    finally:
        conexao.close()


def ver_pedido():
    print("VER PEDIDO")
    cod_pedido = ler_inteiro("Código do pedido: ")
    cabecalho = banco.consultar(
        """SELECT p.cod_pedido, c.nome_cliente, p.data_pedido, p.status
           FROM pedidos p
           JOIN clientes c ON c.cod_cliente = p.cod_cliente
           WHERE p.cod_pedido = %s""",
        (cod_pedido,),
    )
    if len(cabecalho) == 0:
        print("Pedido não encontrado.")
        return
    cod, cliente, data, status = cabecalho[0]
    print(f"Pedido {cod} · {cliente} · {data:%d/%m/%Y} · {status}")

    itens = banco.consultar(
        """SELECT pr.nome_produto, i.qtd, i.preco_unit, i.qtd * i.preco_unit AS subtotal
           FROM itens_pedido i
           JOIN produtos pr ON pr.cod_produto = i.cod_produto
           WHERE i.cod_pedido = %s
           ORDER BY i.cod_item""",
        (cod_pedido,),
    )
    total = 0
    for nome, qtd, preco_unit, subtotal in itens:
        print(f"  {qtd} x {nome} (R$ {preco_unit:,.2f}) = R$ {subtotal:,.2f}")
        total = total + subtotal
    if len(itens) == 0:
        print("  (sem itens)")
    print(f"Total: R$ {total:,.2f}")


def pedidos_do_cliente():
    print("PEDIDOS DE UM CLIENTE")
    ver_clientes()
    cod_cliente = ler_inteiro("Código do cliente: ")
    linhas = banco.consultar(
        """SELECT cod_pedido, data_pedido, status
           FROM pedidos
           WHERE cod_cliente = %s
           ORDER BY data_pedido""",
        (cod_cliente,),
    )
    if len(linhas) == 0:
        print("Nenhum pedido para esse cliente.")
    for cod, data, status in linhas:
        print(f"Pedido {cod} - {data:%d/%m/%Y} - {status}")


# ---- Menu principal ----

while True:
    print("""
LOJA CONECTA · SISTEMA

1. Ver produtos
2. Cadastrar produto
3. Alterar preço e estoque
4. Remover produto
5. Novo pedido
6. Ver pedido
7. Pedidos de um cliente

0. Sair
""")
    op = input("Digite a opção desejada: ")

    try:
        if op == "1":
            ver_produtos()
        elif op == "2":
            cadastrar_produto()
        elif op == "3":
            alterar_produto()
        elif op == "4":
            remover_produto()
        elif op == "5":
            novo_pedido()
        elif op == "6":
            ver_pedido()
        elif op == "7":
            pedidos_do_cliente()
        elif op == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")
    except psycopg.OperationalError:
        print("Sem conexão com o banco. Confira a internet e o arquivo .env.")

    input("Tecle ENTER para continuar")
