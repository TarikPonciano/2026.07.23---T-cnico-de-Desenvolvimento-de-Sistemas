# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Digite um número inteiro: "))

primo = True

for i in range(2, numero):

    if numero % i == 0:
        primo = False
        break


if primo:
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo!")