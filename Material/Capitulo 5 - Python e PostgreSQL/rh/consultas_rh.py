# Capítulo 5 · consultas_rh.py
# Consultas pontuais com a classe Banco: cada uma abre, roda e fecha a conexão.
# Os valores digitados entram no SQL como parâmetros (%s), nunca colados no texto.

from classBanco import Banco

banco = Banco()

# 1) Sem parâmetro: todos os setores
print("SETORES")
setores = banco.consultar("SELECT cod_setor, nome_setor FROM setores ORDER BY cod_setor")
for cod, nome in setores:
    print(cod, "-", nome)

# 2) Um parâmetro: os funcionários de um setor
print()
cod_setor = int(input("Ver os funcionários de qual setor? "))
linhas = banco.consultar(
    """SELECT nome_funcionario, cargo_funcionario, salario_funcionario
       FROM funcionarios
       WHERE cod_setor = %s
       ORDER BY nome_funcionario""",
    (cod_setor,),
)
if len(linhas) == 0:
    print("Nenhum funcionário nesse setor.")
for nome, cargo, salario in linhas:
    print(f"{nome} | {cargo} | R$ {salario:,.2f}")

# 3) Busca por parte do nome: o % vai no valor, não no SQL
print()
termo = input("Buscar pelo nome: ")
linhas = banco.consultar(
    "SELECT nome_funcionario, cargo_funcionario FROM funcionarios WHERE nome_funcionario ILIKE %s",
    ("%" + termo + "%",),
)
for nome, cargo in linhas:
    print(nome, "-", cargo)

# 4) Dois parâmetros, na ordem dos %s: o novo salário e o código
print()
cod = int(input("Código do funcionário para reajustar: "))
novo_salario = float(input("Novo salário: R$ "))
quantidade = banco.executar(
    "UPDATE funcionarios SET salario_funcionario = %s WHERE cod_funcionario = %s",
    (novo_salario, cod),
)
if quantidade == 0:
    print("Nenhum funcionário com esse código.")
else:
    print("Salário atualizado.")
