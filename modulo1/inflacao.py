print("****Bem-vindo à calculadora de inflação do kg do tomate****")

preco_ant = float(input("Qual era o preço do tomate há 1 ano? "))
preco_atual = float(input("Qual é o preço atual do kg do tomate? "))
dif = preco_atual-preco_ant
inf = (dif/preco_ant)*100

print(f"A diferença de preço do kg do tomate em um ano é de R$ {dif:.2f}.")
print(f"A inflação do kg do tomate em um ano é de {inf:.2f} %.")
