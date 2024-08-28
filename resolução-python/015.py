'''
n = int(input('Digite um numero: '))

if n > 0:
    print('seu numero é positivo. ')
elif n < 0:
    print('seu numero é negativo. ')
elif n == 0:
    print('seu numero é 0. ')
'''


def is_negative(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return 'negative'
    elif x == 0:
        return '0'
    
n = int(input('Digite um numero: '))
print(is_negative(n))
