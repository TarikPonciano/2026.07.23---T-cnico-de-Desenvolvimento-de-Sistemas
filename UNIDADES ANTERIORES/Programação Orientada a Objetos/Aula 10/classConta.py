class Conta():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Tentativa de saque abortada! Valor de saldo é insuficiente!")
            return False

    def mostrar_saldo(self):

        print(f"""
Informações da Conta:
              
Titular: {self.titular}
Saldo Atual: R$ {self.saldo:,.2f}
""")
        
if __name__ == "__main__":

    conta1 = Conta("Denzel", 5000)

    conta1.sacar(2500)

    conta1.mostrar_saldo()

    conta1.depositar(1500)

    conta1.mostrar_saldo()

    while True:
        quantidade_saque = float(input("Digite quanto deseja sacar: "))

        resposta = conta1.sacar(quantidade_saque)

        if resposta == True:
            print(f"{conta1.titular} conseguiu comprar sua chinela havaianas!")
            break
        else:
            print(f"{conta1.titular} não conseguiu comprar sua chinela havaianas! Terá que voltar descalço para casa.")

    conta1.mostrar_saldo()