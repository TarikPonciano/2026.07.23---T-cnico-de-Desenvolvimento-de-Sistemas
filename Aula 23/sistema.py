# Crie um Sistema de Gerenciamento de RH. Criar um sistema que permita a um usuário cadastrar novos funcionários, ver uma lista de funcionários e ver as informações de um funcionário específico.

funcionarios = [

]

# Crie em um laço de repetição um menu de opções. O menu deve conter as opções Cadastrar Funcionário, Ver Funcionários, Ver Detalhes de Funcionário e Sair. Implemente um texto que informa ao usuário qual opção ele selecionou.

while True:

    print(f"""

--------------- GERENCIAMENTO XYZ ---------------
          
Menu de Opções:
          
          1. Cadastrar Funcionário
          2. Ver Funcionários
          3. Ver Funcionário Específico

          0. Sair
""")
    
    op = input("Digite o número da opção desejada: ")

    if op == "1":
        # Crie um sistema de cadastro onde o usuário preenche as informações do funcionário e na sequência armazena esse funcionário no sistema.
        #Informações do funcionário serão Nome, CPF, Cargo, Salário e Departamento
        print("SISTEMA DE CADASTRO")
    elif op == "2":
        print("SISTEMA DE VISUALIZAÇÃO")
    elif op == "3":
        print("ESCOLHA UM FUNCIONÁRIO!")
    elif op == "0":
        print("ENCERRANDO PROGRAMA...")
        break


    input("DIGITE ENTER PARA CONTINUAR")