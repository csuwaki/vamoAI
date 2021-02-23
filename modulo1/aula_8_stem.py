def dif_idade():
    idade1 = int(input("Entre com seu ano de nascimento: "))
    idade2 = 1794
    dif_idade = (idade1-1794)
    return dif_idade

def cidade_de_nascimento():
    cidade_de_nascimento = input("Digite a cidade que você nasceu: ").title()
    return cidade_de_nascimento

def pais_de_nascimento():
    pais_de_nascimento = input("Digite o país que você nasceu: ").title()
    return pais_de_nascimento

country = pais_de_nascimento()
city = cidade_de_nascimento()
diferenca = dif_idade()

if city == "Paris" and country != "França": 
    print("Você e Jeanne Villepreux-Power nasceram na mesma cidade, mas não no mesmo país.")
elif city == "Paris" and country == "França": 
    print("Você e Jeanne Villepreux-Power nasceram na mesma cidade e no mesmo país.")
elif city != "Paris" and country == "França":
    print("Você e Jeanne Villepreux-Power nasceram na mesma cidade, mas não no mesmo país.")
else:
    print("Você e Jeanne Villepreux-Power não nasceram na mesma cidade (Paris) e nem no mesmo país (França).")

print(f"Você e Jeanne Villepreux-Power possuem {diferenca} anos de diferença de idade.")

