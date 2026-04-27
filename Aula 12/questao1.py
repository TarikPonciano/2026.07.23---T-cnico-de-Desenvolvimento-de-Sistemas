# 1. Peça um número inteiro ao usuário, na sequência exiba na tela a tabuada desse número (multiplicações de 0 a 10)

num = int(input("Digite um número:"))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
    