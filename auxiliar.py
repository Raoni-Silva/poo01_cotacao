import requests
import json
import pandas as pd
from datetime import datetime as dt
import warnings

class pooAux():
    def __init__(self):
        pass

    def getApi(self, url):
        cotacoes = requests.get(url)
        print(cotacoes)
        cotacoes = cotacoes.json()
        df = pd.DataFrame.from_dict(cotacoes)
        return df
        