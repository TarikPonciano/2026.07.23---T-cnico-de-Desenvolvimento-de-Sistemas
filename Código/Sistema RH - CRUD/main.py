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
    
    if (len(funcionarios) == 0):
        print("NÃO HÁ FUNCIONÁRIOS CADASTRADOS")

    # Alternativa -> for func in funcionarios:
    print(f"Código | Nome | CPF | CARGO | SALARIO | Cod Setor | Setor")
    for cod_func, nome_func, cpf_func, cargo_func, salario_func, cod_setor, nome_setor in funcionarios:
        print(f'''{cod_func} | {nome_func} | {cpf_func} | {cargo_func} | R$ {salario_func:,.2f} | {cod_setor} | {nome_setor}''')
        
        
        
    
    
while (True):
    print('''
          BEM VINDO AO SISTEMA RH XYZ
          
          MENU:
          
          1. Ver Funcionários
          
          
          0. Sair
          ''')
    
    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA:")
    
    if (op == "1"):
        verFuncionarios()
    elif (op == "0"):
        print("Saindo do programa...")
        
        break
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
    
    input("TECLE ENTER PARA CONTINUAR")
