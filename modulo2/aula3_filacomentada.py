#criando uma fila
queue = ["definir grupo", "definir tema do projeto", "título", "ideias", "história", "fluxograma", " fazer código"]

#adicionando um novo item à fila
queue.append("melhorias no código")

#mostra fila
print(queue)

#remove primeiro item. FIFO (First In, First Out)
queue.pop(0)
print(queue)

#com a remoção, o item de índice [1] passa para o [0], e será o próximo a ser removido.
queue.pop(0)
print(queue)

