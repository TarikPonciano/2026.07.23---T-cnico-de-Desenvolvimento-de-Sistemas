#Representar a venda de 1 tipo de produto
class Venda():
    def __init__(self, nome_prod, preco_prod, qtd_prod, nome_vendedor, nome_loja):
        self.nome_prod = nome_prod
        self.preco_prod = preco_prod
        self.qtd_prod = qtd_prod
        self.nome_vendedor = nome_vendedor
        self.nome_loja = nome_loja

        self.total_venda = round(preco_prod * qtd_prod, 2)

    def mostrar_informacoes(self):
        print(f"""
Nome: {self.nome_prod}
Quantidade: {self.qtd_prod}
Total: R$ {self.total_venda:.2f}
""")
        
    def alterar_quantidade(self, nova_qtd):
        if nova_qtd > 0:
            self.qtd_prod = nova_qtd

            self.atualizar_total()

            return True
        else:
            print("Tentativa de alterar quantidade com número inválido!")
            return False
    def alterar_preco(self, novo_preco):
        if novo_preco > 0:

            self.preco_prod = novo_preco

            self.atualizar_total()
            return True
        else:
            print("Tentativa de alterar o preço com número inválido!")
            return False
        
    def atualizar_total(self):

        self.total_venda = round(self.qtd_prod * self.preco_prod, 2)

if __name__ == "__main__":

    venda_teste = Venda("TV 52' LG SMART", 2800, 1, "Vinicius", "Magazine Luisa")

    venda_teste.alterar_preco(2800*0.9)

    venda_teste.mostrar_informacoes()