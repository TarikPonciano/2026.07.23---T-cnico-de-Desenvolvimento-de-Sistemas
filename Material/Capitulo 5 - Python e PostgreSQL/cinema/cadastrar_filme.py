# Capítulo 5 · Prática 4 · cadastrar_filme.py
# O programa da prática "Qual mensagem aparece?". Rode depois de prever cada saída.
# Rode o setup_cinema.py antes, para começar com os 5 filmes.

import psycopg
from classBanco import Banco

banco = Banco()


def cadastrar_filme(titulo, duracao, classificacao):
    try:
        banco.executar(
            """INSERT INTO filmes (titulo_filme, duracao_filme, classificacao_filme)
               VALUES (%s, %s, %s)""",
            (titulo, duracao, classificacao),
        )
        print("Filme cadastrado:", titulo)
    except psycopg.errors.CheckViolation as erro:
        if erro.diag.constraint_name == "ck_duracao":
            print("Duração inválida.")
        else:
            print("Classificação inválida.")
    except psycopg.errors.NotNullViolation:
        print("Faltou um dado obrigatório.")
    except psycopg.Error:
        print("Erro no banco.")
    finally:
        print("---")


cadastrar_filme("Maré Alta", 101, "12")      # a
cadastrar_filme("Maré Alta", 0, "12")        # b
cadastrar_filme("Maré Alta", 101, "13")      # c
cadastrar_filme(None, 101, "L")              # d
cadastrar_filme("Maré Alta", 101, "Livre")   # e
cadastrar_filme("Maré Alta", 101, "12")      # f
