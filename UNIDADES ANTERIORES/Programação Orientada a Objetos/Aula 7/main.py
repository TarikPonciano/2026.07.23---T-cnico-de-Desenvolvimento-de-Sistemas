# Forma Antiga com dicionário

# func_1 = {
#     "Nome": "João",
#     "Salário": 5000,
#     "Idade": 25,
#     "Cargo": "Vendedor"
# }

# func_1["Telefone"] = "85988921231"

# print(func_1)

from classFuncionario import Funcionario

func_1 = Funcionario("João", 5000, 25, "Vendedor")

func_2 = Funcionario("Maria", 7000, 35, "Gerente")

print(func_2.nome)