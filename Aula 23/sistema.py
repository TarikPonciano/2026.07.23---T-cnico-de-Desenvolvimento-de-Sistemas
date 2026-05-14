# Crie um Sistema de Gerenciamento de RH. Criar um sistema que permita a um usuário cadastrar novos funcionários, ver uma lista de funcionários e ver as informações de um funcionário específico.

funcionarios = [
    {
        "Nome": "Ana Silva Santos",
        "CPF": "12345678910",
        "Cargo": "Analista de Sistemas",
        "Salário": 5500.00,
        "Departamento": "Tecnologia"
    },
    {
        "Nome": "Bruno Oliveira Costa",
        "CPF": "23456789011",
        "Cargo": "Desenvolvedor Python",
        "Salário": 6000.00,
        "Departamento": "Tecnologia"
    },
    {
        "Nome": "Carlos Mendes Pereira",
        "CPF": "34567890112",
        "Cargo": "Gerente de Projetos",
        "Salário": 7500.00,
        "Departamento": "Gestão"
    },
    {
        "Nome": "Diana Ferreira Lima",
        "CPF": "45678901213",
        "Cargo": "Designers Gráfico",
        "Salário": 4800.00,
        "Departamento": "Marketing"
    },
    {
        "Nome": "Eduardo Santos Gomes",
        "CPF": "56789012314",
        "Cargo": "Contador",
        "Salário": 5200.00,
        "Departamento": "Financeiro"
    },
    {
        "Nome": "Fernanda Rocha Alves",
        "CPF": "67890123415",
        "Cargo": "Vendedor",
        "Salário": 4500.00,
        "Departamento": "Vendas"
    },
    {
        "Nome": "Gabriel Costa Silva",
        "CPF": "78901234516",
        "Cargo": "Especialista em Infraestrutura",
        "Salário": 6500.00,
        "Departamento": "Tecnologia"
    },
    {
        "Nome": "Helena Martins Souza",
        "CPF": "89012345617",
        "Cargo": "Recursos Humanos",
        "Salário": 5000.00,
        "Departamento": "RH"
    },
    {
        "Nome": "Igor Ferreira Duarte",
        "CPF": "90123456718",
        "Cargo": "Analista de Qualidade",
        "Salário": 5300.00,
        "Departamento": "Qualidade"
    },
    {
        "Nome": "Julia Nascimento Oliveira",
        "CPF": "01234567819",
        "Cargo": "Especialista em Marketing",
        "Salário": 5800.00,
        "Departamento": "Marketing"
    },
    {
        "Nome": "Kevin Dias Ribeiro",
        "CPF": "12345678920",
        "Cargo": "Desenvolvedor Frontend",
        "Salário": 5900.00,
        "Departamento": "Tecnologia"
    },
    {
        "Nome": "Lucia Goulart Pereira",
        "CPF": "23456789021",
        "Cargo": "Gerente de Vendas",
        "Salário": 7200.00,
        "Departamento": "Vendas"
    },
    {
        "Nome": "Mariano Silva Souza",
        "CPF": "34567890122",
        "Cargo": "Advogado",
        "Salário": 8000.00,
        "Departamento": "Jurídico"
    },
    {
        "Nome": "Natalia Campos Martins",
        "CPF": "45678901223",
        "Cargo": "Gerente Administrativo",
        "Salário": 6800.00,
        "Departamento": "Administração"
    },
    {
        "Nome": "Otavio Ribeiro Costa",
        "CPF": "56789012324",
        "Cargo": "Assistente Administrativo",
        "Salário": 3800.00,
        "Departamento": "Administração"
    },
    {
        "Nome": "Patricia Lima Alves",
        "CPF": "67890123425",
        "Cargo": "Analista Financeiro",
        "Salário": 6200.00,
        "Departamento": "Financeiro"
    },
    {
        "Nome": "Quincy Santos Garcia",
        "CPF": "78901234526",
        "Cargo": "Coordenador de Logística",
        "Salário": 5400.00,
        "Departamento": "Logística"
    },
    {
        "Nome": "Rafael Monteiro Duarte",
        "CPF": "89012345627",
        "Cargo": "Especialista em Segurança",
        "Salário": 7000.00,
        "Departamento": "Tecnologia"
    },
    {
        "Nome": "Sophia Carvalho Neves",
        "CPF": "90123456728",
        "Cargo": "Atendente de Suporte",
        "Salário": 3500.00,
        "Departamento": "Suporte"
    },
    {
        "Nome": "Tiago Barros Mendes",
        "CPF": "01234567829",
        "Cargo": "Supervisora de Operações",
        "Salário": 6500.00,
        "Departamento": "Operações"
    }
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
        print("LISTA DE FUNCIONÁRIOS")
        contador = 1
        for funcionario in funcionarios:
            print(f"{contador}. {funcionario["Nome"]} - {funcionario["CPF"]}")
            contador += 1


    elif op == "3":
        # Exibir também a lista de funcionários, porém deveremos perguntar ao usuário qual funcionário queremos ver mais detalhes. Após escolher um funcionário usando o número, exibir a ficha formatada do funcionário.
        print("LISTA DE FUNCIONÁRIOS")
        contador = 1
        for funcionario in funcionarios:
            print(f"{contador}. {funcionario["Nome"]} - {funcionario["CPF"]}")
            contador += 1

        numero = int(input("Digite o número do funcionário desejado para ver mais informações: (0=Cancelar)"))

        if numero == 0:
            print("Cancelando operação...")
        else:
            funcionario_escolhido = funcionarios[numero-1]

            print(f"""
FICHA DE FUNCIONÁRIO:
                  
    Nome: {funcionario_escolhido["Nome"]}
    CPF: {funcionario_escolhido["CPF"]}
    Cargo: {funcionario_escolhido["Cargo"]}
    Salário: R$ {funcionario_escolhido["Salário"]:,.2f}
    Departamento: {funcionario_escolhido["Departamento"]}

""")
    elif op == "0":
        print("ENCERRANDO PROGRAMA...")
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA!")



    input("DIGITE ENTER PARA CONTINUAR")