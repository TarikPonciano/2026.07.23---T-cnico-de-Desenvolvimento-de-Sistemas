# Capítulo 5 · Gabarito da Prática 2 · sistema_cinema.py · ainda sem classe
#
# 1. Criar um aplicativo Python para visualizar os dados do cinema
# 2. As opções do menu devem ser:
#     1 - Ver Filmes
#     2 - Ver Sessões
#     3 - Cadastrar novo filme
#     4 - Cadastrar nova sessão
# 3. Funcionalidades extras:
#     - Ver detalhes de um filme (a pessoa escolhe um filme da lista e vê só as informações dele)
#     - Ao ver as sessões, exibir o nome do filme de cada sessão
#
# Para não repetir a conexão em cada opção, ela foi para duas funções:
# consultarBanco (SELECT) e manipularBanco (INSERT, UPDATE, DELETE).

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def consultarBanco(sql, parametros=()):
    conexaoDB = None
    cursor = None

    try:
        conexaoDB = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname="cinema",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode=os.getenv("DB_SSL")
        )
        cursor = conexaoDB.cursor()

        cursor.execute(sql, parametros)

        return cursor.fetchall()
    except Exception as error:
        print("ERRO AO CONSULTAR BANCO")
        print(error)
        if (conexaoDB is not None):
            conexaoDB.rollback()
        return None
    finally:
        if (cursor is not None):
            cursor.close()
        if (conexaoDB is not None):
            conexaoDB.close()


def manipularBanco(sql, parametros=()):
    conexaoDB = None
    cursor = None

    try:
        conexaoDB = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname="cinema",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode=os.getenv("DB_SSL")
        )
        cursor = conexaoDB.cursor()

        cursor.execute(sql, parametros)

        conexaoDB.commit()

        return True
    except Exception as error:
        print("ERRO AO MANIPULAR BANCO")
        print(error)
        if (conexaoDB is not None):
            conexaoDB.rollback()
        return False
    finally:
        if (cursor is not None):
            cursor.close()
        if (conexaoDB is not None):
            conexaoDB.close()


def verFilmes():
    print("LISTA DE FILMES")
    filmes = consultarBanco("SELECT * FROM filmes ORDER BY cod_filme;")

    if (filmes is None):
        return

    print("Código | Título | Duração | Classificação")
    for f in filmes:
        print(f"{f[0]} | {f[1]} | {f[2]} min | {f[3]}")


def verSessoesComNomedoFilme():
    print("LISTA DE SESSÕES")
    sessoes = consultarBanco('''
        SELECT s.cod_sessao, f.titulo_filme, s.data_sessao, s.horario_sessao, s.sala_sessao
        FROM sessoes s
        JOIN filmes f ON f.cod_filme = s.cod_filme
        ORDER BY s.data_sessao, s.horario_sessao;
    ''')

    if (sessoes is None):
        return

    print("Código | Filme | Data | Horário | Sala")
    for s in sessoes:
        print(f"{s[0]} | {s[1]} | {s[2]:%d/%m/%Y} | {s[3]:%H:%M} | {s[4]}")


def cadastrarFilme():
    print("CADASTRO DE FILME")
    titulo = input("Título: ")
    duracao = int(input("Duração (minutos): "))
    classificacao = input("Classificação (L, 10, 12, 14, 16 ou 18): ")

    ok = manipularBanco('''
        INSERT INTO filmes
        VALUES (default, %s, %s, %s);
    ''', (titulo, duracao, classificacao))

    if (ok):
        print("FILME CADASTRADO!")


def cadastrarSessao():
    print("CADASTRO DE SESSÃO")
    verFilmes()
    cod_filme = int(input("Código do filme: "))
    data = input("Data (AAAA-MM-DD): ")
    horario = input("Horário (HH:MM): ")
    sala = int(input("Sala (1 a 5): "))

    ok = manipularBanco('''
        INSERT INTO sessoes
        VALUES (default, %s, %s, %s, %s);
    ''', (cod_filme, data, horario, sala))

    if (ok):
        print("SESSÃO CADASTRADA!")


def buscarFilmePorID():
    verFilmes()

    cod_escolhido = int(input("Digite o código do filme desejado: "))

    consulta = consultarBanco('''
        SELECT * FROM filmes
        WHERE cod_filme = %s;
    ''', (cod_escolhido,))

    if (not consulta):
        print("Filme não encontrado!")
        return

    filme_escolhido = consulta[0]

    print(f"""
    Código: {filme_escolhido[0]}
    Título: {filme_escolhido[1]}
    Duração: {filme_escolhido[2]} minutos
    Classificação: {filme_escolhido[3]}
    """)


while True:
    print("""
    CINEMA ESTRELA

    1 - Ver Filmes
    2 - Ver Sessões
    3 - Cadastrar Novo Filme
    4 - Cadastrar Nova Sessão
    5 - Ver Detalhes de um Filme

    0 - Sair
    """)

    op = input("Digite a opção desejada: ")

    if (op == "1"):
        verFilmes()
    elif (op == "2"):
        verSessoesComNomedoFilme()
    elif (op == "3"):
        cadastrarFilme()
    elif (op == "4"):
        cadastrarSessao()
    elif (op == "5"):
        buscarFilmePorID()
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Escolha uma opção válida...")

    input("TECLE ENTER PARA CONTINUAR")
