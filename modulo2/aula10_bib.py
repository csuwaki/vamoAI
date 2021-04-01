import statistics

calcados = [36,38,39,38,37,35,33,40,41,42,36,36,37,39,38,36,36]
mais_vendido = statistics.mode(calcados)

print(f"Calçados com numeração {mais_vendido} foram os mais vendidos hoje.")