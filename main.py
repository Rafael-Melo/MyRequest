import requests

link = 'https://myapi--rafaelvilas2.repl.co/pegarvendas'

#GET de MyAPI
requisicao = requests.get(link)
print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas'])
