# Capítulo 5 · Gabarito da Prática 1 · setup_cinema.py
# Prepara o banco cinema do zero: apaga, cria e preenche as tabelas filmes e sessoes.
# Antes de rodar: o banco cinema existe na Aiven e o .env está na mesma pasta deste arquivo.

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

conexao = None

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
    cursor.execute("DROP TABLE IF EXISTS sessoes")
    cursor.execute("DROP TABLE IF EXISTS filmes")

    # 2) Criar: pais antes dos filhos
    cursor.execute("""
        CREATE TABLE filmes (
          cod_filme           integer      GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
          titulo_filme        varchar(100) NOT NULL,
          duracao_filme       integer      NOT NULL,
          classificacao_filme varchar(2)   NOT NULL,
          CONSTRAINT ck_duracao      CHECK (duracao_filme > 0),
          CONSTRAINT ck_classificacao CHECK (classificacao_filme IN ('L', '10', '12', '14', '16', '18'))
        )
    """)
    cursor.execute("""
        CREATE TABLE sessoes (
          cod_sessao     integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
          cod_filme      integer NOT NULL,
          data_sessao    date    NOT NULL,
          horario_sessao time    NOT NULL,
          sala_sessao    integer NOT NULL,
          CONSTRAINT ck_sala CHECK (sala_sessao BETWEEN 1 AND 5),
          CONSTRAINT fk_sessao_filme FOREIGN KEY (cod_filme) REFERENCES filmes (cod_filme)
        )
    """)
    print("Tabelas criadas.")

    # 3) Dados: pais antes dos filhos
    cursor.execute("""
        INSERT INTO filmes (titulo_filme, duracao_filme, classificacao_filme)
        VALUES ('O Último Farol',    112, '12'),
               ('Corrida nas Dunas',  98, 'L'),
               ('Código Vermelho',   125, '16'),
               ('A Ilha dos Gatos',   90, 'L'),
               ('Noite sem Fim',     105, '14')
    """)
    cursor.execute("""
        INSERT INTO sessoes (cod_filme, data_sessao, horario_sessao, sala_sessao)
        VALUES (1, '2026-11-06', '19:00', 1),
               (1, '2026-11-06', '21:30', 1),
               (2, '2026-11-07', '15:00', 2),
               (3, '2026-11-07', '20:00', 3),
               (4, '2026-11-08', '14:00', 2),
               (2, '2026-11-08', '16:30', 4)
    """)
    print("Dados inseridos.")

    conexao.commit()
    print("Banco cinema pronto!")

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


# PRÁTICA 1 · OS DOIS ERROS PROVOCADOS
#
# 1) Uma letra trocada no DB_PASSWORD do .env:
#    Não foi possível conectar ao banco.
#    connection failed: connection to server at "...", port ... failed:
#    FATAL:  password authentication failed for user "avnadmin"
#    Pegou o except psycopg.OperationalError. Não aparece "Conexão fechada.":
#    o connect falhou, conexao continuou None e o finally não tinha o que fechar.
#
# 2) CREAT no lugar de CREATE na tabela sessoes:
#    Erro no SQL. Nada foi gravado.
#    syntax error at or near "CREAT"
#    LINE 2:         CREAT TABLE sessoes (
#    Conexão fechada.
#    Pegou o except psycopg.Error, que chamou o rollback().
#
# PENSE E RESPONDA: por que os filmes continuam no banco?
# Os DROP, o CREATE de filmes e o CREAT estavam na mesma transação. O rollback desfez tudo,
# até os DROP: as tabelas da rodada anterior voltam, com os 5 filmes e as 6 sessões.
# No PostgreSQL, DROP e CREATE também entram na transação.
