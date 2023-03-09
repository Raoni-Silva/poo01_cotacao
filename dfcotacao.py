import requests
import json
import pandas as pd


cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes = cotacoes.json()
df = pd.DataFrame.from_dict(cotacoes)
print(df.fillna(method="ffill"))