# 1. Receba 10 números inteiros. Imprima na tela a soma dos números e quantos eram números pares.
soma = 0
contador_par = 0
#contador_impar = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    soma += num

    if num % 2 == 0:
        contador_par += 1
    # else:
    #     contador_impar += 1


print(f"A soma dos números é: {soma}")
print(f"A quantidade de números pares digitados foi: {contador_par}")