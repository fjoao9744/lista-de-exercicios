'''
n = int(input('fale um numero: '))

if n % 2 == 0:
    print('seu numero é par')

else:
    print('seu numero é impar')
'''
'''
n = int(input('fala um numero: '))

ver = n % 2
par = False

match ver:
    case 0:
        par = True
    case 1:
        pass

print('Seu numero é par!' if par == True else 'Seu numero é impar!')
'''
'''
print("seu numero é par!" if (int(input("digite um numero: ")) % 2) == 0 else "seu numero é impar")
'''

def par(x):
    if x % 2 == 0:
        print("par")
    else:
        print("impar")

par(7)