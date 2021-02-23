#Pergunte a pessoa usuária o nome, a idade e se ela é estudante de Python;
#Permita apenas pessoas usuárias maiores de 18 anos reservarem um ingresso para um clube
#de festas;
#Permita a pessoa usuária escolher entre a entrada padrão, que custa R$ 35,00 e a VIP, que
#custa R$ 60,00;
#Conceda um desconto de 50% aos estudantes de Python; Se houver menores de idade,
#imprima quantos anos faltam para a pessoa usuária ter 18 anos e, consequentemente, ter
#acesso ao clube.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
py_std = input("Você estuda python? Responda com sim ou não. ")
entrada1 = 35
entrada2 = 60
meia_entrada1 = entrada1/2
meia_entrada2 = entrada2/2
maioridade = (18-idade)


if idade >= 18 and py_std.lower() == "não":
    print("Você pode reservar o ingresso para o clube VAMO AI. ")

    entrada_inteira = int(input(f"Qual tipo de entrada você gostaria de reservar? \n \
    Para entrada padrão (R${entrada1}), digite 1. \n \
    Para entrada VIP (R${entrada2}), digite 2. "))
    if entrada_inteira == 1:
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso padrão foi confirmada!")
    else:
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso VIP foi confirmada!")


elif idade >= 18 and py_std.lower() == "sim":
    print("Como estudante de python, você tem direito à meia-entrada. ")
   
    entrada_meia = int(input(f"Qual tipo entrada você gostaria de reservar? \n \
    Para entrada padrão (R${meia_entrada1}), digite 1. \n \
    Para entrada VIP (R${meia_entrada2}), digite 2. " )) 
    if entrada_meia == 1:
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso padrão foi confirmada!")
    else:
        print(f"Obrigada pela compra, {nome.title()}! Sua reserva de ingresso VIP foi confirmada!")

else:
    print(f"{nome.title()}, você é menor de idade, por isso não poderá adquirir ingressos. Ainda faltam {maioridade} anos para você poder entrar no clube.")




