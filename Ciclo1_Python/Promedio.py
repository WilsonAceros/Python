"""2.	Crea un programa que se llame Promedio.py,
que pida 5 números, y calcula el promedio."""

x=int(input("Calcula del promedio de cuantos números: "))
sum=0
for i in range(x):
    a=float(input("Ingresa un numero: "))
    sum+=a
promedio=(sum/float(x))
print(promedio)
