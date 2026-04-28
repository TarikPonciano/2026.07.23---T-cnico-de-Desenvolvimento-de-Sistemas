# 2. Crie um programa que gera bilhetes da mega-sena. O programa deve gerar 6 números inteiros entre 1 e 60 e imprimi-los no formato:
# num1 - num2 - num3 - num4 - num5 - num6
# Bônus: Evite que um mesmo número seja impresso múltiplas vezes
import random

bilhete = ""



for i in range(6):
    num = random.randint(1,60)
    
    if i == 5:
        bilhete += f"{num}"
    else:
        bilhete += f"{num} - "

print(bilhete)

