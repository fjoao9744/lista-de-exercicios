'''
n = int(input())
print('o antecessor de {} é {} e o sucessor é {}'.format(n, n - 1, n + 1))
'''
'''
n = int(input())

ant = n - 1
suc = n + 1

print(f'o antecessor de {n} é {ant} e o sucessor é {suc}')
'''

def ant(x):
    return x - 1
def suc(x):
    return x + 1

n = int(input())
print(f'o sucessor de {n} é {ant(n)} e o sucessor é {suc(n)}')

