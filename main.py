import requests

link = 'https://myapi--rafaelvilas2.repl.co/pegarvendas'

#Comando GET
requisicao = requests.get(link)
print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas'])
