# nome = "Banana"

# nome = nome.lower()

# print(nome[0])

# print(nome.count("a"))

# nome = nome.replace("an", "em")

# print(nome)

#CRUD 

#Create - Inserir
#Read - Ler/Acessar
#Update - Alterar
#Delete - Remover

# Crie um programa que recebe uma palavra. Imprima a última letra dessa palavra. 

# palavra = "Cachorro"

# # Usar o len() para descobrir o tamanho de uma coleção

# print(palavra[-1])


# Crie um programa que recebe uma palavra. Informe se a palavra começa com vogal ou consoante.

# palavra = "1223"

# if palavra[0].lower() in "aeiou":
#     print("Começa com vogal!")
# elif palavra[0] in "0123456789":
#     print("Começa com numero!")
# else:
#     print("Começa com consoante")


# Crie um programa que recebe uma palavra. Imprima todos os caracteres dessa palavra, linha por linha

# Maneira tradicional
# palavra = "Jujuba"
# qtd_vogais = 0

# for i in range(len(palavra)):
#     print(palavra[i])

#     if palavra[i] in "aeiou":
#         qtd_vogais += 1

# print(qtd_vogais)

# Conte quantas vogais tem na palavra do programa acima

# Maneira Python

texto = "Senhor dos Aneis"
qtd_vogais = 0

for letra in texto:
    if letra in "aeiou":
        print(letra)
        qtd_vogais += 1

print(qtd_vogais)