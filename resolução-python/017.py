n = int(input("digite um numero: "))

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
