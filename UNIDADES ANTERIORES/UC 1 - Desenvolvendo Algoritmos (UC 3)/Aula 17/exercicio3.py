# Crie um programa que recebe 8 notas VÁLIDAS e imprima na tela a média dessas notas. Ao final também exiba o boletim do aluno seguindo o formato:

#Nota 1 - 7
#Nota 2 - 8.5
#Nota 3 - 8

notas = []
alunos = []
# turmas = []

while True:
    aluno = input("Digite o nome do aluno:")
    nota = float(input("Digite a nota:"))
    # turma = input("Digite sua turma")
    
    if nota>= 0 and nota <= 10:
        notas.append(nota)
        alunos.append(aluno)
        # turmas.append(turma)
    else:
        print("NOTA INVÁLIDA")

    if len(notas) >= 3:
        break


media = sum(notas)/len(notas)

print(f"Media da Turma: {media}")

ordem = 0
for n in notas:
    print(f"{alunos[ordem]} - {notas[ordem]:.1f}") 
    ordem += 1

# for aluno,nota in zip(alunos,notas):
#     print(aluno,nota)

# for i,aluno in enumerate(alunos):

#     print(f"{i+1}. {aluno} - {notas[i]} - {turmas[i]}")