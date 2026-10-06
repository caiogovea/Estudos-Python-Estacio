class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo: R${self.saldo}")


conta = Conta(100)

conta.mostrar_saldo()

conta.depositar(50)
conta.mostrar_saldo()

conta.sacar(30)
conta.mostrar_saldo()

conta.sacar(200)