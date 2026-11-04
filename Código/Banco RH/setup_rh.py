import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

# 1. Criação e configuração da conexão e cursor
conexaoDB = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    sslmode=os.getenv("DB_SSL")
)  
cursor = conexaoDB.cursor()


# 2. SQL que será executado
cursor.execute('''
               DROP TABLE IF EXISTS funcionarios;
               ''')
cursor.execute('''
               DROP TABLE IF EXISTS setores;
               ''')
print("REMOÇÃO DE TABELAS ANTIGAS CONCLUÍDA")

cursor.execute('''
               CREATE TABLE setores(
                   cod_setor INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                   nome_setor VARCHAR(255) NOT NULL UNIQUE
               );
               ''')

cursor.execute('''
               CREATE TABLE funcionarios(
                   cod_funcionario INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                   nome_funcionario VARCHAR(255) NOT NULL,
                   cpf_funcionario CHAR(11) NOT NULL UNIQUE,
                   cargo_funcionario VARCHAR(255) NOT NULL,
                   salario_funcionario NUMERIC(10,2) NOT NULL,
                   cod_setor INTEGER NOT NULL,
                   CONSTRAINT ck_cpf_tamanho CHECK (LENGTH(cpf_funcionario) = 11),
                   CONSTRAINT ck_salario_positivo CHECK (salario_funcionario > 0),
                   CONSTRAINT fk_func_setor FOREIGN KEY (cod_setor) REFERENCES setores (cod_setor)
               );
               ''')
print("TABELAS CRIADAS COM SUCESSO!")

conexaoDB.commit()
# 3. Finalização do processo. Fechar cursor e conexaoDB
cursor.close()

conexaoDB.close()