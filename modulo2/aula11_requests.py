import requests
requisicao = requests.options('https://www.coindesk.com/coindesk-api')
print(requisicao.status_code)