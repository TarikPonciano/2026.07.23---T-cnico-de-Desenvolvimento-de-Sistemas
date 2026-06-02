#CRUD 
#Create - Inserir
#Read - Ler/Acessar
#Update - Alterar
#Delete - Remover

print("------- LISTA DE FRUTAS -------")
frutas = ["Maçã", "Pêra", "Uva", "Abacate", "Abacaxi"] # Ordenada, Mutável

print(len(frutas))

print(frutas[-1])

print(frutas[3])

print(frutas)

print("------- LISTA DE ANIMAIS -------")
# Tente criar e imprimir uma lista com 5 animais
animal1 = "Macaco"
animais = ["Papagaio", "Lobo", "Kiwi", animal1, "Javali"]

# Insira um novo animal na lista

# animais.append("Dragão")
# animais.append("Mula")

# animais.insert(0, "Gato")

#animais += ["Enguia", "Peixe", "Cachorro"]

# Remova um animal da lista

# animais.pop()
# animais.remove("Cavalo")

# Substituir valor
animais[2] = "Galinha"

print(animais)


print("------- LISTA DE PESSOA -------")
# Nome, Idade, Altura, Conta Paga
pessoa = ["Michael", 35, 1.75, True]

print(f"""
Dados Pessoais:

Nome: {pessoa[0]}
Idade: {pessoa[1]} anos
Altura: {pessoa[2]} metros
Conta Paga: {pessoa[3]}
""")

print("------- LISTA DE NUMEROS -------")

numeros = [10, 50, 30, 25, 13, 34]

soma = sum(numeros)
maior_numero = max(numeros)
menor_numero = min(numeros)
media = sum(numeros)/len(numeros)

# Método manual
# for num in numeros:
#     soma += num

#     if num > maior_numero:
#         maior_numero = num

# for i in range(len(numeros)):

#     soma += numeros[i]

#     if numeros[i] > maior_numero:
#         maior_numero = numeros[i]

print(soma)
print(maior_numero)