"""3. Reescribe el programa Saludar.py, usando la estructura condicional switch.
Guarde el archivo como SuperSaludo.py.
"""
import datetime
#Captura la hora del sistema del
x= datetime.datetime.now()
print("Fecha y hora actual: ",x)
#Guardo en una tupla la hora y los minutos
hour=(x.hour, x.minute)
#Imprimo la hora actual
# print(hour)
def switch_hour(x):
    if (hour>=(6,0) and hour<=(11,59)):#Valida si esta en el horario de la mañana
        x=1
    elif (hour>=(12,0) and hour<=(17,59)):#Valida si esta en el horario de la tarde
        x=2
    elif (hour>=(18,0) and hour<=(21,59)):#Valida si esta en el horario de la tarde noche
        x=3
    elif (hour>=(22,0) and hour<=(23,59)):#Valida si esta en el horario de la noche
        x=4
    else:
        print("Fuera rango horario")
    return {
    1: lambda: "Good morning",
    2: lambda: "Good afternoon",
    3: lambda: "Good evening",
    4: lambda: "Good night"
    }.get(x, lambda: None)#Valor por defecto fuera de rango

print(switch_hour(hour)())
