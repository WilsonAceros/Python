#con las listas puedo agregar y borrar elementos
#Son mutables

n=[1,3,6,'hola',True]
print(n)
n.append(False)
print(n)
n.pop(3)
print(n)
n.remove(False)
print(n)

m=[5,6,'mundo']
print(n+m)

print(m*3)

#Con las tuplas no puedo agregar ni borrar elementos
#las tuplas son inmutables
#Ventaja: son mas rapidas de acceder

mi_tupla=(1,2,3,4,True)
mi_tupla

for elemento in n:
    print(elemento)