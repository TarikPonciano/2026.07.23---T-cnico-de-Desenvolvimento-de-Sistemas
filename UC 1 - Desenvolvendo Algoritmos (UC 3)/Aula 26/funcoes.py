def minha_funcao(texto):
    
    print(f'Essa é minha função. {texto}')

texto = "Hoje é dia 20/05/2026"

minha_funcao(texto)

minha_funcao("Boa noite!")

def ver_detalhes_funcionario(nome, salario, cargo):
    print(f"""
DETALHES DO FUNCIONÁRIO

Nome: {nome}
Salário: R$ {salario:,.2f}
Cargo: {cargo}
""")
    
def somar (num1, num2):
    soma = num1 + num2
    print(f"Resultado da soma: {soma} ")

def dividir(num1, num2):
    resultado = num1 / num2

    return resultado

# Calculadora de 10%. Crie uma função que recebe o valor de uma conta, use o valor dessa conta para calcular a gorjeta(10%) e o valor final da conta (total + gorjeta) e imprima na tela uma nota fiscal do que o usuário terá que pagar.

def calculadora_gorjeta_padrao(valor_conta):
    gorjeta = valor_conta * 0.10
    valor_final = valor_conta + gorjeta

    print(f"""
============ NOTA FISCAL ============
          
VALOR DA CONTA: R$ {valor_conta:,.2f}
GORJETA (10%): R$ {gorjeta:,.2f}

TOTAL A PAGAR: R$ {valor_final:,.2f}
""")

# Calculadora de gorjeta. Crie uma função que recebe as informações valor da conta e porcentagem da gorjeta, a função deverá retornar o valor total a ser pago pelo cliente, imprima na tela.

def calcular_gorjeta_personalizada(valor_conta, pct_gorjeta):
    gorjeta = valor_conta * pct_gorjeta

    valor_total = valor_conta + gorjeta

    return valor_total

# Crie uma função de calculadora. Essa função deve receber as informações num1, num2 e operação, essa função deverá retornar o resultado da operação escolhida. Imprima o resultado de 5 operações com essa ferramenta. P.S: Lembre de verificar divisões por 0 e forneça o resultado adequado.

def calculadora(num1, num2, operacao):
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            resultado = "TENTATIVA DE DIVISÃO POR ZERO. RESULTADO INVÁLIDO!"
        else:
            resultado = num1 / num2
    else:
        resultado = "OPERAÇÃO INVÁLIDA"

    return resultado


# resultado1 = calculadora(30, 20, "*")
# resultado2 = calculadora(30, 20, "/")
# resultado3 = calculadora(30, 20, "+")
# resultado4 = calculadora(30, 20, "-")
# resultado5 = calculadora(30, 0, "/")

# print(f"""

# RESULTADO 1: {resultado1}
# RESULTADO 2: {resultado2}
# RESULTADO 3: {resultado3}
# RESULTADO 4: {resultado4}
# RESULTADO 5: {resultado5}

# """)