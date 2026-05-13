# frutas = {
#     1:  {
#     "Preço": 3.5,
#     "Nome": "Banana",
#     "Estoque": 100
# },
#     2: {
#     "Preço": 4.2,
#     "Nome": "Maçã",
#     "Estoque": 200
# }
# }

# print(frutas[2]["Nome"])

funcionarios = []

nome = input("Digite o nome do funcionário: ")
idade = int(input("Digite a idade do funcionário: "))
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

novo_funcionario = {
    "Nome": nome,
    "Idade": idade,
    "Cargo": cargo,
    "Salário": salario
}

funcionarios.append(novo_funcionario)

print("----------------- TODOS OS FUNCIONÁRIOS -----------------")
print(funcionarios)


print("----------------- UM FUNCIONÁRIO -----------------")
print(funcionarios[0])


print("----------------- NOME DE UM FUNCIONÁRIO -----------------")
print(funcionarios[0]["Nome"])


