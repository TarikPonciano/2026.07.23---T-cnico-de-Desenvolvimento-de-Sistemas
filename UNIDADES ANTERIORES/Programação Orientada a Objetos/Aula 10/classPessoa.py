class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos!")

    def fazer_aniversario(self):
        self.idade += 1

if __name__ == "__main__":
    pessoa1 = Pessoa("Jennifer", 35)

    pessoa1.apresentar()

    pessoa1.fazer_aniversario()

    pessoa1.apresentar()