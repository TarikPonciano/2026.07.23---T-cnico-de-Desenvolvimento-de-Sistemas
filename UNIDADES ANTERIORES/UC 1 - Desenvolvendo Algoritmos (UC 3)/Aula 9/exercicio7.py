# Entrada de Dados

num1 = float(input("Digite o primeiro número: "))

operacao = input("Escolha uma operação aritmética (+, -, *, /):")

num2 = float(input("Digite o segundo número: "))

# Processamento
resultado = 0 

# Realizar o cálculo correto
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":

    if num2 == 0:
        resultado = "TENTATIVA DE DIVISÃO POR 0"
    else:
        resultado = num1 / num2
        
else:
    resultado = "OPERAÇÃO INVÁLIDA"



# Saída

print(f"{num1} {operacao} {num2} = {resultado}")
