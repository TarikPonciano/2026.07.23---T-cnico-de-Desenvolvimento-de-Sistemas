# Capítulo 5 · Etapa 3 · main.py · CRUD do Sistema RH com a classe Banco
# Funcionários: ver, escolher (ver detalhes), cadastrar, alterar e remover.
# Setores: ver, escolher, cadastrar e alterar.

from classBanco import Banco

banco = Banco()


def verFuncionarios():
    print("LISTA DE FUNCIONÁRIOS")

    funcionarios = banco.consultar('''
        SELECT f.cod_funcionario, f.nome_funcionario, f.cpf_funcionario, f.cargo_funcionario,
               f.salario_funcionario, f.cod_setor, s.nome_setor
        FROM funcionarios f
        JOIN setores s ON f.cod_setor = s.cod_setor
        ORDER BY f.cod_funcionario ASC;
    ''')

    print("Código | Nome | CPF | Cargo | Salário | Cod Setor | Setor")

    if (len(funcionarios) == 0):
        print("NÃO HÁ FUNCIONÁRIOS CADASTRADOS")
        return

    # Alternativa: for func in funcionarios, e func[0], func[1]...
    for cod_func, nome_func, cpf_func, cargo_func, salario_func, cod_setor, nome_setor in funcionarios:
        print(f"{cod_func} | {nome_func} | {cpf_func} | {cargo_func} | R$ {salario_func:,.2f} | {cod_setor} | {nome_setor}")


def escolherFuncionario():
    verFuncionarios()

    cod_escolhido = int(input("Digite o código do funcionário desejado: "))

    consulta = banco.consultar('''
        SELECT f.cod_funcionario, f.nome_funcionario, f.cpf_funcionario, f.cargo_funcionario,
               f.salario_funcionario, f.cod_setor, s.nome_setor
        FROM funcionarios f
        JOIN setores s ON f.cod_setor = s.cod_setor
        WHERE f.cod_funcionario = %s;
    ''', (cod_escolhido,))

    if (len(consulta) == 0):
        print("Funcionário não encontrado!")
        return None

    funcionario = consulta[0]

    print(f'''
    Ficha do Funcionário:

    Código: {funcionario[0]}
    Nome: {funcionario[1]}
    CPF: {funcionario[2]}
    Cargo: {funcionario[3]}
    Salário: R$ {funcionario[4]:,.2f}
    Setor: {funcionario[6]}
    ''')

    return funcionario


def cadastrarFuncionario():
    print("CADASTRO DE NOVO FUNCIONÁRIO")

    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o cpf do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    verSetores()

    cod_setor = int(input("Digite o código do setor do funcionário: "))

    try:
        banco.manipular('''
            INSERT INTO funcionarios
            VALUES (default, %s, %s, %s, %s, %s);
        ''', (nome, cpf, cargo, salario, cod_setor))
        print("FUNCIONÁRIO CADASTRADO COM SUCESSO!")
    except Exception as error:
        print("ERRO AO CADASTRAR FUNCIONÁRIO")


def alterarFuncionario():
    print("ATUALIZAÇÃO DE FUNCIONÁRIO")

    funcionario = escolherFuncionario()

    if (not funcionario):
        print("Não é possível alterar o funcionário. Cheque o código escolhido...")
        return

    continuar = input("Deseja alterar as informações do funcionário? (S/N) ")

    if (continuar != "S"):
        return

    cod, nome, cpf, cargo, salario, cod_setor, nome_setor = funcionario

    print("ALTERAR DADOS:")
    print("(Deixe vazio para manter o original)")

    novo_nome = input(f"Digite o novo nome ({nome}): ").strip()
    if (novo_nome):
        nome = novo_nome

    novo_cpf = input(f"Digite o novo cpf ({cpf}): ").strip()
    if (novo_cpf):
        cpf = novo_cpf

    novo_cargo = input(f"Digite o novo cargo ({cargo}): ").strip()
    if (novo_cargo):
        cargo = novo_cargo

    novo_salario = input(f"Digite o novo salário (R$ {salario:,.2f}): ").strip()
    if (novo_salario):
        salario = float(novo_salario)

    verSetores()
    novo_setor = input(f"Digite o código do novo setor ({cod_setor}): ").strip()
    if (novo_setor):
        cod_setor = int(novo_setor)

    try:
        banco.manipular('''
            UPDATE funcionarios
            SET nome_funcionario = %s,
                cpf_funcionario = %s,
                cargo_funcionario = %s,
                salario_funcionario = %s,
                cod_setor = %s
            WHERE cod_funcionario = %s;
        ''', (nome, cpf, cargo, salario, cod_setor, cod))
        print("FUNCIONÁRIO ATUALIZADO!")
    except Exception as error:
        print("Ocorreu um erro na atualização!")


