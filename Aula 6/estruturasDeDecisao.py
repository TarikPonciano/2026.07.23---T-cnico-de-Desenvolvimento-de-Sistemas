# Crie um programa que recebe a idade de uma pessoa e imprime na tela "Seu acesso está liberado" quando ela for maior de idade e "Acesso Negado" quando ela for menor de idade.

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Seu acesso está liberado")
    print("Você é maior de idade")
else:
    print("Acesso negado")
    print("Você é menor de idade")

print("Boa noite!")


# Crie um programa que pergunta o turno atual (Dia/Noite). Se o turno for Dia, imprima na tela "Bom dia!", se não imprima na tela "Boa noite!"