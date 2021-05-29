def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input('Ingresa un numero: '))
fibo=[]
if n>0:
    for i in range(n):
        fibo.append(fibonacci(i+1))
    print(fibo)
else:
    print('Ingresa un valor entero mayor a 0')