# 2. Fila de atendimento
# Uma clínica tem uma fila com os nomes: ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]. Adicione "Tatiane" ao final da fila e remova "Fábio" porque ele desistiu. Exiba a fila atualizada e o total de pessoas.

pacientes = ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]

pacientes.append("Tatiane")

pacientes.remove("Fábio")

numero = 1
for p in pacientes:
    print(f"{numero}. {p}")
    numero += 1

print(f"Total de Pacientes: {len(pacientes)}")
# paciente_remover = input("Digite o nome de quem você quer remover: ")
# if paciente_remover in pacientes:
#     pacientes.remove(paciente_remover)
# else:
#     print("PACIENTE NÃO EXISTE")

# numero = None

# if numero < len(pacientes):
#     pacientes.pop(numero)