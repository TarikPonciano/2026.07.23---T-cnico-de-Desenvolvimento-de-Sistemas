import utils

filmes_assistidos = [
    {"nome": "CIDADE DE DEUS", "gênero": "CRIME", "ano": 2002, "faixa etária": "+16", "nota": 5, "comentário": "OBRA-PRIMA DO CINEMA NACIONAL."},
    {"nome": "FORREST GUMP", "gênero": "DRAMA", "ano": 1994, "faixa etária": "+14", "nota": 5, "comentário": "HISTÓRIA EMOCIONANTE E INSPIRADORA."},
    {"nome": "A VIAGEM DE CHIHIRO", "gênero": "ANIMAÇÃO", "ano": 2001, "faixa etária": "LIVRE", "nota": 4, "comentário": "ANIMAÇÃO LINDA E COALHADA DE MAGIA."},
    {"nome": "WHIPLASH", "gênero": "DRAMA", "ano": 2014, "faixa etária": "+12", "nota": 5, "comentário": "RITMO INTENSO E ATUAÇÕES INCRÍVEIS."}
]

filmes_nao_assistidos = [
    {"nome": "O CAVALEIRO DAS TREVAS", "gênero": "AÇÃO", "ano": 2008, "faixa etária": "+12"},
    {"nome": "A ORIGEM", "gênero": "FICÇÃO CIENTÍFICA", "ano": 2010, "faixa etária": "+14"},
    {"nome": "INTERESTELAR", "gênero": "FICÇÃO CIENTÍFICA", "ano": 2014, "faixa etária": "+10"},
    {"nome": "PARASITA", "gênero": "DRAMA", "ano": 2019, "faixa etária": "+16"},
    {"nome": "MATRIX", "gênero": "AÇÃO", "ano": 1999, "faixa etária": "+12"},
    {"nome": "CLUBE DA LUTA", "gênero": "DRAMA", "ano": 1999, "faixa etária": "+18"},
    {"nome": "PULP FICTION", "gênero": "CRIME", "ano": 1994, "faixa etária": "+18"},
    {"nome": "O SENHOR DOS ANÉIS: A SOCIEDADE DO ANEL", "gênero": "FANTASIA", "ano": 2001, "faixa etária": "+12"},
    {"nome": "O REI LEÃO", "gênero": "ANIMAÇÃO", "ano": 1994, "faixa etária": "LIVRE"},
    {"nome": "GLADIADOR", "gênero": "AÇÃO", "ano": 2000, "faixa etária": "+14"},
    {"nome": "VINGADORES: ULTIMATO", "gênero": "AÇÃO", "ano": 2019, "faixa etária": "+12"},
    {"nome": "CORINGA", "gênero": "DRAMA", "ano": 2019, "faixa etária": "+16"},
    {"nome": "VIVA: A VIDA É UMA FESTA", "gênero": "ANIMAÇÃO", "ano": 2017, "faixa etária": "LIVRE"},
    {"nome": "O RESGATE DO SOLDADO RYAN", "gênero": "GUERRA", "ano": 1998, "faixa etária": "+16"},
    {"nome": "BONS COMPANHEIROS", "gênero": "CRIME", "ano": 1990, "faixa etária": "+16"}
]

