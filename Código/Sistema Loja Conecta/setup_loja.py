# Capítulo 5 · Prática guiada · setup_loja.py
# O banco da Loja Conecta do Capítulo 4, agora montado pelo Python.
# Uma mudança: os códigos passam a ser gerados pelo banco (GENERATED ALWAYS AS IDENTITY),
# porque o sistema vai cadastrar produtos e vendas novos. O START WITH faz o contador começar
# no mesmo número do Capítulo 4: os dados ficam iguais (produtos 10 a 16, pedidos 100 a 107).
# Antes de rodar: o banco loja existe na Aiven e o .env desta pasta tem DB_NAME=loja.

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

    # 2. Apagar: filhos antes dos pais
    cursor.execute("DROP TABLE IF EXISTS itens_pedido;")
    cursor.execute("DROP TABLE IF EXISTS pedidos;")
    cursor.execute("DROP TABLE IF EXISTS clientes;")
    cursor.execute("DROP TABLE IF EXISTS produtos;")
    cursor.execute("DROP TABLE IF EXISTS categorias;")
    print("REMOÇÃO DE TABELAS ANTIGAS CONCLUÍDA")

    # Criar: pais antes dos filhos
    cursor.execute('''
        CREATE TABLE categorias (
            cod_categoria INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_categoria VARCHAR(40) NOT NULL UNIQUE
        );
    ''')
    cursor.execute('''
        CREATE TABLE produtos (
            cod_produto INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 10) PRIMARY KEY,
            nome_produto VARCHAR(80) NOT NULL,
            preco NUMERIC(8,2) NOT NULL CONSTRAINT ck_preco CHECK (preco >= 0),
            estoque INTEGER NOT NULL DEFAULT 0 CONSTRAINT ck_estoque CHECK (estoque >= 0),
            cod_categoria INTEGER CONSTRAINT fk_prod_categoria REFERENCES categorias (cod_categoria)
        );
    ''')
    cursor.execute('''
        CREATE TABLE clientes (
            cod_cliente INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_cliente VARCHAR(100) NOT NULL,
            email_cliente VARCHAR(100) NOT NULL UNIQUE,
            cidade_cliente VARCHAR(60) NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE pedidos (
            cod_pedido INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 100) PRIMARY KEY,
            cod_cliente INTEGER NOT NULL CONSTRAINT fk_ped_cliente REFERENCES clientes (cod_cliente),
            data_pedido DATE NOT NULL DEFAULT CURRENT_DATE,
            status VARCHAR(10) NOT NULL DEFAULT 'aberto'
                CONSTRAINT ck_status CHECK (status IN ('aberto', 'enviado', 'entregue', 'cancelado'))
        );
    ''')
    cursor.execute('''
        CREATE TABLE itens_pedido (
            cod_item INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            cod_pedido INTEGER NOT NULL CONSTRAINT fk_item_pedido REFERENCES pedidos (cod_pedido) ON DELETE CASCADE,
            cod_produto INTEGER NOT NULL CONSTRAINT fk_item_produto REFERENCES produtos (cod_produto),
            qtd INTEGER NOT NULL CONSTRAINT ck_qtd CHECK (qtd > 0),
            preco_unit NUMERIC(8,2) NOT NULL CONSTRAINT ck_preco_unit CHECK (preco_unit >= 0),
            CONSTRAINT uq_item_pedido_produto UNIQUE (cod_pedido, cod_produto)
        );
    ''')
    print("TABELAS CRIADAS COM SUCESSO!")

    # Dados: pais antes dos filhos. Sem os códigos: o banco gera, na ordem das linhas.
    cursor.execute('''
        INSERT INTO categorias (nome_categoria)
        VALUES ('Informática'), ('Celulares'), ('Acessórios'), ('Games');
    ''')
    cursor.execute('''
        INSERT INTO produtos (nome_produto, preco, estoque, cod_categoria)
        VALUES ('Notebook Lume 14', 3499.00, 5, 1),
               ('Monitor 24 pol', 899.90, 8, 1),
               ('Smartphone Nova X', 1899.00, 10, 2),
               ('Fone Bluetooth', 199.90, 25, 3),
               ('Capa para celular', 49.90, 40, 3),
               ('Mouse sem fio', 89.90, 30, 3),
               ('Cabo HDMI', 39.90, 50, NULL);
    ''')
    cursor.execute('''
        INSERT INTO clientes (nome_cliente, email_cliente, cidade_cliente)
        VALUES ('Mariana Costa', 'mariana@email.com', 'Recife'),
               ('Rafael Torres', 'rafael@email.com', 'Olinda'),
               ('Paula Nogueira', 'paula@email.com', 'Recife'),
               ('Tiago Freire', 'tiago@email.com', 'Jaboatão'),
               ('Lívia Campos', 'livia@email.com', 'Recife'),
               ('Gustavo Ramos', 'gustavo@email.com', 'Paulista');
    ''')
    cursor.execute('''
        INSERT INTO pedidos (cod_cliente, data_pedido, status)
        VALUES (1, '2026-09-02', 'entregue'),
               (2, '2026-09-05', 'entregue'),
               (1, '2026-09-10', 'entregue'),
               (3, '2026-09-18', 'enviado'),
               (4, '2026-09-25', 'cancelado'),
               (5, '2026-10-01', 'entregue'),
               (3, '2026-10-03', 'aberto'),
               (1, '2026-10-05', 'aberto');
    ''')
    cursor.execute('''
        INSERT INTO itens_pedido (cod_pedido, cod_produto, qtd, preco_unit)
        VALUES (100, 10, 1, 3499.00),
               (100, 13, 2, 199.90),
               (101, 12, 1, 1899.00),
               (101, 14, 1, 49.90),
               (102, 13, 1, 179.90),
               (103, 11, 2, 899.90),
               (103, 16, 1, 39.90),
               (104, 12, 1, 1899.00),
               (105, 10, 1, 3299.00),
               (105, 14, 3, 49.90),
               (106, 13, 1, 199.90);
    ''')
    print("DADOS INSERIDOS.")

    conexaoDB.commit()

except Exception as erro:
    print("ACONTECEU UM ERRO:", erro)

    if (conexaoDB is not None):
        conexaoDB.rollback()

finally:
    # 3. Finalização do processo: fechar o cursor e a conexão
    if (cursor is not None):
        cursor.close()

    if (conexaoDB is not None):
        conexaoDB.close()
