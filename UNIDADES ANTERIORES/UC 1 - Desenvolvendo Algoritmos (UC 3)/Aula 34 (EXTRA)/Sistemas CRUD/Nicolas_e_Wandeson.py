import datetime
alunos = [
    {
        "Nome": "Wandersson",
        "Data de nascimento": "17/05/1988",
        "Genero": "M",
        "Avaliação 1": 8,
        "Avaliação 2": 9
    },

    {
        "Nome": "Nicolas",
        "Data de nascimento": "04/12/2009",
        "Genero": "M",
        "Avaliação 1": 5,
        "Avaliação 2": 10
    },

    {
        "Nome": "Tais",
        "Data de nascimento": "12/08/2008",
        "Genero": "F",
        "Avaliação 1": 9,
        "Avaliação 2": 8
    },

    {
        "Nome": "João Vitor",
        "Data de nascimento": "23/03/2009",
        "Genero": "M",
        "Avaliação 1": 7,
        "Avaliação 2": 8
    },

    {
        "Nome": "Pedro",
        "Data de nascimento": "15/11/2008",
        "Genero": "M",
        "Avaliação 1": 6,
        "Avaliação 2": 9
    },

    {
        "Nome": "Jorge",
        "Data de nascimento": "30/01/2007",
        "Genero": "M",
        "Avaliação 1": 8,
        "Avaliação 2": 7
    },

    {
        "Nome": "Ryan",
        "Data de nascimento": "18/06/2009",
        "Genero": "M",
        "Avaliação 1": 10,
        "Avaliação 2": 9
    },

    {
        "Nome": "Lay",
        "Data de nascimento": "09/09/2008",
        "Genero": "F",
        "Avaliação 1": 7,
        "Avaliação 2": 10
    },

    {
        "Nome": "Stefano",
        "Data de nascimento": "27/02/2007",
        "Genero": "M",
        "Avaliação 1": 8,
        "Avaliação 2": 8
    },

    {
        "Nome": "Aline",
        "Data de nascimento": "14/04/2009",
        "Genero": "F",
        "Avaliação 1": 9,
        "Avaliação 2": 10
    },

    {
        "Nome": "Denzel",
        "Data de nascimento": "05/12/2008",
        "Genero": "M",
        "Avaliação 1": 6,
        "Avaliação 2": 7
    }

 

         
]

def cadastrar_aluno():
    while True:
        nome_aluno = input("Digite o nome do aluno: ")
        if nome_aluno == "":
            print("Preencha o campo nome: ")
        else:
            break
    while True:
        data_nascimento = (input("Digite a data de nascimento do aluno (dia/mês/ano): "))
        if data_nascimento == "":
            print("Preencha o campo data de nascimento: ")
        else:
            break
    while True:
        genero_aluno = input("Digite o sexo do aluno (M - Masculino. F - Feminino): ").strip().upper()
        if genero_aluno != "M" and genero_aluno != "F":
            print("Digite o sexo conforme o padrão pedido: ")
            
        elif genero_aluno == "":
            print("Preencha o campo sexo: ")
        else:
            break
    while True:
        avaliacao1 = float(input("Digite a nota da primeira avaliação do aluno: "))
        if avaliacao1 == "":
            print("Preencha o campo avaliação do aluno: ")
        else:
            break
    while True:

        avaliacao2 = float(input("Digite a nota da segunda avaliação do aluno: "))
        if avaliacao2 == "":
            print("Preencha o campo de segunda avaliação: ")
        else:
            break

    novo_aluno = {
        "Nome": nome_aluno,
        "Data de nascimento": data_nascimento,
        "Genero": genero_aluno,
        "Avaliação 1": avaliacao1,
        "Avaliação 2": avaliacao2
    }

    alunos.append(novo_aluno)

def ver_aluno():
    contador = 1
    for aluno in alunos:
        print(f"{contador} - {aluno["Nome"]} - {aluno["Data de nascimento"]} - Gênero:{aluno["Genero"]} - Primeira Nota:{aluno["Avaliação 1"]} - Segunda nota: {aluno["Avaliação 2"]} ")
        contador += 1


