class Produto:
    imposto = 1.05 
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor*Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Playstation 4', 'Video Game', 3000)
p2 = Produto('Xbox', 'Video Game', 4000)

print(p1.valor)
print(p2.valor)
print(p1.__dict__)