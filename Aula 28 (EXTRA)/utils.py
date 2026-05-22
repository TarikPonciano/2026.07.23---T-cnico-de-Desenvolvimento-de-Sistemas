# Nível 1 de uso de função (Imprimir algo na tela)

def verificarCPF_nivel1(cpf_verificavel):
    if len(cpf_verificavel) == 11:
        print("CPF TEM O TAMANHO CERTO!")
    else:
        print("CPF COM TAMANHO INVÁLIDO!")

# Nível 2 de uso da função (Retornar informação)

def verificarCPF_nivel2(cpf_verificavel):
    if len(cpf_verificavel) == 11:
        print("CPF COM TAMANHO VÁLIDO")
        return "Válido"
    else:
        print("CPF COM TAMANHO INVÁLIDO")
        return "Inválido"

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