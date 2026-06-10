class Aluno():
    def __init__(self, nome, idade, matricula, notas, turma):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = notas
        self.turma = turma

    def mostrar_informacoes(self):

        print(f"""
Ficha do Aluno:
              
Nome: {self.nome}
Idade: {self.idade}
Matricula: {self.matricula}
Notas: {self.notas}
Média: {self.calcular_media():.1f}
Turma: {self.turma}

""")
        
    def calcular_media(self):
        media = sum(self.notas)/len(self.notas)
        return media