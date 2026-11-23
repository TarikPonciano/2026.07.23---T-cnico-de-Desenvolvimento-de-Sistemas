# Capítulo 5 · Etapa 3 · classBanco.py
# A conexão num lugar só: abre, roda o SQL e fecha.
# O except é genérico (Exception): mostra a mensagem do erro, para ajudar no debug,
# e repassa o erro com raise. Quem chamou decide a mensagem para o usuário.

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


class Banco():
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.dbname = os.getenv("DB_NAME")
        self.ssl = os.getenv("DB_SSL")

    # Esse método deveria ser privado, ou seja, executado somente dentro da classe
    def conectar(self):
        return psycopg.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.dbname,
            sslmode=self.ssl
        )

    # SELECT: devolve a lista de linhas (cada linha é uma tupla)
    def consultar(self, sql, parametros=()):
        conexao = None

        try:
            conexao = self.conectar()
            cursor = conexao.cursor()

            cursor.execute(sql, parametros)

            return cursor.fetchall()

        except Exception as error:
            print("ERRO DE CONSULTA:", error)
            raise

        finally:
            if (conexao is not None):
                conexao.close()

    # INSERT, UPDATE ou DELETE: grava e devolve quantas linhas mudaram
    def manipular(self, sql, parametros=()):
        conexao = None

        try:
            conexao = self.conectar()
            cursor = conexao.cursor()

            resultado = cursor.execute(sql, parametros)

            conexao.commit()

            return resultado.rowcount

        except Exception as error:
            print("ERRO DE MANIPULAÇÃO:", error)
            raise

        finally:
            if (conexao is not None):
                conexao.close()
