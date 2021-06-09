import statistics

import matplotlib.pyplot as plt

func1=[12,12,7,8,5,6,7,8,9,10,11,12]
func2=[12,7,9,6,5,10,12,5,4,7,9,9]
func3=[12,7,9,6,5,10,12,5,4,7,9,9]
func4=[10,10,9,2,11,3,4,7,6,9,10,4]


plt.title("Vendas de roupas", fontsize=20,c='red')
Eixo_x=['Dia 1', 'Dia 2', "dia 3", 'dia 4', 'dia 5', 'dia 6','dia 7','dia 8', 'dia 9','dia 10', 'dia 11','dia 12']

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], Eixo_x, rotation=90)
plt.xlabel("Dias", fontsize=14, c= 'brown')
plt.ylabel("Quantidade de roupas vendidas", fontsize=14,c="pink")

plt.plot(func1, c='red', Label='Lucas')
plt.plot(func2, c='blue', Label='Maria')
plt.plot(func3, c= 'violet', Label='Joao')
plt.plot(func4, c= 'green', Label='Marta')
plt.legend()
plt.show()
