# 2. Crie um programa que pede números inteiros até que seja digitado -1. Quando o usuário digitar -1, encerre e exiba a soma de todos os números
soma = 0

while True:
    numero = int(input("Digite um número: "))
        
    if numero == -1:
        break

    soma += numero


print(f"A soma dos números foi: {soma}")
