# Crie um programa que recebe a idade de uma pessoa e imprime na tela "Seu acesso está liberado" quando ela for maior de idade e "Acesso Negado" quando ela for menor de idade.

# idade = int(input("Digite sua idade:"))

# if idade >= 18:
#     print("Seu acesso está liberado")
#     print("Você é maior de idade")
# else:
#     print("Acesso negado")
#     print("Você é menor de idade")

# print("Boa noite!")

# Crie um programa que pergunta o turno atual (Dia/Noite). Se o turno for Dia, imprima na tela "Bom dia!", se não imprima na tela "Boa noite!"

#Melhore o programa para incluir o turno da Tarde

turno = input("Digite o turno atual (Manhã/Tarde/Noite):") 

if turno == "Manhã":
    print("Bom Dia!")
elif turno == "Tarde":
    print("Boa Tarde!")
elif turno == "Noite":
    print("Boa Noite!")
elif turno == "Madrugada":
    print("Boa Madrugada!")
else:
    print("Digite um turno válido!")


# 1. Receba a nota de um aluno, imprima "Aprovado" se a nota for maior ou igual a 7, se não imprima "Reprovado".

# 2.Receba o nome de um animal se o animal for gato imprima "Miau Miau", se o animal for cachorro imprima "Au Au", se o animal for papagaio imprima "Lôro quer biscoito" se não for nenhum dos animais imprima "Animal Não Catalogado".

# 3. Melhore o programa do aluno para: Escreva um programa que recebe 4 notas, calcule a média do aluno e imprima na tela a média calculada e a situação de acordo com a seguinte regra:

#media maior ou igual a 7 e media menor ou igual a 10: aprovado
#media menor que 7 e media maior ou igual a 4: recuperação
#media menor que 4 e media maior ou igual a 0: reprovado

