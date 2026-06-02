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
    

qtd_presentes = 0
qtd_ausentes = 0

for aluno in turma:
    print(f"Registro de frequência do aluno {aluno}")
    
    presenca = input("Digite o estado do aluno (presente/ausente):")
    
    if presenca == "presente":
        qtd_presentes += 1

    if presenca == "ausente":
        qtd_ausentes += 1



print(f"""
Presentes: {qtd_presentes}
Ausentes: {qtd_ausentes}
""")

