"""4. Realiza variaciones al programa anterior: cambia el orden
de los casos del switch, modifica la posición de algunos casos,
cambia el valor por defecto, explica qué pasa en cada caso por
medio de comentarios en el código."""
import datetime
#Captura la hora del sistema del
x= datetime.datetime.now()
print("Fecha y hora actual: ",x)
#Guardo en una tupla la hora y los minutos
hour=(x.hour, x.minute)
# hour=23,30
#Imprimo la hora actual
# print(hour)
def switch_hour(x):
    if (hour>=(6,0) and hour<=(11,59)):#Valida si esta en el horario de la mañana
        x=1
    elif (hour>=(12,0) and hour<=(17,59)):#Valida si esta en el horario de la tarde
        x=2
    elif (hour>=(18,0) and hour<=(21,59)):#Valida si esta en el horario de la noche
        x=3
    return {
        #Cambiando el orden en los casos del switch
    2: lambda: "Good afternoon",
    3: lambda: "Good evening",
    1: lambda: "Good morning",
    }.get(x,lambda: "Good night")#Valor por defecto

print(switch_hour(hour)())
