def factorial(n):
    """
    Calcula el factorial de n
    
    n int >0
    returnt n!
    
    """
    print(n)
    if n==1:
        return 1
    return n*factorial(n-1)

n=int(input('Ingresa un numero: '))
 
print(factorial(n))