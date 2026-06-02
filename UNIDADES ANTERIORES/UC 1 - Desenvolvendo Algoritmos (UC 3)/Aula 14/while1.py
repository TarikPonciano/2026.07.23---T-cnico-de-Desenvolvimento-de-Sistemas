# Imprima os números de 0 a 10 no terminal

# contador = 0

# while contador < 11:
#     print(contador)
#     contador += 1

# Peça números até que a pessoa escreva o número 0
# Faça a soma desses números
# O maior número
# O menor número
# Quantos números negativos foram digitados
numero = -1
soma = 0

contador_negativos = 0

maior = float("-inf")
menor = float("inf")

while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero < 0:
        contador_negativos += 1

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    soma += numero

print(f"Soma: {soma}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Negativos encontrados: {contador_negativos}")

