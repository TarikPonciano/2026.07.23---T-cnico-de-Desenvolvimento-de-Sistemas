# 3. Crie um programa que recebe 5 números reais, exiba na tela o maior entre os números inseridos.

maior = None

for i in range(5):
    num = float(input("Digite um número: "))

    if maior == None:
        maior = num

    if num > maior:
        maior = num
    

print(f"O maior número: {maior}")

