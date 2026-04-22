preco_produto = float(input("Digite o preço do produto: "))

qtd_produto = int(input("Digite quantas unidades foram compradas: "))

valor_total = preco_produto * qtd_produto

desconto = 0

if valor_total > 100 or qtd_produto >= 5:
    desconto = valor_total * 0.15
    

elif valor_total <= 100 and qtd_produto >= 3:
    desconto = valor_total * 0.1

else: 
    desconto = 0

    
valor_final = valor_total-desconto

print(f"O valor total da compra era: R$ {valor_total:.2f}")
print(f"Você recebeu desconto de: R$ {desconto:.2f}")
print(f"O valor final da compra é: R$ {valor_final:.2f}")



