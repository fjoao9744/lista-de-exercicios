'''
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
print(1 ** 1)
print(1 ** (1 / 2))
'''

'''
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

print(f'{n1} + {n2} = {n1 + n2}')
print(f'{n1} - {n2} = {n1 - n2}')
print(f'{n1} * {n2} = {n1 * n2}')
print(f'{n1} / {n2} = {n1 / n2}')
print(f'{n1} ** {n2} = {n1 ** n2}')
print(f'√{n1}= {n1 ** (1 / 2)}')
print(f'√{n2}= {n2 ** (1 / 2)}')
'''

'''
import math

ns = [1, 1]

print(sum(ns)) #soma numeros de listas

print(math.pow(2, 3)) #2 elevado a 3

print(math.sqrt(9)) #faz raiz quadrada
'''


def soma(x, y):
    return x + y

def diminuir(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

def potencia(x, y):
    return x ** y

def raiz(x):
    return x ** (1 / 2)
