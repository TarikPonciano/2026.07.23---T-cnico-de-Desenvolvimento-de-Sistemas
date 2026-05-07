# nomes = ["João", "Miguel", "Zeca", "Jorge"]

# print(nomes[0])

# nomes.append("Emilly")

# nomes[1] = "Miguelito"

# print(nomes.pop(2))

# print(nomes)

# Crie um programa que recebe o nome de 5 alunos e exiba-os em ordem alfabética.

# Declarar a lista vazia
nomes = []
# medias = []

# Lógica de receber informação e guardar na lista
for i in range(5):
    nome = input("Digite o nome do aluno: ")

    # media = float(input("Digite a média do aluno: "))

    nomes.append(nome)
    # medias.append(media)

nomes.sort() #Organiza os elementos em ordem crescente
#nomes.reverse() #Organiza os elementos em ordem decrescentes

# Percorrer a lista para fazer algo
for n in nomes:
    print(f"1. {n}")

for i in range(len(nomes)):
    print(f"{i}. {nomes[i]}")