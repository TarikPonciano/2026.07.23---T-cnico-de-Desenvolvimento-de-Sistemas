class Retangulo():
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):

        area = self.altura * self.largura 
        print(f"A área do retângulo é: {area}m²")
        

    def calculare_perimetro(self):
        
        perimetro = (self.altura * 2) + (self.largura * 2)
        print(f"O perímetro do retângulo é: {perimetro}m")

    def desenhar_retangulo(self):

        linha = "+" * self.largura
        print (linha)
        for i in range(self.altura-2):
            print(f"+{" "*(self.largura-2)}+")
        print(linha)
        

if __name__ == "__main__":

    retangulo1 = Retangulo(5,6)
    
    retangulo1.calcular_area()

    retangulo1.calculare_perimetro()

    retangulo1.desenhar_retangulo()

    