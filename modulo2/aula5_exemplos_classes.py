class Pilha:
    def __init__(self, livros_cabeceira):
        self.itens = livros_cabeceira
    
    def pop(self):
        return self.itens.pop()
    
    def append(self, item):
        return self.itens.append(item)
    
    def tamanho(self):
        return len(self.itens)

livros_cabeceira = Pilha(["Josué de Castro"])
print(livros_cabeceira.itens)
