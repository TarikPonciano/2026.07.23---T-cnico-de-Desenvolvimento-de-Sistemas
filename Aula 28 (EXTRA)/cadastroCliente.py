# Nível 1 de uso de função (Imprimir algo na tela)

def verificarCPF_nivel1(cpf_verificavel):
    if len(cpf_verificavel) == 11:
        print("CPF TEM O TAMANHO CERTO!")
    else:
        print("CPF COM TAMANHO INVÁLIDO!")

# nome = input("Digite o nome do cliente:")

# idade = int(input("Digite a idade do cliente: "))

# cpf = input("Digite o cpf: ")

# verificarCPF_nivel1(cpf)

# Nível 2 de uso da função (Retornar informação)

def verificarCPF_nivel2(cpf_verificavel):
    if len(cpf_verificavel) == 11:
        print("CPF COM TAMANHO VÁLIDO")
        return "Válido"
    else:
        print("CPF COM TAMANHO INVÁLIDO")
        return "Inválido"

# nome = input("Digite o nome do cliente:")

# idade = int(input("Digite a idade do cliente: "))

# while True:

#     cpf = input("Digite o cpf: ")

#     resultado = verificarCPF_nivel2(cpf) # Deve retornar "Válido" ou "Inválido"

#     if resultado == "Válido":
#         break
#     else:
#         continue


# novo_cliente = {
#     "Nome": nome,
#     "Idade": idade,
#     "CPF": cpf
# }

# print(novo_cliente)


# Nível 3 de uso da função (Implementar uma funcionalidade do sistema)
def coletarCPF_nivel3():
    while True:
        novo_cpf = input("Digite um cpf: ")

        if len(novo_cpf) == 11:
            print("CPF COM TAMANHO VÁLIDO!")
            return novo_cpf
        else:
            print("CPF COM TAMANHO INVÁLIDO!")
            continue

nome = input("Digite o nome do cliente:")

idade = int(input("Digite a idade do cliente: "))

cpf = coletarCPF_nivel3()


novo_cliente = {
    "Nome": nome,
    "Idade": idade,
    "CPF": cpf
}

print(novo_cliente)