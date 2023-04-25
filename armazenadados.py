import requests
import json
import pandas as pd
from datetime import datetime
from time import time

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/1')
cotacoes = cotacoes.json()

nome = cotacoes[0]['name']
cotacao = cotacoes[0]['bid']

data = cotacoes[0]['timestamp']
data = time()
data = (datetime.utcfromtimestamp(data).strftime('%Y-%m-%d'))
data = datetime.strptime(data, '%Y-%m-%d')
data_str = data.strftime('%Y-%m-%d')
data = data_str

lista = []
lista.append({'nome': nome, 'cotacao': cotacao, 'data': data}) 

df = pd.DataFrame.from_dict(lista)
print(df)


