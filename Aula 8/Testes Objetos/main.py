from classAluno import Aluno
from classLivro import Livro
from classPokemon import Pokemon

aluno1 = Aluno("Joaquim", 32, 1, [7,8,8.5,9], "A")

aluno2 = Aluno("Manoel", 35, 2, [8,8,9,9], "B")

print(f"""
Ficha do Aluno:
      
      Nome: {aluno1.nome}
      Idade: {aluno1.idade}
      Matricula: {aluno1.matricula}
      Notas: {aluno1.notas}
      Turma: {aluno1.turma}

""")

livro1 = Livro("Crônicas de Nárnia", "J.k Lewis", "Fantasia")

print(f"""

FICHA DO LIVRO:

Título: {livro1.titulo}
Autor: {livro1.autor}
Genero: {livro1.genero}
    
      """)


poke1 = Pokemon("Pikachu", "Elétrico", 24)

print(f"""

POKEDEX:
      
Espécie: {poke1.especie}
Tipo: {poke1.tipo}
Level: {poke1.level}

""")