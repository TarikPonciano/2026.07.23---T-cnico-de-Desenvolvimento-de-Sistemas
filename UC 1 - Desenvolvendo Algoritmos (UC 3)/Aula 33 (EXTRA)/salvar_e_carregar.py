# Leitura de txt

# dados = None

# with open("dados.txt","r") as arquivo:
#     dados = arquivo.read()

# print(dados)
import json

def carregar_dados():
    dados = None

    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)
        return dados