print("Bem vindo ao jogo de adivinhação!")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas): # enquanto ainda há tentativas disponíveis, execute o código novamente.
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   =  chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto!")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto!")
    print("Fim do jogo")
    
    rodada = rodada + 1