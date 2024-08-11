'''

din = float(input('digite o valor a ser convertido? '))

dol = din * 0.18 # valor do dolar atualmente
euro = din * 0.17 # valor do euro atualmente

print(f"você tem {dol:.2f} dolares e {euro:.2f} euros") #arredondado

'''

import requests
import json

var = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

dolar = json.loads(var.content)

print(f"o {dolar['USDBRL']['name']} esta com a cotação de {dolar['USDBRL']['high']}")


