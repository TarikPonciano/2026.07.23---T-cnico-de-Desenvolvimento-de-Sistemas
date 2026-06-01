def escolher_filme():
    while True:
        print("""Acessar:
    1. Filme já assistido
    2. Filme não assitido""")
        escolha = input("Digite o que você deseja acessar: ")
        if escolha == "1" or escolha == "2":
            return escolha
        else:
            print("Número inválido, digite novamente.")

def ver_filmes_assistidos(lista):
    print("""
        🎥 Filmes Assistidos 🎥
""")
    for i, filme in enumerate(lista):
        print(f"""{i+1}. {filme["nome"].title()} | {filme["gênero"].title()}
    Ano de lançamento: {filme["ano"]} | Faixa Etária: {filme["faixa etária"]}
    Nota: {filme["nota"]:.2f} | Comentário: {filme["comentário"].title()}
""")

def ver_filmes_nao_assistidos(lista):
    print("""
        🎥 Filmes Não Assistidos 🎥
""")
    for i, filme in enumerate(lista):
        print(f"""{i+1}. {filme["nome"].title()} | {filme["gênero"].title()}
    Ano de lançamento: {filme["ano"]} | Faixa Etária: {filme["faixa etária"]}
""")

def escolha_de_menu():
    while True:
        escolha = input("""
O que deseja fazer agora?
        1. Continuar.
        2. Voltar para o menu inicial.
    --> """)
        if escolha == "1" or escolha == "2":
            return escolha
        else:
            print("Opção inválida, digite novamento.")

# ----------------------------------------------------------------------------

# def verificar_texto(variavel):
#     if variavel == "":
#         print("Preencha o campo acima.")
#         return False
#     else:
#         return True
    
# def verificar_num(variavel):
#     if variavel == "":
#         print("Preencha o campo acima.")
#         return False
#     try:
#         float(variavel)  # testa se consegue virar número
#         return True
#     except ValueError:
#         print("Digite apenas números.")
#         return False

# ----------------------------------------------------------------------------
    
def coletar_nome():
    while True:
        nome = input("Digite o nome do filme: ")
        if nome == "":
            print("Preencha o campo Nome.")
        else:
            nome = nome.upper
            return nome

def coletar_genero():
    while True:
        genero = input("Digite o gênero do filme: ")
        if genero == "":
            print("Preencha o campo Gênero.")
        else:
            genero = genero.upper
            return genero
    
def coletar_ano():
    while True:
        ano = input("Digite o ano de lançamento do filme: ")
        if ano == "":
            print("Preencha o campo Ano de Lançamento.")
        elif not ano.isdigit():
            print("Digite apenas números.")
        else:
            ano = int(ano)
            if ano <= 1800 or ano >= 2026:
                print("Digite um ano válido.")
            else:
                return ano
    
def coletar_faixa_etaria():
    while True:
        faixa = input("Digite a faixa étaria do filme (L, +10, +12, +16, +18): ")
        if faixa == "":
            print("Preencha o campo Faixa Etária.")
        elif faixa.upper() not in ["L", "+10", "+12", "+16", "+18"]:
            print("Digite uma classificação válida --> L, +10, +12, +16, +18.")
        else:
            return faixa
    
# def coletar_nota():
#     while True:
#         nota = input("Digite uma nota de 0 a 5: ")
#         if nota == "":
#             print("Preencha o campo Nota.")
#         elif not nota.isdecimal():
#             print("Digite apenas números.")
#         else:
#             nota = float(nota)
#             if nota < 0 or nota > 5:
#                 print("Digite apenas uma nota entre 0 e 5.")
#             else:
#                 return nota
            
def coletar_nota():
    while True:
        nota = input("Digite uma nota de 0 a 5: ")
        if nota == "":
            print("Preencha o campo Nota.")
        else:
            try:
                nota = float(nota)
                if nota < 0 or nota > 5:
                    print("Digite apenas uma nota entre 0 e 5.")
                else:
                    return nota
            except ValueError:
                print("Digite apenas números válidos (use ponto para decimais).")
    
def coletar_comentario():
    while True:
        comentario = input("Digite seu comentário: ")
        if comentario == "":
            print("Preencha o campo Comentário.")
        else:
            comentario = comentario.upper
            return comentario
    
# ----------------------------------------------------------------------------

def indice_filme(lista):
    while True:
        escolha = input("Digite o número do filme que deseja editar: ")
        if escolha == "":
            print("Preencha o campo.")
        elif not escolha.isdigit():
            print("Digite apenas números.")
        else:
            escolha = int(escolha)
            if escolha < 0 or escolha > len(lista):
                print("Número inválido, digite novamente.")
            else:
                indice = (escolha-1)
                return indice
        
def edicao():
    while True:
        print("""Edição:
    1. Nota
    2. Comentário""")
        escolha = int(input("Digite a opção que deseja: "))
        if escolha not in [1, 2]:
            print("Opção inválida, digite novamente.")
        else:
            return escolha