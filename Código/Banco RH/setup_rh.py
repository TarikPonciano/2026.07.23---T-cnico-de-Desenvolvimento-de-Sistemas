import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

conexaoDB = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    sslmode=os.getenv("DB_SSL")
)  

cursor = conexaoDB.cursor()

cursor.execute("SELECT VERSION()")

resultado = cursor.fetchall()

print(resultado)

cursor.close()

conexaoDB.close()