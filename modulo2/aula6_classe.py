class Automovel:
    def __init__(self, tipo, modelo, ano, quilometragem_em_km):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem_em_km = quilometragem_em_km

carro = Automovel("SUV", "Jeep Renegade", "2021", 0)
print(carro.__dict__)

