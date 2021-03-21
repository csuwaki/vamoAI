"""POO - Herança múltipla

Herança múltipla nada mais é do que a possibilidade de uma classe herdar
de múltiplas classes, fazendo com que a classe filha herde todos os atributos
e métodos de várias classes.

- Pode ser feita por multiderivação direta ou indireta.

"""

class Animal:
    
    def __init__(self, nome):
        self.nome = nome
    
    def cumprimentar(self):
        return f'Oi! Eu sou {self.nome}!'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} nada.'
  

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} anda.'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

baleia = Aquatico('Wally')
print(baleia.cumprimentar())
print(baleia.nadar())

cachorro = Terrestre('Rex')
print(cachorro.cumprimentar())
print(cachorro.andar())

carlos = Pinguim('Carlos')
print(carlos.cumprimentar())
print(carlos.andar())
print(carlos.nadar())