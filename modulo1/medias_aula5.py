nota1 = float(input ("Digite sua nota de biologia: "))
nota2 = float(input ("Digite sua nota de matemática: "))
nota3 = float(input ("Digite sua nota de história: "))

media = (nota1+nota2+nota3)/3


if (media >= 6):
    print(f"Como sua nota foi {media:.1f}, você foi aprovado!")

else:
    print(f"Como sua nota foi {media:.1f}, você foi reprovado!")

