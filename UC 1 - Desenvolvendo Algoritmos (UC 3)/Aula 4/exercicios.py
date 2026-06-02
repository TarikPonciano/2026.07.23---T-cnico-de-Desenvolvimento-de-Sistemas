# Crie um programa que pede o nome da pessoa e o ano de nascimento da pessoa. Exiba o nome e a idade da pessoa.

nome = input("Digite o seu nome:")
ano_nascimento = int(input("Digite o ano em que nasceu:"))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print(f"Olá, {nome}!")
print(f"Você tem {idade} anos.")

# Crie um programa que recebe o nome de um produto, o preço e a quantidade comprada desse produto. Exiba ao final o valor total a pagar desse produto.

nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
qtd_produto = int(input("Digite quantas unidades deseja comprar: "))

valor_total = qtd_produto * preco_produto

print(f"Você comprou {qtd_produto} unidades de {nome_produto} e precisará pagar R$ {valor_total:.2f}")

# Crie um programa que pede o nome de um aluno e suas 4 notas. Ao final exiba a média do aluno.

print("Bem vindo ao Sistema Escolar XYZ")

nome_aluno = input("Digite o nome do aluno:")

n1 = float(input("Digite a nota 1:"))
n2 = float(input("Digite a nota 2:"))
n3 = float(input("Digite a nota 3:"))
n4 = float(input("Digite a nota 4:"))

media_notas = (n1 + n2 + n3 + n4) / 4

print(f"A média do aluno {nome_aluno} é: {media_notas:.1f}")