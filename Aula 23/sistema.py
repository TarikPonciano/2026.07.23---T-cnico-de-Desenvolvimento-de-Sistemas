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
        #Valide se o cpf tem 11 caracteres
        print("CADASTRO DE FUNCIONÁRIO")

        nome = input("Digite o nome: ")

        while True:
            cpf = input("Digite o cpf com 11 caracteres: ")
        
            # if len(cpf) != 11 or not cpf.isdigit():
            #     print("CPF INVÁLIDO!")
            # else:
            #     break

            break

        cargo = input("Digite o cargo: ")
        salario = float(input("Digite o salário: "))
        departamento = input("Digite o departamento: ")

        novo_funcionario = {
            "Nome": nome,
            "CPF": cpf,
            "Cargo": cargo,
            "Salário": salario,
            "Departamento": departamento
        }

        funcionarios.append(novo_funcionario)

    elif op == "2":
        # Imprimir a lista de funcionários de forma numerada exibindo apenas o seu nome
        print("SISTEMA DE VISUALIZAÇÃO")
        print(funcionarios)
    elif op == "3":
        # Exibir também a lista de funcionários, porém deveremos perguntar ao usuário qual funcionário queremos ver mais detalhes. Após escolher um funcionário usando o número, exibir a ficha formatada do funcionário.
        print("ESCOLHA UM FUNCIONÁRIO!")
    elif op == "0":
        print("ENCERRANDO PROGRAMA...")
        break


    input("DIGITE ENTER PARA CONTINUAR")