def removerFuncionario():
    print("REMOÇÃO DE FUNCIONÁRIO")

    funcionario = escolherFuncionario()

    if (not funcionario):
        print("Funcionário não encontrado!")
        return

    continuar = input("DESEJA REALMENTE APAGAR ESSE FUNCIONÁRIO? (S/N) ")

    if (continuar != "S"):
        print("Cancelando operação...")
        return

    try:
        banco.manipular('''
            DELETE FROM funcionarios
            WHERE cod_funcionario = %s;
        ''', (funcionario[0],))
        print("Funcionário removido com sucesso!")
    except Exception as error:
        print("Não foi possível remover o funcionário!")


def verSetores():
    print("LISTA DE SETORES")

    setores = banco.consultar("SELECT * FROM setores ORDER BY cod_setor;")

    print("Código | Nome")

    if (len(setores) == 0):
        print("NÃO HÁ SETORES CADASTRADOS")
        return

    for cod_setor, nome_setor in setores:
        print(f"{cod_setor} | {nome_setor}")


def escolherSetor():
    verSetores()

    id_setor = int(input("DIGITE O CÓDIGO DO SETOR DESEJADO: "))

    consulta = banco.consultar('''
        SELECT cod_setor, nome_setor FROM setores
        WHERE cod_setor = %s;
    ''', (id_setor,))

    if (len(consulta) == 0):
        print("SETOR NÃO ENCONTRADO")
        return None

    setor = consulta[0]

    funcionarios = banco.consultar('''
        SELECT cod_funcionario, nome_funcionario, cargo_funcionario FROM funcionarios
        WHERE cod_setor = %s;
    ''', (id_setor,))

    print(f"FUNCIONÁRIOS DO SETOR {setor[0]} - {setor[1]}:")

    if (len(funcionarios) == 0):
        print("(nenhum funcionário)")

    for func in funcionarios:
        print(f"{func[0]} - {func[1]} - {func[2]}")

    return setor


def cadastrarSetor():
    print("CADASTRO DE NOVO SETOR")

    nome = input("Digite o nome do setor: ").strip()

    if (len(nome) <= 0):
        print("Insira um nome válido!")
        return

    try:
        banco.manipular('''
            INSERT INTO setores
            VALUES (default, %s);
        ''', (nome,))
        print("SETOR CADASTRADO!")
    except Exception as error:
        print("Não foi possível cadastrar o setor!")


def alterarSetor():
    print("ATUALIZAÇÃO DE SETOR")

    setor = escolherSetor()

    if (not setor):
        print("Setor inválido!")
        return

    cod_setor, nome_setor = setor

    novo_nome = input(f"Digite o novo nome do setor ({nome_setor}): ").strip()

    if (novo_nome):
        nome_setor = novo_nome

    try:
        banco.manipular('''
            UPDATE setores
            SET nome_setor = %s
            WHERE cod_setor = %s;
        ''', (nome_setor, cod_setor))
        print("SETOR ATUALIZADO!")
    except Exception as error:
        print("Não foi possível atualizar o setor!")


while (True):
    print('''
    BEM VINDO AO SISTEMA RH XYZ

    MENU:

    1. Ver Funcionários
    2. Escolher Funcionário
    3. Cadastrar Funcionário
    4. Alterar Funcionário
    5. Remover Funcionário

    11. Ver Setores
    12. Escolher Setor
    13. Cadastrar Setor
    14. Alterar Setor

    0. Sair
    ''')

    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA: ")

    if (op == "1"):
        verFuncionarios()
    elif (op == "2"):
        escolherFuncionario()
    elif (op == "3"):
        cadastrarFuncionario()
    elif (op == "4"):
        alterarFuncionario()
    elif (op == "5"):
        removerFuncionario()
    elif (op == "11"):
        verSetores()
    elif (op == "12"):
        escolherSetor()
    elif (op == "13"):
        cadastrarSetor()
    elif (op == "14"):
        alterarSetor()
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")

    input("TECLE ENTER PARA CONTINUAR")
