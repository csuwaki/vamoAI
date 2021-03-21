""" POO - Polimorfismo #curso de python udemy

Quando reimplementamos um método presente na classe Mãe em classes filhas
estamos realizando uma sobrescrita de método (Overriding)
Ou seja, estamos mudando o comportamento do objeto. No exemplo, existe o método falar(), mas cada animal fala de um jeito.
O overriding é a melhor representação do polimorfismo.
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome
    
    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este método") #raise lança uma exceção, a classe filha deverá implementar este método

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala au au!")

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()