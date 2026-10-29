# Capítulo 5 · testar_conexao.py
# Confere se o .env foi lido e se o Python consegue conversar com o banco na Aiven.
# Antes de rodar: pip install "psycopg[binary]" python-dotenv

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()   # procura o arquivo .env e carrega os valores no ambiente

if os.getenv("DB_HOST") is None:
    print("Não encontrei o .env. Confira o nome do arquivo e a pasta.")
else:
    print("Conectando em", os.getenv("DB_HOST"))

    conexao = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode=os.getenv("DB_SSLMODE"),
    )
    cursor = conexao.cursor()

    cursor.execute("SELECT current_database(), CURRENT_DATE")
    linha = cursor.fetchone()
    print("Conectado! Resposta do banco:", linha)

    conexao.close()
