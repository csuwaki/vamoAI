def inserir_valor(valor_a,valor_b):
    if (valor_b >=1) and (valor_b <=50) and (valor_b >=1) and (valor_a <=50):
        mult = valor_b*valor_a
        print(f"O resultado da multiplicação é {mult}.")
    else:
        print("Valores não válidos. Você deve inserir um número entre 1 e 50.")


inserir_valor(7,5)
inserir_valor(90,100)
inserir_valor(2,3)
