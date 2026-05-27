## TITULO 01 - Simulador de Emprestimo bancario.
# 
# CONTEXTO: Maria deseja solicitar um emprestimo bancario ao Banco para o financiamento
# de uma casa. O banco possui regras claras para aprovar ou negar o credito bancario.
# 
# REGRA: O emprestimo será aprovado quando a prestacao mensal não exceder 30% de seu salario.
# 
# O programa deve receber:
# 01) - O valor da casa que será financiada pelo banco.
# 02) - O valor do Salario da pessoa que deseja o financiamento.
# 03) - Quantos anos de financiamento do emprestimo.

#Resumo - Calcule se o valor do empréstimo for maior ou menor que o salário de Maria.
#         Se o valor da prestação exeder o limite de 30% do salário, empréstimo negado.
#         Se o valor da prestação não exceder o limete empréstimo aprovado.     
# ----------------------------------------------------------------------

print("-="*20)
print("*** EMPRESTIMO BANCARIO PARA FINANCIAMENTO/ BANCO XYZ ***")
print("-="*20)

Valor_financ = float(input("Qual o valor da casa que deseja financiar: R$ "))
salario = float(input("Qual o salario do comprador: "))
anos_financ = int(input("Quantos anos de financiamento: ")) 

meses = anos_financ * 12 # Calcular meses de financiamento.
prestacao = Valor_financ / meses # Calcular o valor da prestacao.
limite_salario = salario * 0.30

print("\n--- ANÁLISE DO FINANCIAMENTO ---")
print(f"Para o Financiamento de uma casa R$ {Valor_financ:.0f} em {anos_financ} anos e com o salario: R$ {salario:.0f}:")
if  prestacao > limite_salario:
    print("EMPRESTIMO NEGADO!")
    print(f"Quantidade de parcelas: {meses}")
    print(f"Valor da prestação mensal: R$ {prestacao:.2f}")
    print(f"Limite máximo da prestação (30% do salário): R$ {limite_salario:.0f}")
    
elif prestacao <= limite_salario:
    print("EMPRESTIMO APROVADO!") 
    print(f"Quantidade de parcelas: {meses}")
    print(f"Valor da prestação mensal: R$ {prestacao:.2f}")
    print(f"Limite máximo da prestação (30% do salário): R$ {limite_salario:.0f}")



#------------------------------------------------------------------------------------

# TITULO 02 - SIMULADOR DE ALISTAMENTO MILITAR.
# 
# CONTEXTO: Joao deseja se alistar no serviço militar porém é preciso analisar sua idade.
# 
# REGRA: O programa deve informar se já é hora de alistar ou já passou o tempo do alistamento.
# Deve conter o tempo que falta para se alistar ou o prazo que passou.
# (No Brasil, o alistamento é obrigatorio aos 18 anos de idade. )
# 
# O programa deve pedir:
# 01) O ano de nascimento do solicitante.
# ----------------------------------------------------------------------------

print("==================ALISTAMENTO MILITAR===========================")
ano_nasc = int(input("Ano de Nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.")

if idade == 18:
    print("Voce tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o seu alistamento.")
    ano = ano_atual + saldo
    print(f"Seu alistamento será no ano: {ano}")
elif idade > 18:
    saldo = idade - 18
    print(f"Voce já deveria ter se alistado há {saldo} anos.")
    ano = ano_atual - saldo
    print(f"Seu alistamento foi ano: {ano}")


#----------------------------------------------------------------------------------

#TITULO 3 - SIMULADOR DE UM PAGAMENTO:
# O programa deve ser exeutado e um laço de repetição while.

#CONTEXTO: João deseja efetuar um pagamento de uma conta, com as seguintes opções:
# 1: À vista dinheiro com 10% de desconto.
# 2: À vista no cartão com 5% de desconto.
# 3: Até 2 parcelas no cartão sem desconto.
# 4: 3 parcelas ou mais com 20% de juros do total da compra.

# REGRA - O usuário deve escolher uma dessas opções, e deve aparecer o valor final a ser calculado,
# dependendo da situação. Se o usuário digitar o número 0 nas opções, encerre o programa.

# O programa deve pedir o preço da compra.
while True:
    print("=====GERENCIADOR DE PAGAMENTO = LOJAS WANDY=================")
    preco = float(input("Preco das compras: R$ "))
    print("""
        FORMAS DE PAGAMENTO:    
        [1] à Vista dinheiro/Pix
        [2] à Vista no cartão
        [3] 2x no cartão
        [4] 3x ou mais no cartão
        [0] Sair
        
    """)    
    opcao = (input("Qual é a opção desejada: "))
    if opcao == "1":
        total = preco - (preco * 10 / 100)
        desc = preco * 10 / 100
    elif opcao == "2":
        total = preco - (preco * 5 / 100)
        desc = preco * 5 / 100
    elif opcao == "3":    
        total = preco   
        parcela  = total / 2    
        desc = 0
        print(f"Sua compra será parcelada em 2X de R$ {parcela} SEM JUROS.")
    elif opcao == "4":
        total = preco + (preco * 20 /100)
        totalparc = int(input("Quantas parcelas: "))
        parcela = total / totalparc
        desc = 0
        print(f"Sua compra será parcelada em {totalparc} de R$ {parcela:.2f} COM JUROS de 20%.")
        
    elif opcao == "0":
            
            print("Encerrando programa...")
            break
            
            

    print(f"Sua compra de {preco:.2f} vai custar R$ {total:.2f} no final. Seu desconto foi de R$ {desc}.")





















