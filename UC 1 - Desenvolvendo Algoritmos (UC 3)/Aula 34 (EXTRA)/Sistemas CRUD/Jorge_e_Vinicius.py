# Cadastro de Livros (biblioteca)



# Biblioteca: "Buscar livro por autor" / "Listar apenas livros disponíveis"

livros = []


def livro_exist(titulo):
    for dados in livros:
        if dados["titulo"]==titulo:
            return True
    return False
    
# Coloca a primeira letra de cada palavra em maiúscula
# nome = "aaaaaaaaaaa"

# resultado = nome.title()

# print(resultado)

def cadastra_livro():
    print("CADASTRO DE LIVRO NA BIBLIOTECA")

    while True:

        titulo = input("Informe o titulo do livro: ")
        titulo = titulo.title()
        if titulo == "":
            print("Preencha o campo acima para prosseguir.")
        elif livro_exist(titulo):
            print("Livro já cadastrado.")
        
        else:
            break
    while True:
        
        autor = input("Informe o nome do autor: ")
        if autor == "":
            input("Preencha o campo acima para prosseguir: ")
        elif autor.isdigit():
            print("Formato de autor inválido.")
        else:
            break
    while True:

        tema = input("Digite o tema do livro: ")
        if tema == "":
            print("Preencha o campo acima para prosseguir: ")
        elif tema.isdigit():
            print("Formato de tema inválido.")
        else:
            break

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "tema": tema
    }

    livros.append(novo_livro)

def escolher_livro():
    ver_livro()
    while True:
        try:
            num = int(input("Digite o número do livro: "))
            if num <1 or num > len(livros):
                print("Digite um número válido.")
                return
            elif num == "":
                print("Digite um valor válido.")
            elif num == len(livros):
                contador =1
                for livro in livros:
                        if num == livro:
                            print(f"{contador}. {livro['titulo']} | {livro["autor"]} | {livro["tema"]}")
                            contador+=1
            else:
                break
        except ValueError:
            print("DIGITE APENAS NÚMEROS")

def remover_titulo():
    ver_livro()
    num_livro = escolher_livro()
    livro_removido = livros.pop(num_livro-1)
    print(f"{livro_removido["titulo"]} foi removido da sua biblioteca.")


def ver_livro():
    
    print("LIVROS CADASTRADOS")

    contador = 1
    for livro in livros:
        
        print(f"{contador}. {livro['titulo']} | {livro['autor']} | {livro['tema']}")
        contador += 1


def alterar_livro():
    ver_livro()
    num_livro = escolher_livro()
    
    livro_escolhido = livros[num_livro -1]

    print(f"""
        INFORMAÇÕES DO LIVRO:
          
Titulo: {livro_escolhido['titulo']}
Autor: {livro_escolhido['autor']}
Tema: {livro_escolhido['tema']}
""")
    
    print("Deseja alterar alguma informação desse livro?\n Pressione ENTER para não alterar.: ")
 
    novo_titulo = input(f"Digite o novo titulo do livro ({livro_escolhido['titulo']}): ")
    if novo_titulo: 
        livro_escolhido['titulo'] = novo_titulo
    novo_autor = input(f"Digite o novo nome do autor ({livro_escolhido['autor']}): ")
    if novo_autor:
        livro_escolhido['autor'] = novo_autor
    novo_tema = input(f"Digite o novo tema ({livro_escolhido['tema']}): ")
    if novo_tema:
        livro_escolhido['tema'] = novo_tema

def pesquisa_tema():
    ver_livro()
    contador = 1
    print("Digite zero para cancelar operação.")
    escolha = input("Digite o tema que deseja consultar: ")
    for livro in livros:
        if escolha == livro["tema"]:
            print(f"{contador} - {livro["titulo"]} | {livro["tema"]}")
            contador += 1

        elif escolha == "0":
            print("Encerrando programa.")

        else:
            ("DIGITE A OPÇÃO DESEJADA")
            break

def pesquisa_autor():
    ver_livro()
    contador = 1
    print("DIGITE (0) PARA CANCELAR")
    escolha = input("Digite o nome do autor: ")
    for livro in livros:
        if escolha == livro["autor"]:
            print(f"{contador}. {livro["titulo"]} | {livro["autor"]}.")
            contador += 1
        elif escolha == "0":
            print("CANCELANDO OPERAÇÃO")
        else:
            ("DIGITE A OPÇÃO DESEJADA")
            break


while True:
    print("""========= MENU DE OPÇÕES =========
          
          1. Cadastra Livro.
          2. Ver informações.
          3. Atualizar biblioteca.
          4. Remover livro.
          5. Pesquisa por temas.
          6. Pesquisar por autor.
          7. Escolher por titulo.
          0. Sair
""")



    op = input("Digite a opção desejada: ")
    if op == "1":
        cadastra_livro()
    if op == "2":
        ver_livro()

    elif op == "3":
        alterar_livro()
    
    elif op == "4":
        remover_titulo()

    elif op == "5":
        pesquisa_tema()
    elif op == "6":
        pesquisa_autor()
    
    elif op == "7":
        escolher_livro()

    elif op == "0":
        print("Saindo do programa...")
        break
    else:
        ("DIGITE A OPÇÃO DESEJADA")

    input("TECLE ENTER PARA CONTINUAR: ")