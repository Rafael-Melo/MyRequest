import requests

link = 'https://myapi--rafaelvilas2.repl.co/pegarvendas'

requisicao = requests.get(link)
print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas'])
