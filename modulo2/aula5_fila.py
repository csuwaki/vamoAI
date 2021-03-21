class Fila:
    def __init__(self):
        self.queue = []
    
    def tamanho(self):
        return len(self.queue)
    
    def partida(self):
        return self.queue.pop(0)
    
    def chegada(self, pessoas):
        return self.queue.append(pessoas)
        
Banco = Fila()
Banco.chegada("Pessoa 1")
Banco.chegada("Pessoa 2")
Banco.chegada("Pessoa 3")
Banco.chegada("Pessoa 4")

print(Banco.queue)
print(Banco.tamanho())

Banco.partida()

print(Banco.tamanho())
print(Banco.queue)


