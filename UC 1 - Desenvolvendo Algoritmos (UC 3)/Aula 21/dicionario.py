pokemon = {
    "Nome": "Pikachu",
    "Tipo": "Elétrico",
    "Ataque": 50
    }
print(pokemon["Tipo"])

# Crie um programa que contém uma variável pessoa e declare um dicionário com as informações Nome, Idade, Altura e CPF. Imprima a Ficha Pessoal dessa pessoa.

pessoa = {
    "Nome": "Zeca",
    "Idade": 23,
    "Altura": 1.86,
    "CPF": "05152345678"
}

print(f"""
----- Ficha Pessoal -----
      
Nome: {pessoa['Nome']}
Idade: {pessoa['Idade']} anos
Altura: {pessoa['Altura']}m
CPF: {pessoa['CPF']}

""")