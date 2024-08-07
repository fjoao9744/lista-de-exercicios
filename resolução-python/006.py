'''
n1 = int(input())
n2 = int(input())

print(n1 + n2 / 2)
'''

'''
nota1 = int(input('digite a primeira nota: '))
nota2 = int(input('digite a segunda nota: '))

media = nota1 + nota2 // 2
print(f'a media entre as duas notas é de: {media}')
'''

def media(x, y):
    return x + y // 2

nota1 = int(input('digite a primeira nota: '))
nota2 = int(input('digite a segunda nota: '))

print(f'a media entre os dois numeros é de {media(nota1, nota2)}')

