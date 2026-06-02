# Tipos Simples
# nome1 = "José"
# nome2 = "Maria"

# nome1 = nome2

# nome1 = "Carlos"


# print(nome1)
# print(nome2)

# Referência em listas
# frutas = ["Uva", "Maçã", "Pêra"]

# vegetais = ["Alface", "Cebola", "Pepino"]

# vegetais = frutas

# frutas.append("Abacaxi")

# vegetais.remove("Uva")

# print(frutas)

# print(vegetais)

# Referência em Dicionários
funcionarios = [
    {"Nome": "Joaquim", "Salário": 3000, "Cargo": "Recepcionista"},
    {"Nome": "Joana", "Salário": 5000, "Cargo": "Vendedor"}
]

funcionarios[1]["Cargo"] = "Gerente"

funcionario_escolhido = funcionarios[1]
funcionario_escolhido["Salário"] = 7000

print(funcionarios)
