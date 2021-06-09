import matplotlib.pyplot as plt
import numpy as np
import statistics

plt.figure(figsize=[15, 10])

grupos = 5
luana = [4,7,12,5,3]
adoniran = [2,8,9,3,12]
marcela = [7,2,10,3,11]
joana = [12,4,11,8,14]
cristina = [3,6,8,10,2]
dia = ['Dia 26', 'Dia 27', "Dia 28", 'Dia 29', 'Dia 30']
bar_width = 0.17

y = np.arange(grupos)

# Para criar barras horizontais, adicionar h ao 'bar'.
plt.barh(y, luana, bar_width, label = "Luana", color = 'purple')
plt.barh(y + bar_width,  adoniran, bar_width, label = "Adoniran", color = 'salmon')
plt.barh(y + bar_width*2, marcela, bar_width, label = "Marcela", color = 'slateblue')
plt.barh(y + bar_width*3 ,joana, bar_width, label = "Joana", color = 'y')
plt.barh(y + bar_width*4, cristina, bar_width, label = "Cristina", color = 'lightseagreen')

# Criando a legenda
plt.legend()

# Nomeando eixos y e x
plt.xlabel('Total de peças vendidas')
plt.ylabel('Dia do mês')

# Criando o título
plt.title('Vendas por funcionário')
plt.yticks(y+ bar_width, dia)

# Salvando como png
plt.savefig('2BarPlot.png')

# Mostrando o plot
plt.show()


#Qual a média de vendas diária de cada funcionário da loja?
media = print(f'Média de vendas diária: Luana = {statistics.mean(luana)},  Adoniran = {statistics.mean(adoniran)}, \
Marcela = {statistics.mean(marcela)}, Joana = {statistics.mean(joana)}, Cristina = {statistics.mean(cristina)}')

#Qual é a moda de cada funcionário?
moda = print(f'Moda: Luana = {statistics.mode(luana)},  Adoniran = {statistics.mode(adoniran)}, \
Marcela = {statistics.mode(marcela)}, Joana = {statistics.mode(joana)}, Cristina = {statistics.mode(cristina)}')

#E a mediana?
mediana = print(f'Mediana: Luana = {statistics.median(luana)},  Adoniran = {statistics.median(adoniran)}, \
Marcela = {statistics.median(marcela)}, Joana = {statistics.median(joana)}, Cristina = {statistics.median(cristina)}')
