import json
def carregar_dados():
    dados = None

    with open("dados.json", "r",encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

def salvar_dados(livros):
    with open("dados.json", "w",encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4)



def validar_titulo(titulo_livro):
    
    if len(titulo_livro) < 3:
        print("O título precisa ser maior que 3 caracteres!")
        return False
    
    else:
        return True
    
def coletar_numlivro(livros):
    while True:
        num_livro = input("Digite o número do livro: ")
        if num_livro == "":
            print("Campo não pode ficar vazio!")
            continue
        elif not num_livro.isdigit():
            print("Insira somente dígitos!")
            continue

        else:
            num_livro = int(num_livro)
            if num_livro < 1 or num_livro > len(livros):
                print("Número selecionado excedeu quantidade registrada na lista!")
                continue
            
            else:
                return num_livro


def visualizar_titulos(livros):
    
    print("Livros disponíveis:")

    contador = 1
    for livro in livros:
        print(f"{contador}. {livro['Título']} de {livro['Autor']}")
        contador += 1

def cadastrar_livro(livros):
        
    while True:

        titulo_novo = input("Digite o título: ")
            
        if titulo_novo == "":
            print("Preencha o campo 'título'.")
            
        elif validar_titulo(titulo_novo):
            break

    while True:

        autor_novo = input("Digite o nome do autor: ")

        if autor_novo == "":
            print("Preencha o campo 'nome do autor'.")

        else:
            break
        
    while True:

        editora_novo = input("Digite a editora do livro: ")

        if editora_novo == "":
            print("Preencha o campo 'editora'.")

        else:
            break
        
    while True:

        ano_novo = input("Digite o ano de publicação: ")

        if len(ano_novo) != 4:
            print("Digite um ano válido!")

        elif not ano_novo.isdigit():
            print("Digite apenas números!")

        else:
            break

    while True:

        sinopse_novo = input("Digite a sinopse do livro: ")

        if sinopse_novo == "":
            print("Preencha o campo 'sinopse'.")

        else:
            break


    novo_livro = {
            "Título": titulo_novo,
            "Autor" : autor_novo,
            "Editora" : editora_novo,
            "Ano": ano_novo,
            "Sinopse": sinopse_novo
        }
    
    livros.append(novo_livro)

def modificar_livro (livros):
    
    while True:

        visualizar_titulos(livros)

        num_livro = coletar_numlivro(livros)
            
        num_escolhido = livros[num_livro - 1]

        print(f"""
            
        📖 Livro N° {num_livro} selecionado
            
            Título: {num_escolhido["Título"]}
            Autor: {num_escolhido["Autor"]}
            Editora: {num_escolhido["Editora"]}
            Ano: {num_escolhido["Ano"]}
            Sinopse:{num_escolhido["Sinopse"]}

            """)

        print("Modifique as informações desejadas. Para manter algum dado sem modificação, pressione ENTER para pular para o próximo campo.")

        novo_titulo = input(f"Digite o novo título para {num_escolhido['Título']}: ")
        if novo_titulo:
            num_escolhido["Título"] = novo_titulo

        novo_autor = input(f"Digite o novo autor para {num_escolhido['Autor']}: ")
        if novo_autor:
            num_escolhido["Autor"] = novo_autor

        novo_editora = input(f"Digite a nova editora para {num_escolhido['Editora']}: ")
        if novo_editora:
            num_escolhido["Editora"] = novo_editora

        novo_ano = input(f"Digite o novo ano para {num_escolhido['Ano']}: ")
        if novo_ano :
            if novo_ano .isdigit() and len(novo_ano)== 4:

                num_escolhido["Ano"] = novo_ano
            else:
                print("Ano ignorado. Digite uma data de 4 dígitos.")


        novo_sinopse = input(f"Digite a nova sinopse para {num_escolhido['Sinopse']}: ")
        if novo_sinopse:
            num_escolhido["Sinopse"] = novo_sinopse


        print(f"""
            
            Informações do Livro Atualizadas
            
            Título: {num_escolhido['Título']}
            Autor: {num_escolhido['Autor']}
            Editora: {num_escolhido['Editora']}
            Ano: {num_escolhido['Ano']}
            Sinopse: {num_escolhido['Sinopse']}

            """)
        continuar = input("Deseja modfificar outro livro? (s/n): ")
        if continuar.lower() != "s":
            break
    
def remover_livro(livros):

    while True:

        visualizar_titulos(livros)

        num_livro = coletar_numlivro(livros)
        
        livro_removido = livros.pop(num_livro-1)

        print(f"O livro {livro_removido['Título']} do autor {livro_removido['Autor']} foi removido com sucesso!")

def ler_sinopses(livros):

    while True:
        
        visualizar_titulos(livros)

        num_livro = coletar_numlivro(livros)

        livro_escolhido = livros[num_livro-1]

        print(f"""

            Livro {num_livro} selecionado 📙
            
            Título: {livro_escolhido['Título']}

            Sinopse: {livro_escolhido['Sinopse']}

            """)
        break
        
def buscar_autor(livros):
    autor_escolhido = input("Busca por autor: ")
    contador = 1
    print(f"LIVROS DE {autor_escolhido} 📙")
    for livro in livros:
        
        if livro['Autor'].upper() == autor_escolhido.upper():
            
            print(f"{contador}. {livro['Título']} de {autor_escolhido}")
            contador += 1
    if contador == 1:
        print("Desculpe! Nenhum livro encontrado. Tente novamente.")

    
