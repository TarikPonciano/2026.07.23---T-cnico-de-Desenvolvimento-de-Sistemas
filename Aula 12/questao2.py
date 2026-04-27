# 2. Faça um programa que repete 4 vezes a seguinte operação: Pede uma nota de um aluno e acrescenta a nova nota à soma das notas. 
# Ao final das repetições exiba a média do aluno e se ele foi aprovado, reprovado ou está de recuperação.(Defina as médias para cada condição)

# Bônus: Considere apenas notas entre 0 e 10.
# Bônus: Permita que o professor decida quantas notas serão registradas.
# Bônus: Exiba o boletim do aluno ao final

soma_notas = 0
contador_notas = 0

boletim = ""

qtd_notas = int(input("Digite quantas notas serão registradas: "))

for i in range(qtd_notas):
    nota = float(input(f"Digite a nota {i+1}: "))

    if nota >= 0 and nota <= 10:
        soma_notas += nota
        contador_notas += 1

        boletim += f"Nota {contador_notas}: {nota}\n"
    else:
        print("Nota inválida")

    

media = soma_notas/contador_notas

print(f"A média do aluno foi: {media}")

if media >= 6 and media <= 10:
    print("Situação: Aprovado!")
elif media >= 4 and media < 6:
    print("Situação: Recuperação!")
elif media >= 0 and media < 4:
    print("Situação: Reprovado!")
else:
    print("MÉDIA INVÁLIDA!")

print(f"Boletim: ")

print(boletim)