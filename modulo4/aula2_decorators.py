"""
Decorators (decoradores)
- São funções envolvem outras funções e aprimoram seu comportamento.
- São exemplos de Higher Order Functions.
- Possuem sintaxe própria, utilizando um "@" (Syntactic Sugar).
- Syntactic sugar é uma sintaxe que tem por finalidade tornar as construções mais fáceis de serem lidas e expressas.
- Uma construção na linguagem pode ser chamada de Syntactic Sugar se for removida sem causar nenhum efeito sobre a 
funcionalidade e o poder de expressividade do código; 

"""

# def seja_educado_mesmo(funcao):
#     def sendo_mesmo():
#         print('Foi um prazer te conhecer!')
#         funcao()
#         print('Tenha um excelente dia!')
#     return sendo_mesmo 

# @seja_educado_mesmo
# def apresentando():
#     print('Meu nome é carol!')

# apresentando()



##### DECORATORS COM DIFERENTES ASSINATURAS #####

# def gritar(funcao):
#     def aumentar(nome):
#         return funcao(nome).upper()
#     return aumentar 
# -> PROBLEMA, SÓ RECEBE UM ARGUMENTO

# @gritar
# def saudacao(nome):
#     return f'Olá, eu sou o/a {nome}!'

# print(saudacao('Carol'))


# RESOLVENDO O PROBLEMA DE RECEBER APENAS UM ARGUMENTO COM DECORATOR PATTERN:

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar 

#### args permite que você receba argumentos arbitrarios, isto é, quantos quiser. Exemplo (1,"a", 56, "não") Tupla
#### kwars permite que você receba argumentos arbitrarios em formato de keyword values, isto é, chave=valor. Dict
#### Exemplo: {música="Alive", filme="Cinderela"}

@gritar 
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de pedir um {principal}, acompanhado de um {acompanhamento}.'

print(ordenar('sushi', 'missô'))