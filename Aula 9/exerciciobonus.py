print("Bem vindo à Lanchonete XYZ")

print("""
Código | Produto            | Preço (R$) | Categoria
001    | X-Burguer          | R$ 18,00   | Lanches
002    | X-Salada           | R$ 20,00   | Lanches
003    | X-Bacon            | R$ 22,00   | Lanches
004    | Hot Dog Simples    | R$ 12,00   | Lanches
005    | Hot Dog Especial   | R$ 16,00   | Lanches
006    | Batata Frita P     | R$  9,00   | Acompanhamentos
007    | Batata Frita G     | R$ 14,00   | Acompanhamentos
008    | Onion Rings        | R$ 11,00   | Acompanhamentos
009    | Refrigerante Lata  | R$  6,00   | Bebidas
010    | Suco Natural       | R$  8,00   | Bebidas
011    | Milk-Shake         | R$ 15,00   | Bebidas
012    | Sorvete 2 Bolas    | R$ 10,00   | Sobremesas
""")
print()

codigo = input("Digite o código do produto desejado: ")
qtd_produto = int(input("Digite a quantidade de produto desejado: "))

nome_produto = ""
preco_produto = 0

if codigo == "001":
    nome_produto = "X-Burguer"
    preco_produto = 18
elif codigo == "002":
    nome_produto = "X-Salada"
    preco_produto = 20
else:
    print("PRODUTO NÃO IDENTIFICADO")
    

total_venda = preco_produto * qtd_produto

print(f"""
--- RESUMO DO PEDIDO --- 
Produto: {nome_produto}
Preço unitário: R$ {preco_produto:.2f}
Quantidade: {qtd_produto} 
Total a pagar: R$ {total_venda}
Obrigado pela preferência!
""")

