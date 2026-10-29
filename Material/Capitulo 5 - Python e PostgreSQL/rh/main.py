# Capítulo 5 · main.py · Sistema RH com banco de dados
# O Sistema de Funcionários da UC 1, agora guardando os dados no PostgreSQL.
# A lista de dicionários e o dados.json saem; cada operação vira um comando SQL.
# Antes de rodar: setup_rh.py já rodou e o .env está nesta pasta.

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


def gravar(sql, parametros):
    # Roda o INSERT ou o UPDATE e traduz as regras do banco em mensagens
    try:
        banco.executar(sql, parametros)
        return True
    except psycopg.errors.UniqueViolation:
        print("CPF já cadastrado. Tente outro número.")
    except psycopg.errors.ForeignKeyViolation:
        print("Esse setor não existe.")
    except psycopg.errors.CheckViolation as erro:
        if erro.diag.constraint_name == "ck_cpf_tamanho":
            print("O CPF precisa ter 11 dígitos.")
        else:
            print("O salário precisa ser maior que zero.")
    return False


# ---- Operações CRUD ----

def ver_setores():
    for cod, nome in banco.consultar("SELECT cod_setor, nome_setor FROM setores ORDER BY cod_setor"):
        print(f"  {cod}. {nome}")


def cadastrar_funcionario():
    print("CADASTRO DE FUNCIONÁRIOS")
    nome = ler_texto("Nome: ")
    cpf = ler_texto("CPF (só números): ")
    cargo = ler_texto("Cargo: ")
    salario = ler_decimal("Salário: R$ ")
    print("Setores:")
    ver_setores()
    cod_setor = ler_inteiro("Código do setor: ")

    ok = gravar(
        """INSERT INTO funcionarios
             (nome_funcionario, cpf_funcionario, cargo_funcionario, salario_funcionario, cod_setor)
           VALUES (%s, %s, %s, %s, %s)""",
        (nome, cpf, cargo, salario, cod_setor),
    )
    if ok:
        print(f"{nome} foi cadastrado(a)!")


def ver_funcionarios():
    print("LISTA DE FUNCIONÁRIOS")
    linhas = banco.consultar("""
        SELECT f.cod_funcionario, f.nome_funcionario, f.cargo_funcionario,
               f.salario_funcionario, s.nome_setor
        FROM funcionarios f
        JOIN setores s ON s.cod_setor = f.cod_setor
        ORDER BY f.nome_funcionario
    """)
    if len(linhas) == 0:
        print("Nenhum funcionário cadastrado.")
    for cod, nome, cargo, salario, setor in linhas:
        print(f"{cod}. {nome} - {cargo} - R$ {salario:,.2f} - {setor}")


def escolher_funcionario():
    # Devolve a linha do funcionário escolhido, ou None se o código não existe
    ver_funcionarios()
    cod = ler_inteiro("Código do funcionário: ")
    linhas = banco.consultar(
        """SELECT cod_funcionario, nome_funcionario, cargo_funcionario,
                  salario_funcionario, cod_setor
           FROM funcionarios
           WHERE cod_funcionario = %s""",
        (cod,),
    )
    if len(linhas) == 0:
        print("Nenhum funcionário com esse código.")
        return None
    return linhas[0]


def alterar_funcionario():
    print("ALTERAR FUNCIONÁRIO")
    funcionario = escolher_funcionario()
    if funcionario is None:
        return
    cod, nome, cargo, salario, cod_setor = funcionario
    print("Deixe vazio para manter o valor atual.")
    novo_nome = input(f"Nome [{nome}]: ").strip()
    novo_cargo = input(f"Cargo [{cargo}]: ").strip()
    novo_salario = input(f"Salário [{salario}]: ").strip()
    novo_setor = input(f"Setor [{cod_setor}]: ").strip()

    if novo_nome != "":
        nome = novo_nome
    if novo_cargo != "":
        cargo = novo_cargo
    try:
        if novo_salario != "":
            salario = float(novo_salario.replace(",", "."))
        if novo_setor != "":
            cod_setor = int(novo_setor)
    except ValueError:
        print("Salário e setor precisam ser números. Nada foi alterado.")
        return
    ok = gravar(
        """UPDATE funcionarios SET nome_funcionario = %s, cargo_funcionario = %s,
               salario_funcionario = %s, cod_setor = %s WHERE cod_funcionario = %s""",
        (nome, cargo, salario, cod_setor, cod),
    )
    if ok:
        print("Dados atualizados!")


def remover_funcionario():
    print("REMOVER FUNCIONÁRIO")
    funcionario = escolher_funcionario()
    if funcionario is None:
        return
    cod = funcionario[0]
    nome = funcionario[1]

    resposta = input(f"Remover {nome}? (s/n) ").strip().lower()
    if resposta == "s":
        banco.executar("DELETE FROM funcionarios WHERE cod_funcionario = %s", (cod,))
        print(f"{nome} foi removido(a).")
    else:
        print("Nada foi removido.")


# ---- Funcionalidade extra ----

def buscar_por_nome():
    termo = ler_texto("Parte do nome: ")
    linhas = banco.consultar(
        """SELECT nome_funcionario, cargo_funcionario
           FROM funcionarios
           WHERE nome_funcionario ILIKE %s
           ORDER BY nome_funcionario""",
        ("%" + termo + "%",),
    )
    if len(linhas) == 0:
        print("Ninguém encontrado.")
    for nome, cargo in linhas:
        print(f"{nome} - {cargo}")


# ---- Menu principal ----

while True:
    print("""
SISTEMA RH · BANCO DE DADOS

1. Cadastrar funcionário
2. Ver funcionários
3. Alterar funcionário
4. Remover funcionário
5. Buscar por nome

0. Sair
""")
    op = input("Digite a opção desejada: ")

    try:
        if op == "1":
            cadastrar_funcionario()
        elif op == "2":
            ver_funcionarios()
        elif op == "3":
            alterar_funcionario()
        elif op == "4":
            remover_funcionario()
        elif op == "5":
            buscar_por_nome()
        elif op == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")
    except psycopg.OperationalError:
        print("Sem conexão com o banco. Confira a internet e o arquivo .env.")

    input("Tecle ENTER para continuar")
