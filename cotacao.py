import requests
import json
from datetime import datetime
from time import time;
import pandas as pd

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes = cotacoes.json()

df = pd.DataFrame.from_dict(cotacoes)
print(df.head())

# def timestampConvert(x):
#     data = x
#     data = time()
#     data = (datetime.utcfromtimestamp(data).strftime('%Y-%m-%d'))
#     data = datetime.strptime(data, '%Y-%m-%d')
#     return data

# p = 1

# cotacao = cotacoes[0]['timestamp']
# cotacao = time()

# df = pd.DataFrame.from_dict(cotacoes)

# df = df.apply(lambda x:timestampConvert(x))

# df = df[df[cotacao]].apply

# print(df.head())



