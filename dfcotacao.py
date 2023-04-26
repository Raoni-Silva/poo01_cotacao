import requests
import json
import pandas as pd
from datetime import datetime as dt
import auxiliar as aux

class Cotacao():
    def __init__(self):
        self.modulo = 'cotacao'
        self.api_cotacao = 'https://economia.awesomeapi.com.br/json/daily/'
        self.api_codigos = 'https://economia.awesomeapi.com.br/xml/available'
    # def s():       
    #     df = pd.DataFrame.from_dict(cotacoes)

    #     df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    #     df['dia'] = df['timestamp'].dt.day
    #     df['mes'] = df['timestamp'].dt.month
    #     df['ano'] = df['timestamp'].dt.year
    #     print(f'Rodando função: {funcao}')
    #     print(df.fillna(method="ffill"))

    def cotacaoDoDia(self, d0 = dt.strftime(dt.today(),r'%Y%m%d'), moeda='USD-BRL'):
        url = self.api + moeda + '/?start_date='+ d0 + '&end_date=' + d0
        x = aux.pooAux()
        df = x.getApi(url)     
        print(df)
        
    def codigoMoedas(self):
        response = requests.get(self.api_codigos)

        if response.status_code == 200:
            text = response.content
            print(pd.read_xml(text))
            
            # lines = text.splitlines()
            # for line in lines:
            #     print(line)
        else:
            print("Não foi possível obter o conteúdo")
        
        
       


    #def cotacaoDoDia(self,d0 = dt.strftime(dt.today(),r'%Y%m%d'), d1=None, moeda='USD-BRL'):
        # if d1 == None:
        #     d1 = d0
        #     url = self.api + moeda + '/?start_date='+ d0 + '&end_date='+ d1
        #     print(url)
        #     x = aux.pooAux()
        #     df = x.getApi(url)     
        #     print(df.fillna(method="ffill"))
        # else:
        #     # d1 = dt.strftime(d1,r'%Y%m%d')
        #     url = self.api + 'start_date='+ d0 + '&end_date='+ d1
        #     print(url)
        #     x = aux.pooAux()
        #     df = x.getApi(url)     
        #     print(df.fillna(method="ffill"))
            
