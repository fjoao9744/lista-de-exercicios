'''
n = input('digite seu nome completo: ').strip()

print(f'seu primeiro nome é {n.split()[0]}')
print(f'a primeira letra do seu nome é {n[0]}')
print(f'seu nome todo em maiusculo é {n.upper()}')
print(f'e seu nome tem {len(n)} caracteres')
'''
def primeiro_nome(x):
    return str(x).split()[0]

n = input('digite seu nome completo: ').strip()

print(f'seu primeiro nome é {primeiro_nome(n)}')
print(f'a primeira letra do seu nome é {n[0]}')
print(f'seu nome todo em maiusculo é {n.upper()}')
print(f'e seu nome tem {len(n)} caracteres')

#obs: pra que criar funções que ja existem?


