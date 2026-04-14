#Revisão 2: Faça um programa de cadastro de funcionário onde são pedidos 5 informações de um funcionário (você escolhe as informações). Uma informação deve ser número decimal(float) e outra informação deverá ser o ano de nascimento. Ao final imprima a ficha do funcionário incluindo sua idade (sugestão use multi-linha)
print("RH Soluções XYZ")
print()
print("Cadastro de Funcionários")

func_nome = input("Digite o seu nome: ")
func_ano_nasc = int(input("Digite o ano em que nasceu:"))
func_cargo = input("Digite o seu cargo: ")
func_salario = float(input("Digite o salário do funcionário: "))
func_cpf = input("Digite o seu cpf:")

func_idade = 2026 - func_ano_nasc

print(f"""
Ficha do Funcionário:
      
      Nome: {func_nome}
      CPF: {func_cpf}
      Idade: {func_idade}
      Cargo: {func_cargo}
      Salário: R$ {func_salario:.2f}

""")