"""Uma professora deseja desenvolver um sistema para automatizarseu trabalho. Ela precisa criar uma solução onde seus alunos
consigam inserir suas notas (seja a média geral de todas as matérias ou a média de uma única disciplina), receber a média, e
saber sua situação (aprovação, reprovação ou recuperação)."""

def notas():
    aluno = input("Digite seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float
    media = (nota1+nota2+nota3)/3
    return media, aluno


def situacao(media, aluno):
    if (media <= 3) and (media < 5):
        print(f"{aluno.title()}, infelizmente você está de recuperação com média {media:.2f}. Se esforce para passar!")
    
    elif (media > 5):
        print(f"Parabéns {aluno.title()}, você foi aprovado (a) com média {media:.2f}!")

    else: 
        print(f"{aluno.title()}, infelizmente você foi reprovado (a) com média {media:.2f}.")


media,aluno = notas()
situacao(media, aluno)
