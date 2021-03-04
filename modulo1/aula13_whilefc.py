def pergunta():
    pergunta = input("\n\
Qual das palavras não faz parte do grupo? \n\
1. garrafa \n\
2. corrida \n\
3. carro \n\
4. berro \n\
5. colher \n")
    while True:
        if pergunta.title() == "Colher":
            print("Acertou!")
            break
        else: 
            pergunta = input("\n\
Incorreto! Qual das palavras não faz parte do grupo? \n\
1. garrafa \n\
2. corrida \n\
3. carro \n\
4. berro \n\
5. colher \n")


pergunta()
    


    


