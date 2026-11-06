# 1. Criar um arquivo sistema_rh.py

# 2. Criar uma aplicação com menu no terminal que possua as opções:

#     1 - Ver Funcionarios
#     2 - Ver Departamentos
#     0 - Sair

# 3. Criar a infraestrutura de conexão com o banco

# 4. Expandir as funcionalidades com as opções de:

    # 3 - Cadastrar Novo Funcionário
    # 4 - Cadastrar Novo Departamento

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


while True:
    
    
    
    print("""
    SEJA BEM VINDO AO SISTEMA RH
    
    MENU:
    
    1 - Ver Funcionários
    2 - Ver Departamentos
    3 - Cadastrar Novo Funcionário
    4 - Cadastrar Novo Departamento
    
    0 - Sair      
    
          """)
    
    op = input("Digite a opção desejada: ")
    
    if (op == "1"):
        print("VER FUNCIONÁRIOS")
        
        funcionarios = None
        
        conexaoDB = None
        cursor = None
        
        try:
            conexaoDB = psycopg.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    dbname=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    sslmode=os.getenv("DB_SSL")
                )
            cursor = conexaoDB.cursor()
            
            cursor.execute("SELECT * FROM funcionarios;")
            
            funcionarios = cursor.fetchall()
            
            
        except Exception as error:
            print("OCORREU UM ERRO:",error)
            if (conexaoDB is not None):
                conexaoDB.rollback()
        finally:
            if (cursor is not None):
                cursor.close()
            
            if (conexaoDB is not None):
                conexaoDB.close()
                
        print("LISTA DE FUNCIONÁRIOS")
        print("ID | NOME | CPF | CARGO | SALÁRIO | COD DEPT")
        
        if (funcionarios):
            for func in funcionarios:
                print(f"{func[0]} | {func[1]} | {func[2]} | {func[3]} | R$ {func[4]:,.2f} | {func[5]} ")
        else:
            print("ERRO NA CONSULTA")

    elif (op == "2"):
        print("VER DEPARTAMENTOS")
        
        departamentos = None
        conexaoDB = None
        cursor = None
        
        try:
            conexaoDB = psycopg.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    dbname=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    sslmode=os.getenv("DB_SSL")
                )
            cursor = conexaoDB.cursor()
            
            cursor.execute("SELECT * FROM setores;")
            
            departamentos = cursor.fetchall()
            
            
        except Exception as error:
            print("OCORREU UM ERRO:",error)
            if (conexaoDB is not None):
                conexaoDB.rollback()
        finally:
            if (cursor is not None):
                cursor.close()
            
            if (conexaoDB is not None):
                conexaoDB.close()
                
        print("LISTA DE DEPARTAMENTOS")
        print("ID | NOME")
        
        if(departamentos):
            for dept in departamentos:
                print(f"{dept[0]} | {dept[1]}")
        else:
            print("Erro na consulta!")
    
    elif (op == "3"):
        print("CADASTRO DE FUNCIONÁRIO")
        
        nome = input("Digite o nome do Funcionário:")
        cpf = input("Digite o cpf do Funcionário:")
        cargo = input("Digite o cargo do Funcionário:")
        salario = float(input("Digite o salário do Funcionário:"))
        cod_setor = int(input("Digite o código do setor:"))
        
        conexaoDB = None
        curso = None
        
        try:
            conexaoDB = psycopg.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    dbname=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    sslmode=os.getenv("DB_SSL")
                            )
            cursor = conexaoDB.cursor()
            
            cursor.execute(f'''
            INSERT INTO funcionarios
            VALUES (default, %s, %s, %s, %s, %s);               
                           ''', (nome, cpf, cargo, salario, cod_setor))
            
            conexaoDB.commit()
            
        except Exception as error:
            print("Erro no cadastro do Funcionário")
            print(error)
            if (conexaoDB is not None):
                conexaoDB.rollback()            
        finally: 
            if (cursor is not None):
                cursor.close()
            
            if (conexaoDB is not None):
                conexaoDB.close
        
        
    elif (op == "4"):
        print("CADASTRAR NOVO DEPARTAMENTO")
        
        nome = input("DIGITE O NOME DO DEPARTAMENTO: ")
        
        if (not nome):
            nome = None
    
        try:
            conexaoDB = psycopg.connect(
                                host=os.getenv("DB_HOST"),
                                port=os.getenv("DB_PORT"),
                                dbname=os.getenv("DB_NAME"),
                                user=os.getenv("DB_USER"),
                                password=os.getenv("DB_PASSWORD"),
                                sslmode=os.getenv("DB_SSL")
                                        )
            cursor = conexaoDB.cursor()
            
            cursor.execute('''
                           INSERT INTO setores
                           VALUES (default, %s)
                           
                           ''', (nome,))
            
            conexaoDB.commit()
        except Exception as error:
            print("ERRO AO CRIAR DEPARTAMENTO")
            print(error)
            if (conexaoDB is not None):
                conexaoDB.rollback()
        finally:
            if (cursor is not None):
                cursor.close()
            if (conexaoDB is not None):
                conexaoDB.close()
        
        
        
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Escolha uma opção válida...")
    
    input("TECLE ENTER PARA CONTINUAR")
    
