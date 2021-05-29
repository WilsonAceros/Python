import math

def area(r):
    return math.pi*r**2

if __name__=='__main__':
    r=int(input('Ingresa el radio de un circulo: '))
    a=area(r)
    print(f'El area del circulo es: {a}')