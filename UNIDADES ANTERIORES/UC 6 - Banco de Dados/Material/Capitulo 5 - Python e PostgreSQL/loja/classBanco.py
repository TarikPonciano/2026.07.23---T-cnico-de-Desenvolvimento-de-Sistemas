# Capítulo 5 · Prática guiada · classBanco.py
# A mesma classe do Sistema RH, com um método a mais: registrarVenda, que grava o pedido
# e os itens numa transação só (tudo ou nada).

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

    # Venda: o pedido e os itens numa transação só. Devolve o código do pedido.
    # itens é uma lista de tuplas (cod_produto, qtd, preco_unit)
    def registrarVenda(self, cod_cliente, itens):
        conexao = None

        try:
            conexao = self.conectar()
            cursor = conexao.cursor()

            # 1. O pedido. O RETURNING devolve o código que o banco gerou
            cursor.execute('''
                INSERT INTO pedidos
                VALUES (default, %s, default, default)
                RETURNING cod_pedido;
            ''', (cod_cliente,))

            cod_pedido = cursor.fetchone()[0]

            # 2. Os itens, todos com o código do pedido que acabou de nascer
            for cod_produto, qtd, preco_unit in itens:
                cursor.execute('''
                    INSERT INTO itens_pedido
                    VALUES (default, %s, %s, %s, %s);
                ''', (cod_pedido, cod_produto, qtd, preco_unit))

            # 3. Tudo certo: o pedido e os itens são gravados juntos
            conexao.commit()

            return cod_pedido

        except Exception as error:
            print("ERRO NA VENDA:", error)

            # Algum passo falhou: nem o pedido nem os itens ficam gravados
            if (conexao is not None):
                conexao.rollback()
            raise

        finally:
            if (conexao is not None):
                conexao.close()
