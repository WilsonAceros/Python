x=int(input('Digita un numero: '))
y=int(input('Digita otro numero: '))

def suma(a,b):
    """ Suma dos valores a y b
    
    param int a cualquier entero
    param int b cualquier entero
    retorna la suma de a y b
    """
    total=a+b 
    return total 

z=suma(x,y)
print(f'La suma es {z}')

help(suma)