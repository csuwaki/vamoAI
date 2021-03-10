"""
len(dict) = tamanho
get(chave) — retorna o valor associado a chave;
items() — retorna uma lista de tuplas, onde cada tupla é composta de uma chave e valor do dicionário;
keys() — retorna uma lista com todas as chaves do dicionário;
values() — retorna uma lista com todos os valores do dicionário;
pop(chave) — retorna e remove o valor associado a chave;
popitem() — retorna e remove um elemento aleatório do dicionário."""

#Estentendo o dicionário: Inserção de um de par (chave e valor) utilizando o operador [].
series = {}
series["titulo"] = "breaking bad"
series["ano_inicio"] = 2008
series["ano_final"] = 2013

#Inserção de outro dicionário utilizando o comando update(<dicionário>):
outros_dados = {"emissora": "AXN", "país": "eua"}

series.update(outros_dados)
print(series)

#para mostrar as chaves
for key in series.keys():
    print(key)

#para mostrar os valores
for valor in series.values():
    print(valor)

#para mostrar chave e valor
for key, valor in series.items():
    print(f"{key} = {valor}")

#retornano um valor associado à chave.
print(series.get("titulo"))

#para remover um item.
print(series.pop('emissora'))
print(series)


