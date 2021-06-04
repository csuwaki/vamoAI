### Decorators (decoradores)
* São funções envolvem outras funções e aprimoram seu comportamento.
- São exemplos de _Higher Order Functions_.
- Possuem sintaxe própria, utilizando um "@" no início (Syntactic Sugar).
- Syntactic sugar é uma sintaxe que tem por finalidade tornar as construções mais fáceis de serem lidas e expressas.
- Uma construção na linguagem pode ser chamada de Syntactic Sugar se for removida sem causar nenhum efeito sobre a 
funcionalidade e o poder de expressividade do código.

#### Exemplo:
```python
 def seja_educado_mesmo(funcao): #Decorator Function
     def sendo_mesmo():
         print('Foi um prazer te conhecer!')
         funcao()
         print('Tenha um excelente dia!')
     return sendo_mesmo 

@seja_educado_mesmo #Decorator
  def apresentando():
    print('Meu nome é carol!')

 apresentando()

```

### Decorators com diferentes assinaturas

```python
def gritar(funcao): #Decorator Function
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar 

# -> PROBLEMA, SÓ RECEBE UM ARGUMENTO

@gritar #Decorator
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}!'

print(saudacao('Carol'))

```

> **Resolvendo o problema de receber apenas um argumento com Decorator Pattern**:

```
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar 

```

 > *args permite que você receba argumentos arbitrários, isto é, quantos quiser. 
 >
 >**Exemplo** (1,"a", 56, "não"). No formato de tuplas.
>
> **kwargs permite que você receba argumentos arbitrários em formato de keyword values, isto é, chave:valor. No formato de dict. 
>
> **Exemplo**: {música="Alive", filme="Cinderela"}

```python
@gritar #Decorator
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de pedir um {principal}, acompanhado de um {acompanhamento}.'

print(ordenar('sushi', 'missô'))
```