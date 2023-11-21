a = int(input("ingresa un numero: "))
b = int(input("ingresa un numero: "))
c = int(input("ingresa un digito: "))

def suma(a,b,c):
    sum = a + b + c
    print(sum)

def resta(a,c):
    res = a + b + c
    print(res)

def producto(a,b):
    prod = a * b
    print(prod)   

def potencia(a,b):
    pot = a ** b  
    print(pot)

def ecuacion1(a,b):
    ecua1 = a**2*2*a*b-b**3
    print(ecua1)

def ecuacion2(a,b):
    ecua2 = b**3*3*a*b-a**3
    print(ecua2) 

def ecuacion3(a,b):
    ecua3 = ((a-b)/b**3-a**3)-(a**2)+(b**3)  
    print(ecua3)

def ecuacion4(b,d):
    ecua4 = (b+d*(b**2-d**2))   