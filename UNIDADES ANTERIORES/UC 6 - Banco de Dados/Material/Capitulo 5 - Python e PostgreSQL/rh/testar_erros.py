# Capítulo 5 · Para saber · testar_erros.py
# Os tipos de erro do psycopg na prática: um except para cada regra do banco.
# Rode depois do setup_rh.py. Troque os valores do INSERT para ver cada except em ação:
#   CPF da Ana ('12345678901') · salário 0 · setor 9 · CPF '123' · coluna "salario" (escrita errada)

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
        sslmode=os.getenv("DB_SSL"),
    )
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO funcionarios
          (nome_funcionario, cpf_funcionario, cargo_funcionario, salario_funcionario, cod_setor)
        VALUES ('Gil Paz', '12345678901', 'Vendedor', 3000.00, 2)
    """)
    conexao.commit()
    print("Funcionário cadastrado!")

# Do mais específico para o mais geral: o Python usa o primeiro except que servir
except psycopg.errors.UniqueViolation:
    print("CPF já cadastrado.")

except psycopg.errors.ForeignKeyViolation:
    print("Esse setor não existe.")

except psycopg.errors.CheckViolation as erro:
    # Dois CHECKs, um tipo de erro só: o nome da regra diz qual recusou
    if erro.diag.constraint_name == "ck_cpf_tamanho":
        print("O CPF precisa ter 11 dígitos.")
    else:
        print("O salário precisa ser maior que zero.")

except psycopg.OperationalError:
    print("Não foi possível conectar ao banco.")

except psycopg.Error as erro:
    # O que sobrou: SQL escrito errado, tabela ou coluna que não existe...
    print("Outro erro do banco:", erro)

finally:
    if conexao is not None:
        conexao.close()
