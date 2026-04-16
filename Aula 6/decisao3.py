# 3. Melhore o programa do aluno para: Escreva um programa que recebe 4 notas, calcule a média do aluno e imprima na tela a média calculada e a situação de acordo com a seguinte regra:

#media maior ou igual a 7 e media menor ou igual a 10: aprovado
#media menor que 7 e media maior ou igual a 4: recuperação
#media menor que 4 e media maior ou igual a 0: reprovado

nome = input("Digite o nome do aluno: ")


nota1 = float(input("Digite a nota 1: "))

nota2 = float(input("Digite a nota 2: "))

nota3 = float(input("Digite a nota 3: "))

nota4 = float(input("Digite a nota 4: "))

media_notas = (nota1 + nota2 + nota3 + nota4) / 4
situacao = "NÃO DEFINIDO"

if media_notas >= 7 and media_notas <= 10:
    situacao = "Aprovado"
    print("Sua situação é APROVADO!")
elif media_notas < 7 and media_notas >= 4:
    situacao = "Recuperação"
    print("Sua situação é RECUPERAÇÃO!")
elif media_notas < 4 and media_notas >= 0:
    situacao = "Reprovado"
    print("Sua situação é REPROVADO!")
else:
    situacao = "Média Inválida"
    print("Média inválida")

if situacao == "Média Inválida":
    print("NÃO FOI POSSÍVEL EMITIR O BOLETIM")
    

print(f"""
Boletim Escolar:
      
AV1: {nota1}
AV2: {nota2}
AV3: {nota3}
AV4: {nota4}

Média: {media_notas:.1f}
Situação: {situacao}

""")







