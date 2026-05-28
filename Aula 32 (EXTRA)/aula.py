funcionarios = [
    {
        "nome": "Ana Beatriz Souza",
        "cpf": "12345678901",
        "cargo": "Analista de Sistemas",
        "salario": 5200.00
    }
]


def cpf_exist(cpf):
    for dados in funcionarios:
        if dados["cpf"] == cpf:
            return True
    return False



def cadastrar_funcionario():
    print("CADASTRO DE FUNCIONÁRIOS")
    while True:
        nome = input("DIGITE UM NOME: ")
        if nome == "":
            print(" Digite um nome")
        else:
            break
    while True:
        cpf = input("Digite CPF: ").strip()
        if cpf == "":
            print("cpf vazio")
        elif not cpf.isdigit():
            print("cpf só numeros")
        elif cpf_exist(cpf):
            print("cpf já existe")
        elif len(cpf) != 11:
            print("11 dígitos")
        else:
            break
    while True:
        try:
            salario = input("DIGITE SALÁRIO: R$ ").strip()

            salario = salario.replace(",", ".")

            salario = float(salario)

            if salario <= 0:
                print("Erro: o salário deve ser maior que zero.")
            else:
                break

        except ValueError:
            print("Erro: digite apenas números. Exemplo: 3500 ou 3500.50")
        

    cargo = input("DIGITE CARGO: ").strip()
    novo_cadastro = {
        "nome": nome,
        "cpf": cpf,
        "salario": salario,
        "cargo": cargo,
    }
    funcionarios.append(novo_cadastro)
    print("")
    print("CADASTRADO com sucesso")
    print("")
    print("Você cadastrou: ")
    print("")
    print("")
    print(funcionarios[-1])
    print("")
    ver_funcionarios()


def ver_funcionarios():

    print("LISTA DE FUNCIONÁRIOS")
    contador = 1
    for funcionario in funcionarios:
        print(
            f"{contador}. {funcionario['nome']} - {funcionario['cpf']}- {funcionario['cargo']}")
        contador += 1


def alterar_funcionario():
    print("ALTERAR FUNCIONÁRIO")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    ver_funcionarios()

    while True:
        try:
            posicao = int(
                input("Digite o número do funcionário que deseja alterar: "))

            if posicao < 1 or posicao > len(funcionarios):
                print("Funcionário não encontrado. Digite um número válido.")
            else:
                indice = posicao - 1
                break

        except ValueError:
            print("Digite apenas números.")
    funcionario = funcionarios[indice]

    print("")
    print("Funcionário selecionado:")
    print(funcionario)
    print("")

    novo_nome = input(f"Novo nome [{funcionario['nome']}]: ").strip()

    if novo_nome != "":
        funcionario["nome"] = novo_nome
    novo_cargo = input(f"Novo cargo [{funcionario['cargo']}]: ").strip()

    if novo_cargo != "":
        funcionario["cargo"] = novo_cargo


def remover_funcionario():
    print("REMOVER FUNCIONÁRIO")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    ver_funcionarios()

    while True:
        try:
            posicao = int(
                input("Digite o número do funcionário que deseja remover: "))

            if posicao < 1 or posicao > len(funcionarios):
                print("Funcionário não encontrado. Digite um número válido.")
            else:
                indice = posicao - 1
                break

        except ValueError:
            print("Digite apenas números.")

    funcionario = funcionarios[indice]

    print("")
    print("Funcionário selecionado para remoção:")
    print(f"Nome: {funcionario['nome']}")
    print(f"CPF: {funcionario['cpf']}")
    print(f"Cargo: {funcionario['cargo']}")
    print(f"Salário: R$ {funcionario['salario']:.2f}")
    print("")

    confirmar = input(
        "Tem certeza que deseja remover este funcionário? (s/n): ").strip().lower()

    if confirmar == "s":
        funcionarios.pop(indice)
        print("Funcionário removido com sucesso!")
    else:
        print("Remoção cancelada.")

sistema = "SISTEMA RH XYZ ATUALIZADO"

while True:

    print(f"""
BEM VINDO AO {sistema}          
Menu:          
          1. Cadastrar Funcionário
          2. Ver Funcionários
          3. Alterar Funcionário
          4. Remover Funcionário
          0. Sair
""")

    op = input("Digite a opção desejada:")

    if op == "1":
        cadastrar_funcionario()
    elif op == "2":
        ver_funcionarios()
    elif op == "3":
        alterar_funcionario()
    elif op == "4":
        remover_funcionario()
    else: 
        print("SAINDO DO PROGRAMA...")
        input("TECLE ENTER PARA CONTINUAR") 
        break

