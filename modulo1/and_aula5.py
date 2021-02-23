print("Bem-vindo ao supermercado.")

mascara = True
alcool_gel = True
temperatura = float(input("Digite sua temperatura: "))

if (mascara == True) and (alcool_gel == True) and (temperatura < 37):
    print("Pode entrar no estabelecimento.")
elif(mascara == False) and (alcool_gel == True) and (temperatura < 37): 
    print("Coloque sua máscara para entrar no estabelecimento.") 
elif(mascara == True) and (alcool_gel == False) and (temperatura < 37):
    print("Passe álcool em gel nas mãos para entrar no estabelecimento.")
else:
    print("Volte para casa e procure um médico, pois vocêe stá febril.")