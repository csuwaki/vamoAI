"""#curso de python udemy
Quando uma classe herda de outra classe, ela herda todos os atributos
e métodos da classe herdada.

A classe de quem se herda (ex. Pessoa) é conhecida como: Super classe; Classe Mãe; 
Classe Pai; Classe Base; Classe Genérica.

A classe que herda (ex. Cliente, Funcionário) é conhecida como: Sub Classe; Classe Filha; Classe Específica.
"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
class Cliente(Pessoa): #Cliente herdou de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) #o método super() acessa ao construtor da Super classe
        self.__renda = renda

class Funcionario(Pessoa): #classe funcionário também herdou de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

cliente = Cliente("Caroline", "Suwaki", "123.456.789.0", 10000)
funcionario = Funcionario("Caroline", "Harumy", "123.456.789.5", 20000)
print(cliente.__dict__)
print(funcionario.__dict__)
