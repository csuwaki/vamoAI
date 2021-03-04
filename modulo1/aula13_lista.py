""" append, pop, remove, count, reverse, insert, len, lista com repartição
"""

lista_convidados = ["Carol", "Lis", "Mateus", "Aline", "Felipe"]

lista_convidados.append("Lalá")
lista_convidados.append("Lelê")
print(lista_convidados)

lista_convidados.pop(0)
print(lista_convidados)

lista_convidados.remove("Lis")
print(lista_convidados)
print(len(lista_convidados))

lista_convidados.reverse()
print(lista_convidados)

lista_convidados.insert(2, "Lis")
print(lista_convidados)

print(lista_convidados[:2])