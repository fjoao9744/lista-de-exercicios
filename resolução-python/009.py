'''

din = float(input('digite o valor a ser convertido? '))

dol = din * 0.18 # valor do dolar atualmente
euro = din * 0.17 # valor do euro atualmente

print(f"você tem {dol:.2f} dolares e {euro:.2f} euros") #arredondado

'''

'''
#não é bem a mesma coisa mas isso é um teste de API
import requests
import json

var = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

dolar = json.loads(var.content)

print(f"o {dolar['USDBRL']['name']} esta com a cotação de {dolar['USDBRL']['high']}")

'''

import requests
import json

def dollar_convert(x):
    var = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    moeda = json.loads(var.content)
    
    dolar = moeda['USDBRL']['high']
    
    return x * float(dolar)

print('-' * 10, 'CONVERSOR DE REAL PARA DOLAR', '-' * 10)
n = int(input('quantos reais deseja converter: '))
print(f'o valor convertido fica: {dollar_convert(n)}')
