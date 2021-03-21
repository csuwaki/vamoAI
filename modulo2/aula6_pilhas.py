class PilhaDeRoupas:
    def __init__(self):
        self.pilhaderoupas = []

    def adicionar(self, roupa):
        return self.pilhaderoupas.append(roupa)
    
    def tamanho(self):
        return len(self.pilhaderoupas)

    def remover(self):
        if len(self.pilhaderoupas) == 0:
            return None
        else:
            return self.pilhaderoupas.pop()
        
Pilha = PilhaDeRoupas()
print(Pilha.pilhaderoupas)

Pilha.adicionar("Vestidos")
Pilha.adicionar("Calças")
Pilha.adicionar("Shorts")
Pilha.adicionar("Camisetas")

print(Pilha.pilhaderoupas)

Pilha.remover()
print(Pilha.pilhaderoupas)

Pilha.remover()
print(Pilha.pilhaderoupas)

print(Pilha.tamanho())

print(Pilha.pilhaderoupas.pop())


 rev = ''
  while len(stack) > 0:
       last = stack.pop()
       rev = rev + last
       # print(last, rev)
       
  return rev