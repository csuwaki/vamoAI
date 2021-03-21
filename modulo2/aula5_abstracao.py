"""Abstração e encapsulamento

O grande objetivo da programação orientada a objetos (POO) é encapsular
nosso código dentro de um grupo lógico e hierarquico utilizando
classes. Ou seja, uma classe é o encapsulamento de atributos e métodos.

       classe
----------------------
 atributos e métodos
----------------------

Abstração em POO é o ato de expor apenas dados relevantes de uma classe
escondendo atributos e métodos privados de usuário.
"""

class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1
    
    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
            
            else:
                print("Saldo insuficiente")
        else:
            print("O valor deve ser positivo")
        
    def transferir(self, valor, conta_destino): 
        self.saldo -= valor #remover valor da conta de origem 
        self.saldo -= 10 #taxa de transferência
        conta_destino.saldo += valor #adicionar valor na conta de destino

#Teste

conta1 = Conta("carol", 150, 1500)
conta2 = Conta("Caroline", 1500, 3000)

conta1.extrato()
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()