# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

# Maior e Menor Acerto; (Nº Questões, Nome)
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.

# Gabarito da Prova:

# 01 - A

# 02 - B

# 03 - C

# 04 - D

# 05 - E

# 06 - E

# 07 - D

# 08 - C

# 09 - B

# 10 - A


maior_acertos = float("-inf")
nome_maior_acertos = ""

menor_acertos = float("inf")
nome_menor_acertos = ""

qtd_provas = 0

soma_notas = 0

while True: 
    
    qtd_provas += 1
    
    questoes_certas = 0

    nome = input("Digite o seu nome: ")
    

    q1 = input("Digite a resposta da questão (A, B, C, D ou E):")
    if q1 == "A":
        questoes_certas += 1

    q2 = input("Digite a resposta da questão (A, B, C, D ou E):")
    if q2 == "B":
        questoes_certas += 1

    q3 = input("Digite a resposta da questão (A, B, C, D ou E):")
    if q3 == "C":
        questoes_certas += 1

    q4 = input("Digite a resposta da questão (A, B, C, D ou E):")
    if q4 == "D":
        questoes_certas += 1
    

    nota = ((questoes_certas/4)*10)

    print(f"Questões Corretas: {questoes_certas}")
    print(f"Nota: {nota:.1f}")
    
    soma_notas += nota
    

    if questoes_certas > maior_acertos:
        maior_acertos = questoes_certas
        nome_maior_acertos = nome

    if questoes_certas < menor_acertos:
        menor_acertos = questoes_certas
        nome_menor_acertos = nome


    resposta = input("Outro aluno irá realizar a prova? (S/N)")

    if resposta == "N":
        
        break
    
        
media_notas = soma_notas / qtd_provas

print(f"""

Aluno com maior número de acertos: {nome_maior_acertos} ({maior_acertos})

Aluno com menor número de acertos: {nome_menor_acertos} ({menor_acertos})

Provas Realizadas: {qtd_provas}

Média da Turma: {media_notas}

""")
