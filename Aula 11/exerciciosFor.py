# Imprima todos os números de 0 até 1000
# for i in range(1001):
#     print(i)

# Imprima todos os números pares de 0 até 1000
# for i in range(0, 1001,2):
#     print(i)

# for i in range(1,1001):
#     if i % 2 == 0:
#         print(i)



# Imprima a soma dos números pares de 0 até 1000
# soma = 0

# for i in range(0,1001):
#     if i % 2 == 0:
#         soma += i

#         print(f"A soma é: {soma}")


# Imprima a quantidade de números pares de 0 até 1000

# contador = 0

# for i in range(0,1001):
#     if i % 2 == 0:
#         contador += 1

# print(f"O número de pares é: {contador}")

# Combinando tudo:

soma = 0
contador = 0
produto = 1

for i in range(1,1001):
    if i % 2 == 0:
        print(i)
        soma += i
        contador += 1
        produto *= i

print(f"A soma é: {soma}")
print(f"O número de pares é: {contador}")
print(f"O produto dos números é: {produto}")