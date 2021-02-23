
print("*BEM VINDO À CALCULADORA DE MENOR PREÇO*")
produto1_nome = input("Digite o nome do primeiro produto: ")
produto1_preco = float(input("Digite o preço do primeiro produto: "))
produto2_nome = input("Digite o nome do segundo produto: ")
produto2_preco = float(input("Digite o preço do segundo produto: "))
produto3_nome = input("Digite o nome do terceiro produto: ")
produto3_preco = float(input("Digite o preço do terceiro produto: "))

if produto1_preco < produto2_preco and produto1_preco < produto3_preco:
    print(f"O produto de menor valor é {produto1_nome}, que custa R${produto1_preco:.2f}.")

elif produto2_preco < produto1_preco and produto2_preco < produto3_preco:
    print(f"O produto de menor valor é {produto2_nome}, que custa R${produto2_preco:.2f}.")

else:
   print(f"O produto de menor valor é {produto3_nome}, que custa R${produto3_preco:.2f}.") 