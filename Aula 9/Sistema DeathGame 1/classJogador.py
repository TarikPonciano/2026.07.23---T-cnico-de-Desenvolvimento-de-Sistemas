from random import randint

class Jogador():

    def __init__(self, nome, ocupacao, pct_sobrevivencia=50, situacao="Vivo"):
        self.nome = nome
        self.ocupacao = ocupacao
        self.pct_sobrevivencia = pct_sobrevivencia
        self.situacao = situacao
        self.vida = 100

    def ver_ficha(self):

        print(f"""
Ficha do Jogador:
              

    Nome: {self.nome}
    Ocupação: {self.ocupacao}
    Situação: {self.situacao}
    Chance de Sobrevivência Atual: {self.pct_sobrevivencia:.1f}%
    Vida Atual: {self.vida} / 100
""")

    def testar_sobrevivencia(self):
        if self.situacao == "Vivo":
            dado = randint(1, 100)

            if dado <= self.pct_sobrevivencia:
                print("O Jogador Sobreviveu a essa prova!")
            else:
                print("O Jogador foi machucado durante essa prova!")
                self.vida -= 10
                if self.vida <= 0:
                    print("O Jogador não resistiu aos ferimentos e morreu")
                    self.situacao = "Morto"
        else:
            print("O JOGADOR JÁ ESTÁ MORTO")

    def alterar_sobrevivencia(self, variacao, tipo):
        nova_sobrevivencia = self.pct_sobrevivencia

        if tipo == "Aumentar":
            nova_sobrevivencia = self.pct_sobrevivencia + variacao
        else:
            nova_sobrevivencia = self.pct_sobrevivencia - variacao


        if nova_sobrevivencia >= 0 and nova_sobrevivencia <= 100:
            self.pct_sobrevivencia = nova_sobrevivencia
        else:
            print("TENTATIVA DE ALTERAR SOBREVIVÊNCIA PARA VALORES NÃO AUTORIZADOS!")