# Capítulo 5 · Gabarito da Prática 3 · consultas_cinema.py
# Quatro consultas pontuais com a classe Banco (copie o classBanco.py para esta pasta).
# Testes sugeridos: classificação L · título "dun" · sessão 3 para a sala 9, depois para a 5 ·
# excluir o filme 1 (tem sessões), o 99 (não existe) e o 5 (sem sessões).
#
# PENSE E RESPONDA: o filme 5 saiu e o 1 não. Quem decidiu foi a FK fk_sessao_filme,
# que está na tabela sessoes (o lado N): o filme 1 tem sessões apontando para ele;
# o filme 5, nenhuma.

import psycopg
from classBanco import Banco

banco = Banco()

# 1) Os filmes de uma classificação
classificacao = input("Classificação (L, 10, 12, 14, 16 ou 18): ").strip().upper()
filmes = banco.consultar(
    """SELECT titulo_filme, duracao_filme
       FROM filmes
       WHERE classificacao_filme = %s
       ORDER BY titulo_filme""",
    (classificacao,),
)
if len(filmes) == 0:
    print("Nenhum filme com essa classificação.")
for titulo, duracao in filmes:
    print(f"{titulo} ({duracao} min)")

# 2) As sessões de um filme, buscando por parte do título (JOIN + ILIKE)
print()
termo = input("Parte do título: ")
sessoes = banco.consultar(
    """SELECT f.titulo_filme, s.data_sessao, s.horario_sessao, s.sala_sessao
       FROM sessoes s
       JOIN filmes f ON f.cod_filme = s.cod_filme
       WHERE f.titulo_filme ILIKE %s
       ORDER BY s.data_sessao, s.horario_sessao""",
    ("%" + termo + "%",),
)
if len(sessoes) == 0:
    print("Nenhuma sessão encontrada.")
for titulo, data, horario, sala in sessoes:
    print(f"{titulo} | {data:%d/%m/%Y} às {horario:%H:%M} | sala {sala}")

# 3) Mudar a sala de uma sessão (a sala vai de 1 a 5: ck_sala)
print()
cod_sessao = int(input("Código da sessão: "))
nova_sala = int(input("Nova sala: "))
try:
    quantidade = banco.executar(
        "UPDATE sessoes SET sala_sessao = %s WHERE cod_sessao = %s",
        (nova_sala, cod_sessao),
    )
    if quantidade == 0:
        print("Nenhuma sessão com esse código.")
    else:
        print("Sala alterada.")
except psycopg.errors.CheckViolation:
    print("Sala inválida: o cinema tem as salas 1 a 5.")

# 4) Excluir um filme (filme com sessão não sai: fk_sessao_filme)
print()
cod_filme = int(input("Código do filme para excluir: "))
try:
    quantidade = banco.executar("DELETE FROM filmes WHERE cod_filme = %s", (cod_filme,))
    if quantidade == 0:
        print("Nenhum filme com esse código.")
    else:
        print("Filme excluído.")
except psycopg.errors.ForeignKeyViolation:
    print("Esse filme tem sessões: exclua as sessões antes.")
