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
def cpf_exist(cpf):
    for dados in funcionarios:
        if dados["cpf"]==cpf:
            return True
    return False

# VERSÃO EUGENIO
# def alterar_funcionario():
#     print("ALTERANDO DADOS DO FUNCIONÁRIO")

#     if len(funcionarios) == 0:
#         print("Nenhum funcionário Cadastrado")
#         return
    
#     ver_funcionarios()

#     while True:
#         try:
#             posicao = int(input("Digite o número do funcionário"))
#             if posicao < 1 or posicao >len(funcionarios):
#                 print("Funcionário não encontrado")
#             else:
#                 indice = posicao - 1
#                 break
#         except ValueError:
#             print("Digite apenas números")
        
#     funcionario = funcionarios[indice]

#     print("funcionário selecionado: ")
#     print(funcionario)
#     print("----------------------")

#     novo_nome = input(f"Novo nome:[ {funcionario['nome']} ]: ")

#     if novo_nome != "":
#         funcionario["nome"] = novo_nome
    
#     novo_cargo = input(f"Novo nome:[ {funcionario['cargo']} ]: ")

#     if novo_cargo != "":
#         funcionario["cargo"] = novo_cargo
    


        


def cadastrar_funcionario():
    print("CADASTRO DE FUNCIONÁRIOS")

    while True:
        nome = input("Digite o nome do Funcionário: ")
        if nome == "":
            print("Preencha o campo nome")
        else:
            break

    while True:
        cpf = input("Digite o cpf do Funcionários: ")
        if cpf =="":
            print("Digite um CPF")
        elif len(cpf) != 11:
            print("""Quantidade de dígitos fora do padrão
                  """)
        elif not cpf.isdigit():
            print("Dados inválidos")
        elif cpf_exist(cpf):
            print("CPF já cadastrado. Tente outro número")
        else:
            break
    while True:
        try:
            salario = input("Digite o salário do Funcionário: R$ ")
            salario = salario.replace(",",".")
            salario = float(salario)
            if salario <= 0:
                print("Salário deve ser maior que 0")
            else:
                break

        except ValueError:
            print("Digite apenas números")
    
        
    while True:
        cargo = input("Digite o cargo do Funcionário: ")
        if cargo == "":
            print("Digite o nome do Cargo")
        else:
            break

    novo_funcionario = {
    "nome": nome,            # Nome completo
    "cpf": cpf,             # CPF (11 dígitos)
    "cargo": cargo,           # Cargo/Função
    "salario": salario        # Salário mensal
}
    funcionarios.append(novo_funcionario)

def ver_funcionarios():

    print("LISTA DE FUNCIONÁRIOS")
    contador = 1
    for funcionario in funcionarios:
        print(f"{contador}. {funcionario['nome']} - {funcionario['cpf']}- {funcionario['cargo']}- {funcionario['salario']}")
        contador += 1


def escolher_funcionario():
    while True:
        try:
            num = int(input("Digite o número do funcionário:"))

            if num <1 or num > len(funcionarios):
                print("DIGITE UM NÚMERO VÁLIDO")
                continue
            else:
                print("FUNCIONÁRIO ENCONTRADO!")
                return num
        except:
            print("DIGITE APENAS NÚMEROS")

def remover_funcionario():

    ver_funcionarios()

    num_funcionario = escolher_funcionario()
    
    funcionario_removido = funcionarios.pop(num_funcionario-1)

    print(f"{funcionario_removido["nome"]} foi promovido para cliente!")

def alterar_funcionario():

    ver_funcionarios()

    num_funcionario = escolher_funcionario()

    funcionario_escolhido = funcionarios[num_funcionario-1]

    print(f"""
    INFORMAÇÕES DO FUNCIONÁRIO:
          
    NOME: {funcionario_escolhido["nome"]}
    CPF: {"*"*8}{funcionario_escolhido['cpf'][8::]}
    SALÁRIO: R$ {funcionario_escolhido['salario']:,.2f}
    CARGO: {funcionario_escolhido['cargo']}
          """)
    print("ALTERE AS INFORMAÇÕES DO FUNCIONÁRIO. DEIXE VAZIO PARA NÃO ALTERAR!")

    novo_nome = input(f"Digite o novo nome ({funcionario_escolhido["nome"]}): ")
    if novo_nome:
        funcionario_escolhido["nome"] = novo_nome

    novo_cpf = input(f"Digite o novo cpf: ")
    if novo_cpf:
        funcionario_escolhido["cpf"] = novo_cpf

    novo_salario = input(f"Digite o novo salario: ")
    if novo_salario:
        funcionario_escolhido["salario"] = float(novo_salario)

    novo_cargo = input(f"Digite o novo cargo: ")
    if novo_cargo:
        funcionario_escolhido["cargo"] = novo_cargo

    print(f"""
    INFORMAÇÕES DO FUNCIONÁRIO:
          
    NOME: {funcionario_escolhido["nome"]}
    CPF: {"*"*8}{funcionario_escolhido['cpf'][8::]}
    SALÁRIO: R$ {funcionario_escolhido['salario']:,.2f}
    CARGO: {funcionario_escolhido['cargo']}
          """)

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
        ver_funcionarios()
    elif op == "3":
        alterar_funcionario()
    elif op == "4":
        # Mostrar a lista de funcionários na tela
        # Pedir para o usuário digitar o número do funcionário
        # Validar se o número que o usuário digitou é possível
        # Remover o funcionário escolhido
        remover_funcionario()
    elif op == "0":
        print("SAINDO DO PROGRAMA...")
        break
    else:
        print("DIGITE A OPÇÃO NOVAMENTE")

    input("TECLE ENTER PARA CONTINUAR")