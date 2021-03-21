class ContaCorrente:
    contador = 4999 # para o numero da primeira conta ser 5000

    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.numero