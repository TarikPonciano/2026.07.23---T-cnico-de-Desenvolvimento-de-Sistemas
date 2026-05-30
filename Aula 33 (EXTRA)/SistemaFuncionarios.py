import json

def carregar_dados():
    dados = None

    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)
        return dados

def salvar_dados():
    with open("dados.json","w") as arquivo:
        json.dump(funcionarios, arquivo, indent=4)
    
funcionarios = carregar_dados()

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
        salvar_dados()
        break
    else:
        print("DIGITE A OPÇÃO NOVAMENTE")

    input("TECLE ENTER PARA CONTINUAR")