import utils, json

livros = utils.carregar_dados()
    
while True:

    print("""
          
    📚 ------ BEM-VINDO À BIBLIOTECA SLOP ------ 📚
    
                1. Ver Livros Disponíveis
                2. Cadastrar Livros
                3. Modificar Livros
                4. Remover Livros
                5. Ler Sinopses
                6. Buscar Livro por Autor
            
                0. Sair - Salvar
          
""")
    
    op = input("Digite a opção desejada: ")
    
    if op == "1":
        utils.visualizar_titulos(livros)
        
    elif op == "2":
        utils.cadastrar_livro(livros)

    elif op == "3":
        utils.modificar_livro(livros)

    elif op == "4":
        utils.remover_livro(livros)
    
    elif op == "5":
        utils.ler_sinopses(livros)
    
    elif op == "6":
        utils.buscar_autor(livros)
    
    elif op == "0":
        print("Encerrando o programa...")
        utils.salvar_dados(livros)

        break
    
    else:
        print("Digite uma opção válida!")
        

    input("DIGITE ENTER PARA CONTINUAR")

    