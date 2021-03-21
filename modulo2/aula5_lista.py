estudar_python = []

estudar_python.append("Condicionais")
estudar_python.append("Laços de repetição")
estudar_python.append("Lógica de programação")
estudar_python.append("Variáveis")
estudar_python.append("Listas")
estudar_python.append("Classes") 
estudar_python.append("Atributos")
estudar_python.append("Métodos")
estudar_python.append("Objetos") #adiciona elemento

print(estudar_python)
print(len(estudar_python)) #tamanho da lista

estudar_python.insert(0, "Algoritmos") #insere elemento numa posição específica
print(estudar_python)

estudar_python.pop() #remove último elemento da lista
print(estudar_python)

estudar_python.remove("Condicionais") #remove um elemento específico da lista
print(estudar_python)

estudar_python.sort() #ordena a lista
print(estudar_python)

estudos_adicionais = ["Pilha", "Fila"]
estudar_python.extend(estudos_adicionais) #estende a lista com uma nova sequência
print(estudar_python)

estudar_python.reverse()
print(estudar_python)