def escolher_aluno():
    while True:
        try:
            num_aluno = int(input("Digite o número do aluno desejado: "))
            if num_aluno < 1 or num_aluno > len(alunos):
                print("Digite um número válido.")
                continue
            else:
                print("Aluno encontrado.")
                return num_aluno
        except ValueError:
            print("Digite apenas números: ")


def alterar_aluno():
    ver_aluno()

    num_aluno = escolher_aluno()
    
    aluno_escolhido = alunos[num_aluno-1]

    print(f"""
INFORMAÇÕES DO ALUNO:
          Nome: {aluno_escolhido["Nome"]}
          Data de Nascimento: {aluno_escolhido["Data de nascimento"]}
          Gênero: {aluno_escolhido["Genero"]}
          Avaliação 1: {aluno_escolhido["Avaliação 1"]}
          Avaliação 2: {aluno_escolhido["Avaliação 2"]}  """)

    print("ALTERAR AS INFORMAÇÕES DO ALUNO")

    novo_aluno = input("Digite o nome do novo aluno: ")
    if novo_aluno:
        aluno_escolhido["Nome"] = novo_aluno
    nova_data = input("Digite a nova data de nascimento do aluno: ")
    if nova_data:
        aluno_escolhido["Data de nascimento"] = nova_data
    novo_genero = input("Digite o novo gênero do aluno: ")
    if novo_genero:
        aluno_escolhido["Genero"] = novo_genero
    nova_nota1 = float(input("Digite a nova primeira nota do aluno: "))
    if nova_nota1:
        aluno_escolhido["Avaliação 1"] = nova_nota1
    nova_nota2 = float(input("Digite a nova segunda nota do aluno: "))
    if nova_nota2:
        aluno_escolhido["Avaçiação 2"] = nova_nota2

def remover_aluno():
    ver_aluno()

    num_aluno = escolher_aluno()

    aluno_removido = alunos.pop(num_aluno-1)

    print(f"{aluno_removido["Nome"]} foi apagado do sistema escolar.")


def calcular_media():
    ver_aluno()

    num_aluno = escolher_aluno()

    aluno_escolhido = alunos[num_aluno-1]

    media_escolhida = (aluno_escolhido["Avaliação 1"] + aluno_escolhido["Avaliação 2"]) / 2

    print(f"""
MÉDIA DO ALUNO:
          Nome: {aluno_escolhido["Nome"]}
          Nota 1: {aluno_escolhido["Avaliação 1"]}
          Nota 2: {aluno_escolhido["Avaliação 2"]}
          Média: {media_escolhida}    """)
    

    
def calculadora_idade():
    ver_aluno()
    
    num_aluno = escolher_aluno()

    aluno_escolhido = alunos[num_aluno-1]

    data_aluno = aluno_escolhido["Data de nascimento"].split("/")

    mes_atual = datetime.date.today().month

    dia_atual = datetime.date.today().day

    ano_atual = datetime.date.today().year

    if  mes_atual >= int(data_aluno[1]) and dia_atual >= int(data_aluno[0]):
        idade1 = ano_atual - int(data_aluno[2])
        print(f"Você tem {idade1} anos. Parabens você já fez aniversário! ")

    else:
        idade2 = ano_atual - int(data_aluno[2]) - 1
        print(f"Você tem {idade2} anos. Sem bolo, você não fez aniversário.")







while True:
    print("""
BEM VINDO AO CADASTRO DE ALUNOS DA ESCOLA: TARIK PROGRAMAÇÕES:
        1. CADASTRAR UM NOVO ALUNO.
        2. VER ALUNOS CADASTRADOS.
        3. ALTERAR ALUNO CADASTRADO.
        4. REMOVER UM ALUNO.
        5. VER MÉDIA DO ALUNO.
        6. VER IDADE DO ALUNO.
        0. SAIR.  """)
    op = input("Digite a opção desejada: ")

    if op == "1":
        cadastrar_aluno()
    elif op == "2":
        ver_aluno()
    elif op == "3":
        alterar_aluno()
    elif op == "4":
        remover_aluno()
    elif op == "5":
        calcular_media()
    elif op == "6":
        calculadora_idade()
    elif op == "0":
        print("Encerrando programa...")
        break
    else:
        print("Digite a opção novamente. ")

print("TECLE ENTER PARA CONTINUAR...")