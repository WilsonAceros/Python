"""4. Realiza el diseño de un programa que salude según la hora del día e
incluye el pseudocódigo y el diagrama de flujo.
5. Realiza la prueba de escritorio del programa, luego escribe el programa
en un archivo con nombre saludo.py ejecute y pruebe el programa."""

import datetime
#Captura la hora del sistema del
x= datetime.datetime.now()
print("Fecha y hora actual: ",x)
#Guardo en una tupla la hora y los minutos
hour=(x.hour, x.minute)
#Imprimo la hora actual
print(hour)

if hour>=(6,0) and hour<=(11,59):#Condicional para validar si es de mañana
    print("Good morning")
elif hour>=(12,0) and hour<=(17,59):#Valida si es de tarde
    print("Good afternoon")
elif hour>=(18,0) and hour<=(21,59):#Valida que es de tarde noche
    print("Good evening")
else:#Valida que es de noche hour>=(22,0) and hour<=(5,59)
    print("Good night")