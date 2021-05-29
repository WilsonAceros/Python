
def resultado(n):
    return n+(n*n)+(n*n)*n

if __name__=='__main__':
    n=int(input('Ingresa un numero entero: '))
    res=resultado(n)
    print(f'El resultado es {res}')