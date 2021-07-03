print("titulo")
print("NUEVA 1")
print("NUEVA 2")
# print("NUEVA 3")
print("NUEVA 4")
print("NUEVA 5")
# TODO: Falta agregar condicional

precio=56449.6689658
num=6
#el primer numero del formato es el indice correspondiente al orde de la variables
# la coma es la separacion de miles, el . y 3f corresponde a dejar tres digitos decimales
txt="El numero de boletas es {1}, el precio total es {0:,.3f} dolares"
print(txt.format(num,precio))

a,b,c=1,2,4
d=e=f=6
print(a,b,c,d)