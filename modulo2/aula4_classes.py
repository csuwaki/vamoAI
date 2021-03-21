#classe caneta
class Caneta:
    def __init__(self, marca, espessura, cor, tipo):
        self.marca = marca
        self.espessura = espessura
        self.cor = cor
        self.tipo = tipo
    
    def escrever(self, local):
        self.local = local

#classe relógio

class Relogio:
    def __init__(self, marca, tipo_pulseira, mecanismo, material):
        self.marca = marca
        self.tipo_pulseira = tipo_pulseira
        self.mecanismo = mecanismo
        self.material = material

    def mostrar_horas(self, visor, ponteiro):
        self.visor = visor
        self.ponteiro

    def alarme(self, horario, toque):
        self.horario = horario
        self.toque = toque

#classe gato
class Gato:
    def __init__(self, raca, miado, tamanho, peso, sexo):
        self.raca = raca
        self.miado = miado
        self.tamanho = tamanho
        self.peso = peso
        self.sexo = sexo
    
    def dormir(self, local_dormir):
        self.local_dormir = local_dormir
    
    def brincar(self, caixa_de_papelao):
        self.caixa_de_papelao = caixa_de_papelao
    
    def fazer_coco(self, local_coco):
        self.fazer_coco = fazer_coco
    
    def fazer_xixi(self, fazer_coco):
        self.fazer_xixi


