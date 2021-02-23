def nome():
    nome = input("Digite seu nome: ")
    return nome 

def resposta(exame):
    name = nome()
    if exame >=7 and exame <=10:
        print(f"Olá {name}. Seu resultado de exame está bom. Continue assim.")

    elif exame >= 4 and exame <= 6:
        print(f"Olá {name}. Seu resultado de exame está médio. Busque se cuidar mais e fazer acompanhamento médico.")
    
    else:
        print(f"Olá {name}. Seu resultado está ruim. Procure a equipe médica.")

resposta(8)
resposta(4)
resposta(2)