print(f"🎟️ Bem vindo ao seu Letterboxd pessoal para filmes 🎟️")
while True:
    print("""
        🎞️ Menu 🎞️
    1. Adicionar novo filme.
        - Filme já assistido
        - Filme ainda não assisito

    2. Ver minha lista de filmes.
        - Filme já assistido
        - Filme ainda não assisito

    3. Editar filmes.
        - Filme já assistido
            -- Editar atribuições: nota ou comentário
          
    4. Remover filmes.
        - Filme já assistido
        - Filme ainda não assisito
          
    0. Sair do Letterboxd.
""")
    op = input("--> ")
    if op == "1":
        while True:
            print(f"{"="*6}🎫 Acionar Novo Filme 🎫{"="*6}")

            op = utils.escolher_filme()
            print()

            if op == "1": # adicionar um filme assistido
                print("--- Acionar novo filme ❕já asistido❕ ---")
                
                nome = utils.coletar_nome()
                genero = utils.coletar_genero()
                ano = utils.coletar_ano()
                faixa = utils.coletar_faixa_etaria()
                nota = utils.coletar_nota()
                comentario = utils.coletar_comentario()

                novo_filme = {
                    "nome": nome,
                    "gênero": genero,
                    "ano": ano,
                    "faixa etária": faixa,
                    "nota": nota,
                    "comentário": comentario
                }

                filmes_assistidos.append(novo_filme)
                print()
                print("Filme adicionado com sucesso na sua lista!")

            elif op == "2": # adicionar um filme não assistido
                print("--- Acionar novo filme ❕não asistido❕ ---")

                nome = utils.coletar_nome()
                genero = utils.coletar_genero()
                ano = utils.coletar_ano()
                faixa = utils.coletar_faixa_etaria()

                novo_filme = {
                    "nome": nome,
                    "gênero": genero,
                    "ano": ano,
                    "faixa etária": faixa
                }

                filmes_nao_assistidos.append(novo_filme)
                print()
                print("Filme adicionado com sucesso na sua lista!")

            menu = utils.escolha_de_menu()
            if menu == "1":
                continue
            else:
                break

    elif op == "2":
        while True:
            print(f"{"="*6}🎫 Ver Lista de Filmes 🎫{"="*6}")

            op = utils.escolher_filme()
            print()

            if op == "1":
                utils.ver_filmes_assistidos(filmes_assistidos)
            elif op == "2":
                utils.ver_filmes_nao_assistidos(filmes_nao_assistidos)

            menu = utils.escolha_de_menu()
            if menu == "1":
                continue
            else:
                break

    elif op == "3":
        while True:
            print(f"{"="*6}🎫 Editar Filme 🎫{"="*6}")

            utils.ver_filmes_assistidos(filmes_assistidos)

            indice = utils.indice_filme(filmes_assistidos)

            filme_escolhido = filmes_assistidos[indice]

            print(f"""Filme escolhido:
        {filme_escolhido["nome"]}
        Gênro: {filme_escolhido["gênero"]}
        Ano de lançamento: {filme_escolhido["ano"]}
        Faixa Etária: {filme_escolhido["faixa etária"]}
        Nota: {filme_escolhido["nota"]}
        Comentário: {filme_escolhido["comentário"]}
    """)
            escolha = utils.edicao()
            if escolha == 1:
                print("--> Editar nota do filme")
                nova_nota = utils.coletar_nota()
                print("Nota altera com sucesso!")

                filme_escolhido["nota"] = nova_nota

            elif escolha == 2:
                print("--> Editar comentário do filme")
                novo_comentario = utils.coletar_comentario()
                print("Comentário alterado com sucesso.")

                filme_escolhido["comentário"] = novo_comentario

            menu = utils.escolha_de_menu()
            if menu == "1":
                continue
            else:
                break

    elif op == "4":
        while True:
            print(f"{"="*6}🎫 Remover Filme 🎫{"="*6}")

            op = utils.escolher_filme()

            if op == "1":
                utils.ver_filmes_assistidos(filmes_assistidos)

                indice = utils.indice_filme(filmes_assistidos)

                filme_escolhido = filmes_assistidos[indice]

                print(f"""Filme escolhido:
    {filme_escolhido["nome"]}
    Gênro: {filme_escolhido["gênero"]}
    Ano de lançamento: {filme_escolhido["ano"]}
    Faixa Etária: {filme_escolhido["faixa etária"]}
    Nota: {filme_escolhido["nota"]}
    Comentário: {filme_escolhido["comentário"]}
""")
                escolha = input("Deseja remover esse filme (S/N): ")
                escolha = escolha.upper()
                if escolha == "S":
                    filmes_assistidos.pop(indice)
                    print("Filme removido com sucesso!")
                elif escolha == "N":
                    continue

            elif op == "2":
                utils.ver_filmes_nao_assistidos(filmes_nao_assistidos)

                indice = utils.indice_filme(filmes_assistidos)

                filme_escolhido = filmes_assistidos[indice]

                print(f"""Filme escolhido:
    {filme_escolhido["nome"]}
    Gênro: {filme_escolhido["gênero"]}
    Ano de lançamento: {filme_escolhido["ano"]}
    Faixa Etária: {filme_escolhido["faixa etária"]}
    Nota: {filme_escolhido["nota"]}
    Comentário: {filme_escolhido["comentário"]}
""")
                escolha = input("Deseja remover esse filme (S/N): ")
                escolha = escolha.upper()
                if escolha == "S":
                    filmes_nao_assistidos.pop(indice)
                    print("Filme removido com sucesso!")
                elif escolha == "N":
                    continue

            menu = utils.escolha_de_menu()
            if menu == "1":
                continue
            else:
                break

    elif op == "0":
        input("Encerrando o Letterboxd... 😭😭😭")
        break

    else:
        print("Opção inválida, digite novamente!")

print()
input("Programa encerrado.")