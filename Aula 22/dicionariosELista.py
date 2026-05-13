funcionarios = [
    {"Nome": "Joaquim", "Idade": 35, "Cargo": "Vendedor", "Salário": 5000},
    {"Nome": "Maria", "Idade": 28, "Cargo": "Analista de Marketing", "Salário": 6200},
    {"Nome": "Pedro", "Idade": 42, "Cargo": "Gerente de Vendas", "Salário": 8500},
    {"Nome": "Ana", "Idade": 31, "Cargo": "Desenvolvedora", "Salário": 7200},
    {"Nome": "Carlos", "Idade": 38, "Cargo": "Coordenador de TI", "Salário": 9800},
    {"Nome": "Fernanda", "Idade": 26, "Cargo": "Assistente Administrativo", "Salário": 3400},
    {"Nome": "Ricardo", "Idade": 45, "Cargo": "Diretor Comercial", "Salário": 15000},
    {"Nome": "Juliana", "Idade": 29, "Cargo": "Designer", "Salário": 5400},
    {"Nome": "Rafael", "Idade": 33, "Cargo": "Analista de Suporte", "Salário": 4700},
    {"Nome": "Patrícia", "Idade": 39, "Cargo": "Gerente de RH", "Salário": 8900},
    {"Nome": "Lucas", "Idade": 24, "Cargo": "Estagiário de Vendas", "Salário": 2100},
    {"Nome": "Camila", "Idade": 36, "Cargo": "Contadora", "Salário": 7500},
    {"Nome": "Eduardo", "Idade": 41, "Cargo": "Engenheiro de Software", "Salário": 11200},
    {"Nome": "Tatiana", "Idade": 30, "Cargo": "Analista de Qualidade", "Salário": 6000},
    {"Nome": "Gustavo", "Idade": 27, "Cargo": "Vendedor", "Salário": 4800},
    {"Nome": "Larissa", "Idade": 34, "Cargo": "Coordenadora de Projetos", "Salário": 9300},
    {"Nome": "Fábio", "Idade": 47, "Cargo": "Consultor", "Salário": 10500},
    {"Nome": "Renata", "Idade": 32, "Cargo": "Analista Financeiro", "Salário": 6800},
    {"Nome": "Thiago", "Idade": 25, "Cargo": "Auxiliar de Logística", "Salário": 3000},
    {"Nome": "Amanda", "Idade": 40, "Cargo": "Supervisora de Atendimento", "Salário": 7700}
]
contador = 1
print("Lista de Funcionários")
for func in funcionarios:
    print(f"{contador}. {func["Nome"]}")
    contador +=1

numero = int(input("Digite o número do funcionário que deseja visualizar:"))

funcionario_escolhido = funcionarios[numero-1]

print(f"""
FICHA PROFISSIONAL
      
      NOME: {funcionario_escolhido["Nome"]}
      IDADE: {funcionario_escolhido["Idade"]}


""")