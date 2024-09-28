'''n = int(input("digite um numero: "))

primo = False

if n % 2 == 0:
    primo = False
elif n % 3 == 0:
    primo = False
elif n % 5 == 0:
    primo = False
elif n % 7 == 0:
    primo = False
else:
    primo = True
    
if n == 2 or n == 3 or n == 5 or n == 7:
    primo = True
    
    
if primo == True:
    print("seu numero é primo")
if primo == False:
    print("seu numero não é primo")
'''


def primo(n: int) -> None:
    if n in [2, 3, 5, 7]:
        print("Seu numero é primo!")

    else:
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
            print("Seu numero NÃO é primo!")
        else:
            print("Seu numero é primo!")


'''
num = int(input("Digite um numero: "))
primo(num)
'''

'''
for c in range(100):
    print(c, end=' ')
    primo(c)
'''