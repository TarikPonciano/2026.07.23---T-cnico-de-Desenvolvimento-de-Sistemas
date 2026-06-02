# 6. Controle de presença
# Faça um programa que preenche uma lista de alunos com quantos alunos o usuário desejar. Continue até o usuário deixar o nome vazio. Use um for com enumerate() para percorrer a lista de nomes e perguntar ao usuário "presente" ou "ausente" para cada um. Ao final, exiba quantos alunos estiveram presentes e quantos faltaram.

turma = []

while True:
    aluno = input(f"Digite o nome do aluno Nº{len(turma)+1}:") 

    if aluno == "":
        break

    turma.append(aluno)

    # resp = input("Quer continuar? (S/N)")

    # if resp.lower() in ["n", "não", "no"]:
    #     break    
    

frequencias = []

for aluno in turma:
    print(f"Registro de frequência do aluno {aluno}")
    
    presenca = input("Digite o estado do aluno (presente/ausente):")
    
    frequencias.append(presenca)


print(f"""

Presentes: {frequencias.count("presente")}
Ausentes: {frequencias.count("ausente")}
""")

print("LISTA DE FREQUÊNCIA")

print("NOME | FREQUÊNCIA")

for aluno, presenca in zip(turma,frequencias):
    print(f"{aluno} | {presenca}")