# Faça um menu de atendimento eletrônico que contenham as opções:

# 1. Falar com atendente
# 2. Finalizar contrato
# 3. Abrir nova conta
# 4. Visualizar segunda via da fatura
# 0. Sair

# Cada opção deve exibir uma mensagem relevante. Ao ver a mensagem, volte para o menu e peça uma nova opção do usuário. Se a pessoa escolher a opção Sair, encerre o programa. Caso a pessoa escreva uma opção inválida exiba uma mensagem de erro e volte para o menu.
print("Bem vindo ao Sistema XYZ")
while True:

    print(f"""
    Menu de Opções:
        
        1. Falar com atendente
        2. Finalizar contrato
        3. Abrir nova conta
        4. Visualizar segunda via da fatura

        0. Sair

    """)

    op = input("Digite o número da opção desejada: ")

    if op == "1":
        print("Aguarde um atendente ficar disponível para lhe atender...")
    elif op == "2":
        print("Proíbido finalizar contrato :-)")
    elif op == "3":
        print("Processo de criação de conta iniciado...")
    elif op == "4":
        print("Visite uma de nossas agências presenciais para emitir suas segunda via da fatura!")
    elif op == "0":
        print("Finalizando o programa...")
        break
    else:
        print("Digite uma opção válida!")


    input("TECLE ENTER PARA CONTINUAR")
