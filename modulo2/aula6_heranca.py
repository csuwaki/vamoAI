"""Todos os métodos que se repetem na classe filha devem ser incluídos na classe mãe, para evitar possíveis erros,repetição de código e mais testes"""

class Automovel:
    def __init__(self, tipo, modelo, ano, quilometragem_em_km):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem_em_km = quilometragem_em_km

    def mostra_info(self):
        print(f'Tipo: {self.tipo}, Modelo: {self.modelo}, Ano: {self.ano}, Quilometragem: {self.quilometragem_em_km} km. ')
    
class Carro(Automovel):
    def __init__(self, tipo, modelo, ano, quilometragem_em_km):
        super().__init__(tipo, modelo, ano, quilometragem_em_km) #o método super() acessa ao construtor da Super classe Automovel
        

class Moto(Automovel):
    def __init__(self, tipo, modelo, ano, quilometragem_em_km):
        super().__init__(tipo, modelo, ano, quilometragem_em_km) #o método super() acessa ao construtor da Super classe Automovel
        
carro1 = Carro("SUV", "Jeep Renegade", 2021, 0)
carro1.mostra_info()

moto1 = Moto("Scooter", "Yamaha Neo 125", 2019, 30000 )
moto1.mostra_info()
