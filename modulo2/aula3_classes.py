class Cachorro:
    def __init__(self, nome, cor, raca, porte, patas):
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.porte = porte
        self.patas = patas

    def comer(self, racao):
        self.racao = racao
    
    def dormir(self, lugar):
        self.lugar = lugar
    
    def latir(self, tipo_de_latido):
        self.tipo_de_latido = tipo_de_latido
    
    def fazer_coco(self, local_coco):
        self.local_coco = local_coco
    
    def fazer_xixi(self, local_xixi):
        self.local_xixi = local_xixi