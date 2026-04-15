# 3. Crie um programa que pede um número inteiro e verifique se ele é par. Imprima na tela o resultado da verificação:

#Ex: "Par: {True/False}"

num = int(input("Digite um número inteiro:"))

verificar_par = num % 2 == 0

print(f"O número {num} é par: {verificar_par}")

