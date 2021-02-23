temp = float(input("Digite sua temperatura corporal: "))
degree_sign = u"\N{DEGREE SIGN}"

if (temp > 37):
    print(f"Sinto muito, você está com febre de {temp:.1f} {degree_sign}C, melhor tomar um antitérmico!")
  
else:
    print("Você não está com febre, volte para casa!")