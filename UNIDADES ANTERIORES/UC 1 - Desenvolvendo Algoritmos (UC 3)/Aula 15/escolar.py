# Crie um sistema escolar onde para calcular a média de um aluno devemos receber 4 notas válidas (entre 0 e 10). Ao final exiba o status de aprovação do aluno.

# qtd_notas_validas = 0
# soma_notas = 0

# while qtd_notas_validas < 4:

#     nota = float(input("Digite uma nota entre 0 e 10: "))

#     if nota < 0 or nota > 10:
#         print("Nota inválida...")
#         print("Digite novamente...")
#     else:
#         qtd_notas_validas += 1
#         soma_notas += nota


qtd_notas_validas = 0

soma_notas = 0

# Algoritmo de coletar notas
while True:
    
    nota = float(input("Digite uma nota entre 0 e 10:"))

    if nota < 0 or nota > 10:
        print("Nota Inválida... Digite Novamente...")
        continue

    qtd_notas_validas += 1
    soma_notas += nota

    if qtd_notas_validas >= 4:
        break



media = soma_notas/qtd_notas_validas

print(f"Média: {media}")

if media >= 7 and media <= 10:
    print("APROVADO")
elif media >=4 and media < 7:
    print("RECUPERAÇÃO")
elif media >= 0 and media < 4:
    print("REPROVADO")
else:
    print("De alguma maneira a média é inválida")