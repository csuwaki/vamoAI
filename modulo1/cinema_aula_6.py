nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
entrada_padrao = 35
entrada_vip = 60
maioridade = (18-idade)

if idade < 18:
    print(f"{nome.title()}, você é menor de idade, por isso não poderá adquirir ingressos. Ainda faltam {maioridade} anos para você poder entrar no clube.")

else:
    entrada = int(input(f"Qual tipo entrada você gostaria de reservar? Se você for estudante de python, terá direito à meia-entrada.\n \
    A entrada padrão inteira custa R${entrada_padrao}, digite 1 para confirmar sua compra. \n \
    A entrada VIP inteira custa R${entrada_vip}, digite 2 para confirmar sua compra. " )) 
    py_std = input("Você é estudante de python? Estudantes pagam meia entrada. Responda com sim ou não. ")
    
    if entrada == 1 and py_std.lower() == "sim":
        valor = entrada_padrao/2
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso padrão no valor de R${valor} foi confirmada!")
    elif entrada == 1 and py_std.lower() == "não":
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso padrão no valor de R${entrada_padrao} foi confirmada!")
    elif entrada == 2 and py_std.lower() == "sim":
        valor = entrada_vip/2
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso VIP no valor de R${valor} foi confirmada!")
    else:
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso VIP no valor de R${entrada_vip} foi confirmada!")
