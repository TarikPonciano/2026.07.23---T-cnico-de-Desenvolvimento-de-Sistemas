# 1. Criar um aplicativo python para visualizar os dados do cinema

# 2. As opções do menu devem ser:
    # 1 - Ver Filmes
    # 2 - Ver Sessões
    # 3 - Cadastrar novo filme
    # 4 - Cadastrar nova sessão
    
# 3. Funcionalidades extras:
    # - Ver detalhes de um filme (a pessoa escolhe um filme da lista e vê somente informações daquele filme)
    # - Ao ver uma sessão, exibir o nome do filme da sessão
    
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
        if(cursor is not None):
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
        print("ERRO AO CONSULTAR BANCO")
        print(error)
        if (conexaoDB is not None):
            conexaoDB.rollback()
            
        return False
            
    finally:
        if(cursor is not None):
            cursor.close()
        if (conexaoDB is not None):
            conexaoDB.close()

def buscarFilmePorID():
    filmes = consultarBanco("SELECT * FROM filmes;")

    for f in filmes:
        print(f"{f[0]} - {f[1]}")
        
    cod_escolhido = int(input("Digite o código do filme desejado: "))

    filme_escolhido = consultarBanco('''
            SELECT * FROM filmes
            WHERE cod_filme = %s
                                    ''', (cod_escolhido,))[0]

    # filme_escolhido = None

    # for filme in filmes:
    #     if cod_escolhido == filme[0]:
    #         filme_escolhido = filme
    #         break
            
            
    print(f"""
        Código: {filme_escolhido[0]}
        Título: {filme_escolhido[1]}
        Duração: {filme_escolhido[2]} minutos
        Classificação: {filme_escolhido[3]}
        """)

def verSessoesComNomedoFilme():
    sessoes = consultarBanco('''
            SELECT s.cod_sessao, f.titulo_filme, s.data_sessao, s.horario_sessao FROM sessoes s
            JOIN filmes f ON f.cod_filme = s.cod_filme''')

    for sessao in sessoes:
        print(f"{sessao[0]} - {sessao[1]} - {sessao[2]} - {sessao[3]}")