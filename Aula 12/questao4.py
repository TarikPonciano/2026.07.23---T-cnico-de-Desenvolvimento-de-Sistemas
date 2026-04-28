# 4. Receba o nome, o preço e a quantidade de 5 produtos diferentes. Ao final exiba o valor total que o cliente deverá pagar.

# Bônus: Exiba uma nota fiscal com tudo que foi comprado e as informações da venda ao final.
valor_final = 0
nota_fiscal = ""


for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}:"))
    qtd = int(input(f"Digite a quantidade do produto {i+1}:"))

    valor_compra = preco * qtd

    valor_final += valor_compra

    nota_fiscal += f"{nome} | R$ {preco:.2f} | {qtd}  - R$ {valor_compra:.2f}\n"

    
print("------ NOTA FISCAL ------")

print("NOME | PREÇO (R$) | QUANTIDADE - TOTAL (R$)")

print(nota_fiscal)

print(f"Valor total da compra é: R${valor_final:.2f}")