from classGalpao import Galpao

def cadastrar_novo_galpao():
    print("CADASTRO DE NOVO GALPÃO")
    
    codigo = input("Digite o código do galpão:").strip()
    
    if not codigo:
        print("CÓDIGO NÃO PODE FICAR VAZIO!")
        return
    
    nome = input("Digite o nome do galpão:").strip()
    
    if not nome:
        print("NOME NÃO PODE FICAR VAZIO!")
        return
    
    endereco = input("Digite o endereco do galpão:").strip()
    
    if not endereco:
        print("ENDERECO NÃO PODE FICAR VAZIO!")
        return
    
    novo_galpao = Galpao(codigo, nome, endereco)
    
    galpoes.append(novo_galpao)
    
    print("Você deseja remover o galpão? A remoção causará perda irreversível dos dados associados!")
    print(galpoes[0])
    
    resposta = input("S/N")
    if resposta == "S":
        galpoes.pop(0)
    
    
galpoes = []

while True:
    
    print('''
          Bem vindo à GALPAX
          
          Menu:
          
            1. Cadastrar Novo Galpão
            
            0. Sair
          ''')
    
    op = input("Digite a opção desejada: ")
    
    if op == "1":
        cadastrar_novo_galpao()
    elif op == "0":
        print("Saindo do programa...")
        break
    else:
        print("Digite uma opção correta...")
        
    input("DIGITE ENTER PARA CONTINUAR")