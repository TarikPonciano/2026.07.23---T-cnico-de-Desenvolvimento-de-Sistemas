# 1. Criar um arquivo sistema_rh.py

# 2. Criar uma aplicação com menu no terminal que possua as opções:

#     1 - Ver Funcionarios
#     2 - Ver Departamentos
#     0 - Sair

while True:
    print("""
    SEJA BEM VINDO AO SISTEMA RH
    
    MENU:
    
    1 - Ver Funcionários
    2 - Ver Departamentos
    
    0 - Sair      
    
          """)
    
    op = input("Digite a opção desejada: ")
    
    if (op == "1"):
        print("VER FUNCIONÁRIOS")
    elif (op == "2"):
        print("VER DEPARTAMENTOS")
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Escolha uma opção válida...")
    
    input("TECLE ENTER PARA CONTINUAR")