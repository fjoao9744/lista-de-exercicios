'''
n = input('digite seu nome completo: ').split()
print(f'seu primeiro nome é {n[0]} e o ultimo é {n[-1]}')
'''

'''
nome = str(input('digite seu nome completo: ')).strip().split()
print(f'seu primeiro nome é {n[0]} e o ultimo é {n[-1]}')
'''

def primeira_palavra(palavra_completa): #recebe uma string
    palavra = palavra_completa.strip().split() #limpando e separando a string
    return palavra[0]
def ultima_palavra(palavra_completa): #recebe uma string
    palavra = palavra_completa.strip().split() #limpando e separando a string
    return palavra[-1]

nome = str(input('digite seu nome completo: '))
print(f'seu primeiro nome é {primeira_palavra(nome)} e o seu ultimo é {ultima_palavra(nome)}')  
    