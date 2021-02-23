
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO SOBRE JEANNE VILLEPREUX-POWER \n \
    ENTRE COM O NÚMERO CORRESPONDENTE À ALTERNATIVA CORRETA")
pontos = 0
pergunta1 = int(input("Primeira pergunta: \n \
    Em quais países Jeanne Villepreux-Power viveu? \n \
        (1) Inglaterra \n \
        (2) Brasil \n \
        (3) França. \n "))

if pergunta1 == 1 or pergunta1 == 3:
    pontos = pontos + 1
    print(f"Você ganhou 1 ponto! Sua pontuação total é de {pontos} ponto (s).")
   
else: 
    pontos = pontos + 0
    print(f"Infelizmente você errou. Sua pontuação total é de {pontos} ponto (s).")


pergunta2 = int(input("Segunda pergunta: \n \
    Qual a grande contribuição de Jeanne Villepreux-Power para a ciência? \n \
        (1) Foi a primeira mulher a dar a volta ao mundo de barco. \n \
        (2) Foi a única mulher na Academia Gioeniana de Ciências Naturais em Catania, Itália. \n \
        (3) Criou os primeiros aquários de vidro, parecidos com os que conhecemos hoje. \n "))

if pergunta2 == 2 or pergunta2 == 3:
    pontos = pontos + 1
    print(f"Você ganhou 1 ponto! Sua pontuação total é de {pontos} ponto (s).")
   
else: 
    pontos = pontos + 0
    print(f"Infelizmente você errou. Sua pontuação total é de {pontos} ponto (s).")
    
pergunta3 = int(input("Terceira pergunta: \n \
    Qual foi sua descoberta que a tornou famosa? \n \
        (1) Descobriu por observação que a concha que recobre moluscos era por eles produzida, contrariando importantes naturalistas homens do período. \n \
        (2) Descobriu efeitos nocivos de pesticidas nos organismos. \n \
        (3) Descobriu como diversas espécies se reproduziam. \n "))

if pergunta3 == 1 or pergunta3 == 3:
    pontos = pontos + 1
    print("Você ganhou 1 ponto!")

else: 
    pontos = pontos + 0
    print(f"Infelizmente você errou. Sua pontuação total é de {pontos} ponto (s).")
      
print(f"Parabéns por ter chegado até o final do jogo! Você acertou {pontos} perguntas, sua pontuação é de {pontos} ponto (s). \n\
\n \
Conheça Jeanne Villepreux-Power: Nascida em uma pequena vila francesa no final do século XVIII, Jeanne Villepreux-Power era \
filha de um sapateiro e aprendeu o ofício de costureira para conseguir seu sustento. \n \
Desenvolveu seu interesse pela biodiversidade marinha, tornando-se uma naturalista autodidata. \
Para estudar a história natural de organismos marinhos, ela criou recipientes de vidro com fluídos \
onde poderia observá-los. Assim, Jeanne Villepreux-Power desenvolveu os primeiros aquários, \
o que lhe deu o título de “Mãe da Aquariofilia”. \n \
Foi nesses aquários que veio a descoberta que a tornou famosa: ao criar ovos de argonautas \
(moluscos do grupo dos polvos, mas que possuem conchas),  ela descobriu que a concha que recobre esses animais \
 era produzida por eles próprios, contrariando importantes naturalistas do período que apontavam que os argonautas deveriam \
ser como os ermitões (crustáceos) e utilizavam as conchas produzidas por outros animais. \
Além disso, foi a única mulher na Academia Gioeniana de Ciências Naturais em Catania, Itália. \n \
Em 1997, uma cratera em Vênus descoberta pela sonda Magalhães recebeu o nome dela.")