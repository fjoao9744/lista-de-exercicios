'''
n = float(input('digite um numero para arredondar-mos: '))

print(f'seu numero arrendondado ficou: {int(n)}')
'''

'''
n = float(input('digite um numero para arredondar-mos: '))

print(f'seu numero arrendondado ficou: {n:.0f}')
'''

from math import trunc

n = float(input('digite um numero para arredondar-mos: '))

print(f'seu numero arrendondado ficou: {trunc(n)}')
