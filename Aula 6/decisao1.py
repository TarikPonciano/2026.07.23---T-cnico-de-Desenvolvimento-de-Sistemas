# 1. Receba a nota de um aluno, imprima "Aprovado" se a nota for maior ou igual a 7, se não imprima "Reprovado".

nota = input("Digite a nota do aluno: ")

if nota >= 7:
    print(f"Você foi aprovado! Sua nota foi {nota}!")
else:
    print(f"Você foi reprovado! Sua nota foi {nota}!")