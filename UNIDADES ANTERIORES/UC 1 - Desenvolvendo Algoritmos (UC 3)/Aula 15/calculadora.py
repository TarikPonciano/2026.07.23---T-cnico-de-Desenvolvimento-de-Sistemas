# Crie uma calculadora onde a pessoa informa dois números e um operação (+,-,*,/). Ao terminar um cálculo exiba o resultado e pergunte se a pessoa deseja realizar outro cálculo. Caso a resposta seja sim, peça novamente os dois números e operação, caso a pessoa não deseje continuar encerre o programa.

while True:

    num1 = float(input("Digite o primeiro número: "))

    num2 = float(input("Digite o segundo número: "))

    print(f"""
    Escolha uma operação:
        
        1. Soma (+)
        2. Subtração (-)
        3. Multiplicação (*)
        4. Divisão (/)

    """)
    op = input("Digite a operação desejada:")

    resultado = 0

    if op == "1" or op == "+" or op == "Soma":
        resultado = num1 + num2
    elif op == "2" or op == "-" or op == "Subtração":
        resultado = num1 - num2
    elif op == "3" or op == "*" or op == "Multiplicação":
        resultado = num1 * num2
    elif op == "4" or op == "/" or op == "Divisão":
        if num2 == 0:
            resultado = "ERRO! DIVISÃO POR ZERO!"
        else:
            resultado = num1 / num2
    else: 
        resultado = "OPERAÇÃO INVÁLIDA"

    print(f"Resultado da Operação: {resultado}")

    resposta = input("Deseja continuar? (S/N)")
    
    if resposta == "N":
        print("Encerrando a calculadora...")
        break
    