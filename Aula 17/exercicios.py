# Crie um programa que pede o nome de 10 pessoas. Adicione cada nome em uma lista e ao final imprima a lista verticalmente. Ex:
#Maria
#João
#Zeca
#Manel

nomes = []

for i in range(10):
    nome = input("Digite o seu nome: ")
    nomes.append(nome)

print(nomes)

numero = 1

for n in nomes:
    print(f"{numero}. {n}")
    numero+=1

