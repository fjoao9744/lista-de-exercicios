'''n = int(input("digite um numero para vermos sua tabuada"))

print(f"""{n} x 1 = {n * 1}
{n} x 2 = {n * 2}
{n} x 3 = {n * 3}
{n} x 4 = {n * 4}
{n} x 5 = {n * 5}
{n} x 6 = {n * 6}
{n} x 7 = {n * 7}
{n} x 8 = {n * 8}
{n} x 9 = {n * 9}
{n} x 10 = {n * 10}
""")
'''

'''
n = int(input("digite um numero para vermos sua tabuada"))

for c in range(1, 10 + 1):
    print(f'{n} x {c} = {n * c}')
'''

'''
n = int(input('digite algum numero para vermos sua tabuada: '))

cont = 0

while True:
    cont += 1
    print(f'{n} x {cont} = {n * cont}')
    if cont == 10:
        break
'''

'''
n = int(input('digite algum numero para vermos sua tabuada: '))

cont = 0
while cont < 10:
    cont += 1
    print(f'{n} x {cont} = {n * cont}')
'''

def tabuada(x):
    for c in range(1, 10 + 1):
        print(f'{x} x {c} = {x * c}')

n = int(input('digite algum numero para vermos sua tabuada: '))

tabuada(n)
