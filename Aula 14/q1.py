# 1. Crie um programa que imprime na tela os números de 0 a 100

# Imprimir os números pares de 0 a 100

# Imprimir os primeiros 100 números pares

contador = 0
numero_atual = 0

while contador <= 100:
    if numero_atual % 2 == 0:
        print(numero_atual)
        contador += 1
    numero_atual += 1