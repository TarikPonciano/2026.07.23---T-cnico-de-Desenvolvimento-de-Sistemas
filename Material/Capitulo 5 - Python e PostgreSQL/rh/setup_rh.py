# Capítulo 5 · setup_rh.py
# Prepara o banco rh do zero: apaga as tabelas, cria de novo e insere os dados.
# Antes de rodar: o banco rh existe na Aiven e o .env está na mesma pasta deste arquivo.
# Pode rodar quantas vezes quiser: começa sempre do zero.

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

conexao = None   # ainda não há conexão: o finally precisa saber disso

try:
    conexao = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode=os.getenv("DB_SSLMODE"),
    )
    cursor = conexao.cursor()

    # 1) Apagar: filhos antes dos pais
    cursor.execute("DROP TABLE IF EXISTS funcionarios")
    cursor.execute("DROP TABLE IF EXISTS setores")

    # 2) Criar: pais antes dos filhos
    cursor.execute("""
        CREATE TABLE setores (
          cod_setor  integer     GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
          nome_setor varchar(60) NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE funcionarios (
          cod_funcionario     integer       GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
          nome_funcionario    varchar(100)  NOT NULL,
          cpf_funcionario     char(11)      NOT NULL UNIQUE,
          cargo_funcionario   varchar(60)   NOT NULL,
          salario_funcionario numeric(10,2) NOT NULL,
          cod_setor           integer       NOT NULL,
          CONSTRAINT ck_cpf_tamanho      CHECK (LENGTH(cpf_funcionario) = 11),
          CONSTRAINT ck_salario_positivo CHECK (salario_funcionario > 0),
          CONSTRAINT fk_func_setor FOREIGN KEY (cod_setor) REFERENCES setores (cod_setor)
        )
    """)
    print("Tabelas criadas.")

    # 3) Dados: pais antes dos filhos
    cursor.execute("""
        INSERT INTO setores (nome_setor)
        VALUES ('Administrativo'), ('Comercial'), ('Tecnologia')
    """)
    cursor.execute("""
        INSERT INTO funcionarios
          (nome_funcionario, cpf_funcionario, cargo_funcionario, salario_funcionario, cod_setor)
        VALUES ('Ana Souza',     '12345678901', 'Analista de RH',    4200.00, 1),
               ('Bruno Lima',    '23456789012', 'Vendedor',          3100.00, 2),
               ('Carla Mendes',  '34567890123', 'Desenvolvedora',    6800.00, 3),
               ('Diego Rocha',   '45678901234', 'Suporte técnico',   3500.00, 3),
               ('Elisa Martins', '56789012345', 'Gerente comercial', 7500.00, 2)
    """)
    print("Dados inseridos.")

    # 4) Gravar tudo de uma vez
    conexao.commit()
    print("Banco rh pronto!")

except psycopg.OperationalError as erro:
    print("Não foi possível conectar ao banco.")
    print(erro)

except psycopg.Error as erro:
    print("Erro no SQL. Nada foi gravado.")
    print(erro)
    conexao.rollback()

finally:
    if conexao is not None:
        conexao.close()
        print("Conexão fechada.")
