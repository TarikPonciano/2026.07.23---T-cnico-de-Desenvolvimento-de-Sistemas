"""
== Igualdade
!= Diferença
> Maior que
< Menor que
>= Maior ou Igual
<= Menor ou Igual

is É idêntico a 
in Está dentro de
not Inversão de Valor
"""

# Crie um programa que recebe a idade de uma pessoa e exiba na tela se ela pode entar ou não (True ou False). O critério para entrar no sistema é ter idade maior ou igual a 18 anos.

# idade = int(input("Digite sua idade:"))

# verificacao_idade = idade >= 18

# print(f"Acesso ao Sistema: {verificacao_idade}")

# Crie um programa que pede o nome de um produto, o preço do produto e a quantidade do produto. Calcule o valor total a pagar e exiba na tela. Exiba também True ou False para a meta de venda. Meta é True se a venda for maior ou igual a 100 reais.

# prod_nome = input("Digite o nome do produto: ")
# prod_preco = float(input("Digite o preço do produto: "))
# prod_qtd = int(input("Digite quantas unidades foram compradas: "))

# valor_total = prod_preco * prod_qtd

# meta_atingida = valor_total >= 100


# print(f"""
# ------- Registro de Venda -------
      
#       Produto: {prod_nome}
#       Preço: R$ {prod_preco:.2f}
#       Quantidade: {prod_qtd}

#       Valor Total: R$ {valor_total:.2f}

#       Status da Meta: {meta_atingida}
# """)

# idade maior ou igual 13
# peso maior ou igual 50

idade = int(input("Digite a idade do visitante: "))
peso = float(input("Digite o peso do visitante: "))

verificar_idade = idade >= 13
verificar_peso = peso >= 50

pode_andar = verificar_idade and verificar_peso

print(f'''

    Checagem de Idade: {verificar_idade}
    Checagem de Peso: {verificar_peso}

    Pode Andar: {pode_andar}

''')

