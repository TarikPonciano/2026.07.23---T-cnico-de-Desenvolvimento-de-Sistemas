funcionarios = [
    {
        "nome": "Ana Beatriz Souza",
        "cpf": "12345678901",
        "cargo": "Analista de Sistemas",
        "salario": 5200.00
    },
    {
        "nome": "Carlos Eduardo Lima",
        "cpf": "23456789012",
        "cargo": "Desenvolvedor Backend",
        "salario": 6800.00
    },
    {
        "nome": "Fernanda Alves Rocha",
        "cpf": "34567890123",
        "cargo": "Designer UX/UI",
        "salario": 4700.00
    },
    {
        "nome": "João Pedro Martins",
        "cpf": "45678901234",
        "cargo": "Administrador de Redes",
        "salario": 5900.00
    },
    {
        "nome": "Mariana Costa Silva",
        "cpf": "56789012345",
        "cargo": "Gerente de Projetos",
        "salario": 8500.00
    },
    {
        "nome": "Lucas Ferreira Gomes",
        "cpf": "67890123456",
        "cargo": "Técnico em Suporte",
        "salario": 3200.00
    },
    {
        "nome": "Patrícia Mendes Araújo",
        "cpf": "78901234567",
        "cargo": "Analista de Dados",
        "salario": 6100.00
    },
    {
        "nome": "Rafael Henrique Batista",
        "cpf": "89012345678",
        "cargo": "Desenvolvedor Frontend",
        "salario": 6400.00
    },
    {
        "nome": "Juliana Oliveira Castro",
        "cpf": "90123456789",
        "cargo": "Assistente Administrativo",
        "salario": 2800.00
    },
    {
        "nome": "Thiago Ribeiro Santos",
        "cpf": "11223344556",
        "cargo": "Coordenador de TI",
        "salario": 7800.00
    },
    {
        "nome": "Camila Nunes Pereira",
        "cpf": "22334455667",
        "cargo": "Recursos Humanos",
        "salario": 4300.00
    },
    {
        "nome": "Bruno Carvalho Freitas",
        "cpf": "33445566778",
        "cargo": "Engenheiro de Software",
        "salario": 9200.00
    },
    {
        "nome": "Larissa Barbosa Melo",
        "cpf": "44556677889",
        "cargo": "Secretária",
        "salario": 2600.00
    },
    {
        "nome": "Diego Fernandes Pinto",
        "cpf": "55667788990",
        "cargo": "Analista Financeiro",
        "salario": 5100.00
    },
    {
        "nome": "Renata Vieira Campos",
        "cpf": "66778899001",
        "cargo": "Contadora",
        "salario": 7000.00
    },
    {
        "nome": "Felipe Moura Teixeira",
        "cpf": "77889900112",
        "cargo": "Desenvolvedor Mobile",
        "salario": 6600.00
    },
    {
        "nome": "Aline Rodrigues Farias",
        "cpf": "88990011223",
        "cargo": "Marketing Digital",
        "salario": 4500.00
    },
    {
        "nome": "Gustavo Almeida Cunha",
        "cpf": "99001122334",
        "cargo": "Supervisor de Produção",
        "salario": 6200.00
    },
    {
        "nome": "Vanessa Lopes Cardoso",
        "cpf": "10111213141",
        "cargo": "Consultora Comercial",
        "salario": 4800.00
    },
    {
        "nome": "Ricardo Moreira Dias",
        "cpf": "12131415161",
        "cargo": "Auxiliar de Escritório",
        "salario": 2400.00
    }
]

def cadastrar_funcionario():
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
        cadastrar_funcionario()
    elif op == "2":
        # Criar uma função chamada ver_funcionarios() que exibe os funcionários em uma lista numerada no formato {numero}. {nome} - {cpf}
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