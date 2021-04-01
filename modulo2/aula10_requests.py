import requests

res = requests.get('https://scotch.io')

print(res)

if res:
    print('Response OK')
else:
    print('Response Failed')

print(res.status_code) #verificando o status
print(res.headers) #cabeçalhos
print(res.text) #dados de texto