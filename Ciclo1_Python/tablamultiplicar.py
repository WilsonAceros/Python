num=int(input("Ingrese un numero: "))
for x in range(11):
    cadena="{} x {} = {}"
    print(cadena.format(num,x,num*x))