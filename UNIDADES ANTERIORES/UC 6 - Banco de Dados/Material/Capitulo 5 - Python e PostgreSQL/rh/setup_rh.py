# Capítulo 5 · Etapa 1 · setup_rh.py
# Prepara o banco rh do zero: apaga as tabelas, cria de novo e insere os dados.
# Antes de rodar: o banco rh existe na Aiven e o .env está na mesma pasta deste arquivo.

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

conexaoDB = None
cursor = None

try:
    # 1. Criação e configuração da conexão e do cursor
    conexaoDB = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode=os.getenv("DB_SSL")
    )
    cursor = conexaoDB.cursor()

    # 2. SQL que será executado: apagar (filhos antes dos pais)...
    cursor.execute("DROP TABLE IF EXISTS funcionarios;")
    cursor.execute("DROP TABLE IF EXISTS setores;")
    print("REMOÇÃO DE TABELAS ANTIGAS CONCLUÍDA")

    # ... criar (pais antes dos filhos) ...
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

    # ... e inserir os dados (pais antes dos filhos)
    cursor.execute('''
        INSERT INTO setores (nome_setor)
        VALUES ('Administrativo'), ('Comercial'), ('Tecnologia');
    ''')
    cursor.execute('''
        INSERT INTO funcionarios
            (nome_funcionario, cpf_funcionario, cargo_funcionario, salario_funcionario, cod_setor)
        VALUES ('Ana Souza', '12345678901', 'Analista de RH', 4200.00, 1),
               ('Bruno Lima', '23456789012', 'Vendedor', 3100.00, 2),
               ('Carla Mendes', '34567890123', 'Desenvolvedora', 6800.00, 3),
               ('Diego Rocha', '45678901234', 'Suporte técnico', 3500.00, 3),
               ('Elisa Martins', '56789012345', 'Gerente comercial', 7500.00, 2);
    ''')
    print("DADOS INSERIDOS.")

    # Grava tudo de uma vez
    conexaoDB.commit()

except Exception as erro:
    print("ACONTECEU UM ERRO:", erro)

    # Desfaz o que estava pendente
    if (conexaoDB is not None):
        conexaoDB.rollback()

finally:
    # 3. Finalização do processo: fechar o cursor e a conexão
    if (cursor is not None):
        cursor.close()

    if (conexaoDB is not None):
        conexaoDB.close()
