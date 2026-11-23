# Capítulo 5 · Gabarito da Prática 1 · setup_cinema.py
# Prepara o banco cinema do zero: apaga, cria e preenche as tabelas filmes e sessoes.
# Usa o mesmo .env do RH: só o banco muda (dbname="cinema").

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
        dbname="cinema",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode=os.getenv("DB_SSL")
    )
    cursor = conexaoDB.cursor()

    # 2. Apagar: filhos antes dos pais
    cursor.execute("DROP TABLE IF EXISTS sessoes;")
    cursor.execute("DROP TABLE IF EXISTS filmes;")
    print("REMOÇÃO DE TABELAS ANTIGAS CONCLUÍDA")

    # Criar: pais antes dos filhos
    cursor.execute('''
        CREATE TABLE filmes (
            cod_filme INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            titulo_filme VARCHAR(100) NOT NULL,
            duracao_filme INTEGER NOT NULL,
            classificacao_filme VARCHAR(2) NOT NULL,
            CONSTRAINT ck_duracao CHECK (duracao_filme > 0),
            CONSTRAINT ck_classificacao CHECK (classificacao_filme IN ('L', '10', '12', '14', '16', '18'))
        );
    ''')
    cursor.execute('''
        CREATE TABLE sessoes (
            cod_sessao INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            cod_filme INTEGER NOT NULL,
            data_sessao DATE NOT NULL,
            horario_sessao TIME NOT NULL,
            sala_sessao INTEGER NOT NULL,
            CONSTRAINT ck_sala CHECK (sala_sessao BETWEEN 1 AND 5),
            CONSTRAINT fk_sessao_filme FOREIGN KEY (cod_filme) REFERENCES filmes (cod_filme)
        );
    ''')
    print("TABELAS CRIADAS COM SUCESSO!")

    # Dados: pais antes dos filhos
    cursor.execute('''
        INSERT INTO filmes (titulo_filme, duracao_filme, classificacao_filme)
        VALUES ('O Último Farol', 112, '12'),
               ('Corrida nas Dunas', 98, 'L'),
               ('Código Vermelho', 125, '16'),
               ('A Ilha dos Gatos', 90, 'L'),
               ('Noite sem Fim', 105, '14');
    ''')
    cursor.execute('''
        INSERT INTO sessoes (cod_filme, data_sessao, horario_sessao, sala_sessao)
        VALUES (1, '2026-11-06', '19:00', 1),
               (1, '2026-11-06', '21:30', 1),
               (2, '2026-11-07', '15:00', 2),
               (3, '2026-11-07', '20:00', 3),
               (4, '2026-11-08', '14:00', 2),
               (2, '2026-11-08', '16:30', 4);
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


# PRÁTICA 1 · OS DOIS ERROS PROVOCADOS
#
# 1) Uma letra trocada no DB_PASSWORD do .env:
#    ACONTECEU UM ERRO: connection failed: connection to server at "...", port ... failed:
#    FATAL:  password authentication failed for user "avnadmin"
#    O connect falhou: conexaoDB continuou None, então não houve rollback nem nada a fechar.
#
# 2) CREAT no lugar de CREATE na tabela sessoes:
#    REMOÇÃO DE TABELAS ANTIGAS CONCLUÍDA
#    ACONTECEU UM ERRO: syntax error at or near "CREAT"
#    O except chamou o rollback(): os DROP, o CREATE de filmes e o CREAT estavam na mesma
#    transação, e tudo foi desfeito. As tabelas da rodada anterior voltam, com os 5 filmes
#    e as 6 sessões. No PostgreSQL, DROP e CREATE também entram na transação.
