import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

class Banco ():
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.dbname = os.getenv("DB_NAME")
        self.ssl = os.getenv("DB_SSL")
        
    #Esse método deveria ser privado, ou seja, deve ser executado somente dentro da classe
    def conectar(self):
        return psycopg.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            dbname = self.dbname,
            sslmode = self.ssl
        )
    
    def consultar (self, sql, parametros=()):
        conexao = None
        
        try:
            
            conexao = self.conectar()
            cursor = conexao.cursor()
            
            cursor.execute(sql,parametros)
            
            return cursor.fetchall()
        except Exception as error:
            
            print("ERRO DE CONSULTA:", error)
            raise
        
        finally:
            if (conexao is not None):
                conexao.close()

    def manipular (self, sql, parametros = ()):
        conexao = None
        
        try:
            
            conexao = self.conectar()
            cursor = conexao.cursor()
            
            resultado = cursor.execute(sql,parametros)
            
            conexao.commit()
            
            return resultado.rowcount
        
        except Exception as error:
            
            print("ERRO DE CONSULTA:", error)
            raise
        
        finally:
            if (conexao is not None):
                conexao.close()
    
    def registrarVenda(self, cod_cliente, itens):
        conexao = None
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
            
            cursor.execute('''
            INSERT INTO pedidos
            VALUES(default, %s, default, default)
            RETURNING cod_pedido;
                           ''', (cod_cliente,))  
            
            cod_pedido = cursor.fetchall()[0][0]
            
            for item in itens:
                
                cursor.execute('''
                INSERT INTO itens_pedido
                VALUES (default, %s, %s, %s, %s);               
                               ''', (cod_pedido, item[0], item[1], item[2]))
            
                
            conexao.commit()
            
            return cod_pedido
            
            
            
        except Exception as error:
            print("OCORREU UM ERRO AO REGISTRAR A VENDA")
            print(error)
            if (conexao is not None):
                conexao.rollback()
            raise
        finally:
            if (conexao is not None):
                conexao.close()
    