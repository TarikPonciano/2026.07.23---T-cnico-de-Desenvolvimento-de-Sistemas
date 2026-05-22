funcionarios = []

def cadastrarFuncionario():


    print("CADASTRO DE FUNCIONÁRIOS")

    nome = input("Digite o nome do Funcionário: ")
    cpf = input("Digite o cpf do Funcionários: ")
    salario = float(input("Digite o salário do Funcionário: R$ "))
    cargo = input("Digite o cargo do Funcionário: ")

    novo_funcionario = {
    "nome": nome,            # Nome completo
    "cpf": cpf,             # CPF (11 dígitos)
    "cargo": cargo,           # Cargo/Função
    "salario": salario        # Salário mensal
}
    funcionarios.append(novo_funcionario)
    

while True:

    print(f"""
BEM VINDO AO SISTEMA RH XYZ
          
Menu:
          
          1. Cadastrar Funcionário
          2. Ver Funcionários
          3. Alterar Funcionário
          4. Remover Funcionário

          0. Sair
""")
    
    op = input("Digite a opção desejada:")

    if op == "1":
        cadastrarFuncionario()
    elif op == "2":
        print(funcionarios)
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "0":
        print("SAINDO DO PROGRAMA...")
        break
    else:
        print("DIGITE A OPÇÃO NOVAMENTE")

    input("TECLE ENTER PARA CONTINUAR")