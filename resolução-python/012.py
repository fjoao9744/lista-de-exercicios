
n = int(input('quantos km/h você rodou? '))

if n >= 80:
    multa = 100
    n -= 80
    if n >= 0:
        multa += 0.20 * n
        
    print(f'você pagará {multa} reais de multa')

elif n < 80:
    print('tudo bem por aqui tenha um bom dia! ')

    
km = int(input('quantos km/h você rodou? '))

def multa(x):
    n = x
    multa = 0
    add = 0
    
    if n >= 80:
        multa += 100
        n -= 80
    
    parar = False
    
    
    while parar == False:
        
        if n > 0:
            add += 0.20
            
        n -= 1
        
        
        if n <= 0:
            parar = True
        
    
    multa += add
    
    return float(multa)

multa = multa(km)

if multa > 0:
    print(f'você pagará R${km:.2f} reais de multa')
else:
    print('tenha um bom dia! ')