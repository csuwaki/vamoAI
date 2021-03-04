numero_da_sorte = 30
chute = int(input("Adivinhe o número da sorte: "))

while chute != numero_da_sorte:
    chute = int(input("Você não acertou! Tente novamente: "))
print("Você acertou! Fim de jogo.")
