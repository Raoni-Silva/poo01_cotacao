import requests
import json
import pandas as pd
from datetime import datetime as dt

class Cotacao():
    def __init__(self):
        self.modulo = 'cotacao'
        self.api = 'https://economia.awesomeapi.com.br/json/daily/:moeda?'

    def printCotacao(self):
        funcao = 'Print_Cotacao'
        cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
        cotacoes = cotacoes.json()
        df = pd.DataFrame.from_dict(cotacoes)

        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df['dia'] = df['timestamp'].dt.day
        df['mes'] = df['timestamp'].dt.month
        df['ano'] = df['timestamp'].dt.year
        print(f'Rodando função: {funcao}')
        print(df.fillna(method="ffill"))

    def cotacaoDoDia(self,d0 = dt.strftime(dt.today(),r'%Y%m%d')):
        x = self.api + 'start_date='+ d0 + '&end_date='+ d0
        print(x)

