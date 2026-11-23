from classBanco import Banco

banco = Banco()
def cadastrarVenda():
    # Mostrar os clientes 
    
    # verClientes()
    clientes = None
    try:
        clientes = banco.consultar("SELECT * FROM clientes;")
        
    except Exception as error:
        print("Erro ao consultar tabela de clientes!")
        print(error)
    
    if (not clientes):
        print("Não há clientes para visualização!")
        return
    
    print("LISTA DE CLIENTES")
    for cliente in clientes:
        print(f"{cliente[0]}. {cliente[1]}")
    
    # Escolher o cliente
    cliente_escolhido = int(input("Digite o número do cliente desejado: "))
    
    # Mostrar produtos
    
    produtos = None
    try:
        produtos = banco.consultar("SELECT * FROM produtos;")
        
    except Exception as error:
        print("Erro ao consultar tabela de produtos!")
        print(error)
    
    if (not produtos):
        print("Não há produtos para visualização!")
        return
    
    print("LISTA DE PRODUTOS")
    for produto in produtos:
        print(f"{produto[0]}. {produto[1]} - R$ {produto[2]:,.2f}")
    
    
    # Escolher os produtos
    itens = []
    
    while (True):
        
        cod_produto = int(input("Digite o código do produto que deseja comprar: "))
        
        produto_original = None
        try:
            produto_original = banco.consultar("SELECT * FROM produtos WHERE cod_produto = %s", (cod_produto,))
        except Exception as error:
            print("Erro ao consultar produto informado.")
            
        if (not produto_original):
            print("Tente um novo produto")
            continue
        
        qtd_produto = int(input("Digite quantas unidades deseja comprar: "))
        
        preco_produto = produto_original[0][2]
        
        itens.append((cod_produto, qtd_produto, preco_produto))
        
        continuar = input("Deseja continuar? (S/N) ")
        
        if (continuar == "N"):
            print("Encerrando carrinho de compras...")
            break
        
    try:
        banco.registrarVenda(cliente_escolhido, itens)
    except Exception as error:
        print("Erro ao cadastrar venda! Por favor recomece o processo de venda...")
        
        
def verVendas():
    print("LISTA DE PEDIDOS")
    pedidos = None
    try:
        pedidos = banco.consultar("SELECT p.cod_pedido, c.nome_cliente, p.data_pedido, p.status FROM PEDIDOS p JOIN clientes c ON c.cod_cliente = p.cod_cliente;")
        
    except Exception as error:
        print("ERRO AO CONSULTAR PEDIDOS")
        
    if (not pedidos):
        print("NÃO HÁ PEDIDOS")
        return
    print("Código | Cliente | Data | Status")
    for pedido in pedidos:
        print(f"{pedido[0]} | {pedido[1]} | {pedido[2]} | {pedido[3]}")
        
        
    id_escolhido = int(input("Escolha um dos pedidos para ver mais detalhes: "))
    pedido_escolhido = None
    try:
        pedido_escolhido = banco.consultar("SELECT * FROM itens_pedido WHERE cod_pedido = %s", (id_escolhido,))
    except Exception as error:
        print("Não foi possível encontrar o pedido")
        print(error)
        
    if (not pedido_escolhido):
        return
    
    print("NOTA FISCAL")
    total = 0
    for item in pedido_escolhido:
        print(f"{item[0]} - {item[2]} - {item[3]} - R$ {item[4]:.2f} - R$ {(item[3] * item[4]):.2f}")
        total += item[3] * item[4]

    
    print(f"VALOR TOTAL A PAGAR: R$ {total:.2f}")
        

        
        
        
        
        
    

while (True):
    
    print("BEM VINDO AO LOJA CONECTA")
    
    print("""
    ESCOLHA UMA OPÇÃO DO MENU:
    
    1. Cadastrar Nova Venda
    2. Ver Vendas
    
    0. Sair
          """)
    
    op = input("Digite o número da opção desejada: ")
    
    if (op == "1"):
        cadastrarVenda()
    elif (op == "2"):
        verVendas()
    elif (op == "0"):
        print("SAINDO DO PROGRAMA...")
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA")
        
    input("TECLE ENTER PARA CONTINUAR")