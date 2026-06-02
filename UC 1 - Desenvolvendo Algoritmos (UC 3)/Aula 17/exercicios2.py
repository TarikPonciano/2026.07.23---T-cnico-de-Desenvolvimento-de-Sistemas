# Crie um programa que recebe o valor de 5 produtos. Ao final imprima o total da compra.

valores = []

for i in range(5):
    valor = float(input("Digite o valor de um produto:"))
    valores.append(valor)

# soma_valor = 0

# for v in valores:
#     soma_valor += v

print(sum(valores))
print(valores)