'''
n = int(input('Qual é o seu salario?'))

imposto = n * 10 // 100

print(f'você terá que pagar {imposto} de imposto')
'''

'''
n = int(input('Qual é o seu salario?'))

if n <= 2100:
    imposto = 0

if n >= 2100:
    imposto = n * 7 // 100
    
if n >= 2800:
    imposto = n * 15 // 100
    
if n >= 3700:
    imposto = n * 22 // 100
    
if n >= 4600:
    imposto = n * 27 // 100

print(f'você terá que pagar {imposto} reais de imposto de renda')
'''

'''
n = int(input('Qual é o seu salario?'))

if n < 2100:
    imposto = 0

elif n >= 2100 and n <= 2800:
    imposto = n * 0.07
    
elif n >= 2800 and n <= 3700:
    imposto = n * 0.15
    
elif n >= 3700 and n <= 4600:
    imposto = n * 0.22
    
elif n > 4600:
    imposto = n * 0.27

print(f'você terá que pagar R${imposto} reais de imposto de renda')
'''

def imposto_renda(n):
    if n < 2100:
        imposto = 0

    elif n >= 2100 and n <= 2800:
        imposto = n * 0.07
        
    elif n >= 2800 and n <= 3700:
        imposto = n * 0.15
        
    elif n >= 3700 and n <= 4600:
        imposto = n * 0.22
        
    elif n > 4600:
        imposto = n * 0.27
        
    return imposto

n = imposto_renda(int(input('Qual é o seu salario?')))
    
print(f'você terá que pagar R${n:.2f} reais de imposto de renda')