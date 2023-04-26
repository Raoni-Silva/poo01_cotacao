import sys
import requests
import json
import pandas as pd
import dfcotacao as dc
import auxiliar


if sys.argv[1] == 'cotacao': 
    dc.Cotacao().printCotacao()

if sys.argv[1] == 'cotacaoDia':
    if len(sys.argv) == 2:
        dc.Cotacao().cotacaoDoDia()
    # if len(sys.argv) == 3:
    #     d0 = sys.argv[2]
    #     dc.Cotacao().cotacaoDoDia(d0)
    # if len(sys.argv) == 4:
    #     d0 = sys.argv[2]
    #     d1 = sys.argv[3]
    #     dc.Cotacao().cotacaoDoDia(d0,d1)

if sys.argv[1] == 'codigosMoeda':
    dc.Cotacao().codigoMoedas()