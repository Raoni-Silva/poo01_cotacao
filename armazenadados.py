import requests
import json
import pandas as pd
from datetime import datetime
from time import time

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/1')
cotacoes = cotacoes.json()

print(cotacoes[0]['name'])
print(cotacoes[0]['bid'])

data = cotacoes[0]['timestamp']
data = time()
data = (datetime.utcfromtimestamp(data).strftime('%Y-%m-%d'))
data = datetime.strptime(data, '%Y-%m-%d')
data_str = data.strftime('%Y-%m-%d')

print(data_str)