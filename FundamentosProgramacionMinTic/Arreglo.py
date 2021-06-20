"""1.	Escribe un programa que permita leer un arreglo
de n datos enteros, luego imprime de manera invertida.
Guarde el archivo como Arreglo.py"""
#Solicita tamaño del arreglo
n=input("Numero de datos a leer: ")
dato=[]
#Ciclo para solicitar el numero de datos
for i in range(int(n)):
    d=input("Ingresa un dato: ")
    dato.append(d)#Agrega un dato al final de la lista
print(dato)
print(dato[::-1])#Imprimi la lista inversa