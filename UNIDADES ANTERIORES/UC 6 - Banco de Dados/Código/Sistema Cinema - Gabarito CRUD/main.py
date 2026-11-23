# Capítulo 5 · Gabarito da Prática 3 · main.py · CRUD do cinema com a classe Banco
#
# 1. Implementar o classBanco.py (o .env desta pasta tem DB_NAME=cinema)
# 2. Implementar o menu principal da aplicação CRUD e o objeto Banco
# 3. Criar a função verFilmes e testar ela através do menu
# 4. Criar a função escolherFilme, que pede o código de um filme a partir da lista de todos
#    os filmes e exibe os detalhes do filme. Desafio: mostre as sessões daquele filme
# 5. Completar o CRUD: cadastrarFilme, alterarFilme e removerFilme

from classBanco import Banco

banco = Banco()


def verFilmes():
    print("LISTA DE FILMES")

    filmes = banco.consultar('''
        SELECT cod_filme, titulo_filme, duracao_filme, classificacao_filme
        FROM filmes
        ORDER BY cod_filme;
    ''')

    if (len(filmes) == 0):
        print("NÃO HÁ FILMES CADASTRADOS")
        return

    print("Código | Título | Duração | Classificação")
    for cod, titulo, duracao, classificacao in filmes:
        print(f"{cod} | {titulo} | {duracao} min | {classificacao}")


def escolherFilme():
    verFilmes()

    cod_escolhido = int(input("Digite o código do filme desejado: "))

    consulta = banco.consultar('''
        SELECT cod_filme, titulo_filme, duracao_filme, classificacao_filme
        FROM filmes
        WHERE cod_filme = %s;
    ''', (cod_escolhido,))

    if (len(consulta) == 0):
        print("Filme não encontrado!")
        return None

    filme = consulta[0]

    print(f'''
    Ficha do Filme:

    Código: {filme[0]}
    Título: {filme[1]}
    Duração: {filme[2]} minutos
    Classificação: {filme[3]}
    ''')

    # Desafio: as sessões do filme
    sessoes = banco.consultar('''
        SELECT data_sessao, horario_sessao, sala_sessao
        FROM sessoes
        WHERE cod_filme = %s
        ORDER BY data_sessao, horario_sessao;
    ''', (filme[0],))

    print("SESSÕES:")
    if (len(sessoes) == 0):
        print("(nenhuma sessão)")
    for data, horario, sala in sessoes:
        print(f"{data:%d/%m/%Y} às {horario:%H:%M} - sala {sala}")

    return filme


def cadastrarFilme():
    print("CADASTRO DE NOVO FILME")

    titulo = input("Digite o título do filme: ")
    duracao = int(input("Digite a duração (minutos): "))
    classificacao = input("Digite a classificação (L, 10, 12, 14, 16 ou 18): ")

    try:
        banco.manipular('''
            INSERT INTO filmes
            VALUES (default, %s, %s, %s);
        ''', (titulo, duracao, classificacao))
        print("FILME CADASTRADO COM SUCESSO!")
    except Exception as error:
        print("ERRO AO CADASTRAR FILME")


def alterarFilme():
    print("ATUALIZAÇÃO DE FILME")

    filme = escolherFilme()

    if (not filme):
        print("Não é possível alterar o filme. Cheque o código escolhido...")
        return

    continuar = input("Deseja alterar as informações do filme? (S/N) ")

    if (continuar != "S"):
        return

    cod, titulo, duracao, classificacao = filme

    print("ALTERAR DADOS:")
    print("(Deixe vazio para manter o original)")

    novo_titulo = input(f"Digite o novo título ({titulo}): ").strip()
    if (novo_titulo):
        titulo = novo_titulo

    nova_duracao = input(f"Digite a nova duração ({duracao}): ").strip()
    if (nova_duracao):
        duracao = int(nova_duracao)

    nova_classificacao = input(f"Digite a nova classificação ({classificacao}): ").strip()
    if (nova_classificacao):
        classificacao = nova_classificacao

    try:
        banco.manipular('''
            UPDATE filmes
            SET titulo_filme = %s,
                duracao_filme = %s,
                classificacao_filme = %s
            WHERE cod_filme = %s;
        ''', (titulo, duracao, classificacao, cod))
        print("FILME ATUALIZADO!")
    except Exception as error:
        print("Ocorreu um erro na atualização!")


def removerFilme():
    print("REMOÇÃO DE FILME")

    filme = escolherFilme()

    if (not filme):
        print("Filme não encontrado!")
        return

    continuar = input("DESEJA REALMENTE APAGAR ESSE FILME? (S/N) ")

    if (continuar != "S"):
        print("Cancelando operação...")
        return

    try:
        banco.manipular('''
            DELETE FROM filmes
            WHERE cod_filme = %s;
        ''', (filme[0],))
        print("Filme removido com sucesso!")
    except Exception as error:
        # Filme com sessão não sai: a FK fk_sessao_filme recusa
        print("Não foi possível remover o filme! Ele tem sessões?")


def verSessoes():
    print("LISTA DE SESSÕES")

    sessoes = banco.consultar('''
        SELECT s.cod_sessao, f.titulo_filme, s.data_sessao, s.horario_sessao, s.sala_sessao
        FROM sessoes s
        JOIN filmes f ON f.cod_filme = s.cod_filme
        ORDER BY s.data_sessao, s.horario_sessao;
    ''')

    print("Código | Filme | Data | Horário | Sala")
    for cod, titulo, data, horario, sala in sessoes:
        print(f"{cod} | {titulo} | {data:%d/%m/%Y} | {horario:%H:%M} | {sala}")


while (True):
    print('''
    CINEMA ESTRELA

    MENU:

    1. Ver Filmes
    2. Escolher Filme
    3. Cadastrar Filme
    4. Alterar Filme
    5. Remover Filme

    11. Ver Sessões

    0. Sair
    ''')

    op = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA: ")

    if (op == "1"):
        verFilmes()
    elif (op == "2"):
        escolherFilme()
    elif (op == "3"):
        cadastrarFilme()
    elif (op == "4"):
        alterarFilme()
    elif (op == "5"):
        removerFilme()
    elif (op == "11"):
        verSessoes()
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")

    input("TECLE ENTER PARA CONTINUAR")
