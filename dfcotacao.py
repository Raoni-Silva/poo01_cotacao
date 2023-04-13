import requests
import json
import pandas as pd
from datetime import datetime as dt
import auxiliar as aux

class Cotacao():
    def __init__(self):
        self.modulo = 'cotacao'
        self.api = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/?'

    def s():       
        df = pd.DataFrame.from_dict(cotacoes)

        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df['dia'] = df['timestamp'].dt.day
        df['mes'] = df['timestamp'].dt.month
        df['ano'] = df['timestamp'].dt.year
        print(f'Rodando função: {funcao}')
        print(df.fillna(method="ffill"))

    def cotacaoDoDia(self,d0 = dt.strftime(dt.today(),r'%Y%m%d'), d1=None):
        if d1 == None:
            url = self.api + 'start_date='+ d0 + '&end_date='+ d0
            x = aux.pooAux()
            df = x.getApi(url)     
            print(df.fillna(method="ffill"))
        else:
            # d1 = dt.strftime(d1,r'%Y%m%d')
            url = self.api + 'start_date='+ d0 + '&end_date='+ d1
            print(url)
            x = aux.pooAux()
            df = x.getApi(url)     
            print(df.fillna(method="ffill"))
            
