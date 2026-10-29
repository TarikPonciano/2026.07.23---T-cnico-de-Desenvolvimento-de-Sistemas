# Capítulo 5 · classBanco.py
# Abre a conexão, roda um comando e fecha: para consultas pontuais.
# Os dados da conexão vêm do .env (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_SSLMODE).

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


class Banco():
    def __init__(self):
        self.servidor = os.getenv("DB_HOST")
        self.porta = os.getenv("DB_PORT")
        self.nome_banco = os.getenv("DB_NAME")
        self.usuario = os.getenv("DB_USER")
        self.senha = os.getenv("DB_PASSWORD")
        self.ssl = os.getenv("DB_SSLMODE")

    def conectar(self):
        return psycopg.connect(
            host=self.servidor,
            port=self.porta,
            dbname=self.nome_banco,
            user=self.usuario,
            password=self.senha,
            sslmode=self.ssl,
        )

    # SELECT: devolve a lista de linhas (cada linha é uma tupla)
    def consultar(self, sql, parametros=None):
        conexao = self.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, parametros)
            return cursor.fetchall()
        finally:
            conexao.close()

    # INSERT, UPDATE ou DELETE: grava e devolve quantas linhas mudaram
    def executar(self, sql, parametros=None):
        conexao = self.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, parametros)
            conexao.commit()
            return cursor.rowcount
        finally:
            conexao.close()
