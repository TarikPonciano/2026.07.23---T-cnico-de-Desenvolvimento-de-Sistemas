#1. Crie um programa de cadastro de pacientes. O programa deve rodar em um laço while e deve preencher uma lista de pacientes. Cada paciente possui nome, idade, gênero e peso. Colete as informações de cada paciente e armazene na lista de pacientes, até a pessoa desejar encerrar o programa. Ao final do programa, exiba a lista de pacientes. Exiba também quantos pacientes tinham mais que 30 anos e quantos pacientes tinham 30 anos ou menos.

pacientes = []

while True:

    nome = input("Digite o nome do paciente:")
    idade = int(input("Digite a idade do paciente:"))
    peso = float(input("Digite o peso do paciente:"))
    genero = input("Digite o gênero do paciente: ")

    novo_paciente = {
        "Nome": nome,
        "Idade": idade,
        "Peso": peso,
        "Gênero": genero
    }

    pacientes.append(novo_paciente)

    continuar = input("Deseja continuar? (S/N)")

    if continuar == "N":
        print("Encerrando cadastros...")
        break

print("Lista de Pacientes")

contador = 1
qtd_acima30 = 0
qtd_abaixo30 = 0
nomes_acima30 = []
nomes_abaixo30 = []

for paciente in pacientes:
    print(f"{contador}. {paciente["Nome"]}")
    contador += 1

    if paciente["Idade"] > 30:
        qtd_acima30 += 1
        nomes_acima30.append(paciente["Nome"])
    
    if paciente["Idade"] <= 30:
        qtd_abaixo30 += 1
        nomes_abaixo30.append(paciente["Nome"])


print(f"""
Total Acima de 30: {qtd_acima30} {nomes_acima30}

Total Abaixo de 30: {qtd_abaixo30} {nomes_acima30}
""")