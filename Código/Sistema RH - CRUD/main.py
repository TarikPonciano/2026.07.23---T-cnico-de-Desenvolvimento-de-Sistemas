# 1. Implementar o classBanco.py
# 2. Implementar o menu principal da aplicação CRUD e o objeto Banco
# 3. Criar a função verFilmes e testar ela através do menu
# 4. Criar a função verFilmePorID, que deve pedir o ID de um filme a partir da lista de todos os filmes e exibir detalhes do filme. Desafio: Mostre as sessões daquele filme

from classBanco import Banco

banco = Banco()

def verFuncionarios():
    print("LISTA DE FUNCIONÁRIOS")
    
    funcionarios = banco.consultar('''
    SELECT f.cod_funcionario, f.nome_funcionario, f.cpf_funcionario, f.cargo_funcionario, f.salario_funcionario, f.cod_setor, s.nome_setor FROM funcionarios f
    JOIN setores s ON f.cod_setor = s.cod_setor
    ORDER BY f.cod_funcionario ASC;''')
    
    print(f"Código | Nome | CPF | CARGO | SALARIO | Cod Setor | Setor")
    
    if (len(funcionarios) == 0):
        print("NÃO HÁ FUNCIONÁRIOS CADASTRADOS")
        return

    # Alternativa -> for func in funcionarios:
    
    for cod_func, nome_func, cpf_func, cargo_func, salario_func, cod_setor, nome_setor in funcionarios:
        print(f'''{cod_func} | {nome_func} | {cpf_func} | {cargo_func} | R$ {salario_func:,.2f} | {cod_setor} | {nome_setor}''')
        
    
        
        
def escolherFuncionario():
    verFuncionarios()
    
    cod_escolhido = int(input("Digite o código do funcionário desejado:"))
    
    consulta = banco.consultar('''
        SELECT f.cod_funcionario, f.nome_funcionario, f.cpf_funcionario, f.cargo_funcionario, f.salario_funcionario, f.cod_setor, s.nome_setor FROM funcionarios f
        JOIN setores s ON f.cod_setor = s.cod_setor
        WHERE f.cod_funcionario = %s 
                                  ''', (cod_escolhido,))
    
    if (len(consulta) == 0):
        print("Funcionário não encontrado!")
        return
    
    funcionario = consulta[0]
    
    print(f'''
              Ficha do Funcionário:
              
              Código: {funcionario[0]}
              Nome: {funcionario[1]}
              CPF: {funcionario[2]}
              Cargo: {funcionario[3]}
              Salário: {funcionario[4]}
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
    
    
    continuar = input("Deseja alterar as informações funcionário? (S/N)")
    
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
        
    except Exception as error:
        print("Ocorreu um erro na atualização!")
        
    
    
    
    

def verSetores():
    print("LISTA DE SETORES")
        
    setores = banco.consultar('''
        SELECT * FROM setores''')
        
    print(f"Código | Nome")
        
    if (len(setores) == 0):
        print("NÃO HÁ SETORES CADASTRADOS")
        return
    
        # Alternativa -> for func in funcionarios:
        
    for cod_setor, nome_setor in setores:
        print(f'''{cod_setor} | {nome_setor} ''')
   
def escolherSetor():
    
    verSetores()
    
    id_setor = int(input("DIGITE O CÓDIGO DO SETOR DESEJADO:"))
    
    consulta = banco.consultar('''
    SELECT s.cod_setor, s.nome_setor, f.cod_funcionario, f.nome_funcionario, f.cargo_funcionario FROM setores s
    JOIN funcionarios f ON f.cod_setor = s.cod_setor
    WHERE s.cod_setor = %s;                                  
                               ''', (id_setor,))
    
    if (len(consulta) == 0):
        print("SETOR NÃO ENCONTRADO")
        return
    
    
    
    print(f"FUNCIONÁRIOS DO SETOR {consulta[0][0]} - {consulta[0][1]}:")
    
    for func in consulta:
        print(f"{func[2]} - {func[3]} - {func[4]}")
    
def cadastrarSetor():
    print("CADASTRO DE NOVO SETOR")
    
    nome = input("Digite o nome do setor: ").strip()
    
    if (len(nome) <= 0):
        print("Insira um nome válido!")
        return
    
    banco.manipular('''
    INSERT INTO setores
    VALUES (default, %s);                              
                    ''', (nome,))
    
    print("SETOR CADASTRADO!")
    
while (True):
    print('''
          BEM VINDO AO SISTEMA RH XYZ
          
          MENU:
          
          1. Ver Funcionários
          2. Escolher Funcionário
          3. Cadastrar Funcionário
          4. Alterar Funcionário
          
          11. Ver Setores
          12. Escolher Setor
          13. Cadastrar Setor
          
          0. Sair
          ''')
    
    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA:")
    
    if (op == "1"):
        verFuncionarios()
    elif (op == "2"):
        escolherFuncionario()
    elif (op == "3"):
        cadastrarFuncionario()
    elif (op == "4"):
        alterarFuncionario()
    elif (op == "11"):
        verSetores()
    elif (op == "12"):
        escolherSetor()
    elif (op == "13"):
        cadastrarSetor()
    elif (op == "0"):
        print("Saindo do programa...")
        
        break
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
    
    input("TECLE ENTER PARA CONTINUAR")
