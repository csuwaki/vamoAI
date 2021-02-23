
def nome():
    nome = input("Digite seu nome: ")
    return nome 

def media(nota_port, nota_mat, nota_bio):
    return (nota_port + nota_mat + nota_bio)/3

aluno = nome()
nota_final = media(5, 3, 7)
print(f'Olá {aluno.title()}, sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(8, 10, 10)
print(f'Olá {aluno.title()}, sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(10, 3, 6)
print(f'Olá {aluno.title()}, sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(5, 4, 1)
print(f'Olá {aluno.title()}, sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(5, 2, 10)
print(f'Olá {aluno.title()}, sua média é {nota_final:.2f}.')