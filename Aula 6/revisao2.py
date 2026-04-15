# 2. Crie um programa que pede um login e senha. Se o login informado for 'admin' e a senha for 'pass' mostre na tela "Acesso Concedido: {True/False}"

login = input("Digite seu login:")
senha = input("Digite sua senha:")

verificar_acesso = login == "admin" and senha == "pass"

print(f"Acesso Concedido: {verificar_acesso}")