# 5. Verificação de estoque
# Um mercadinho tem a lista estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]. Peça ao usuário um produto com input() e informe se ele está ou não disponível no estoque. Depois, exiba o estoque em ordem alfabética usando sorted().

estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]

produto = input("Digite o nome de algum produto: ")

# achou = False
# for p in estoque:

#     if produto == p:
#         achou = True
#         break

# if achou == True:
#     print("Produto em estoque")
# else:
#     print("Produto fora de estoque")

if produto in estoque:
    print("Produto em estoque.")
else:
    print("Produto fora de estoque.")


#estoque.sort()

estoque_alfabetica = sorted(estoque)
numero = 1
for p in estoque_alfabetica:
    print(f"{numero}. {p}")
    numero += 1