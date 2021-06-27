"""1. Realiza la implementación de la funcionalidad que permita
ingresar datos al usuario y seleccionar una operación a efectuar.
2. Operaciones disponibles para la calculadora: suma, resta,
multiplicación, logaritmo, coseno, seno, raíz cuadrada, convertir
decimal a binario y binario a decimal."""
import math

print("¿Que operación matemática vas a realizar?")
menu=["Suma", "Resta","Multiplicación","División","Potencia",
    "Logaritmo","Coseno","Seno","Raiz cuadrada",
    "Convertir decimal a binario","Convertir binario a decimal"]
#Mostrar el menu
for i in range(len(menu)):
    print(i+1,". ",menu[i])

global opcion #Variable global

opcion=int(input("Elige una opción: "))
#Funcion para pedir los numeros de ingreso para el respectivo calculo
def datos_entrada(opcion):
    if opcion in [1,2,3,4]:
        a=input("Digite un número: ")
        b=input("Digite un número: ")
        return a,b
    elif opcion==5:
        a=input("Base: ")
        b=input("Exponente: ")
        return a,b
    elif opcion==6:
        a=input("Digite un número: ")
        b=input("Digite la base: ")
        return a,b
    elif opcion in [7,8]:
        a=input("Digite un angulo ")
        return a
    elif opcion==9:
        a=input("Digite un número: ")
        return a
    elif opcion==10:
        a=input("Digite un numero decimal: ")
        return a
    elif opcion==11:
        a=input("Digite un numero binario: ")
        return a
    else:
        print("Elige una opcion correcta")

#Calcula la suma de dos numeros
def suma(opcion):
    print(menu[opcion-1])
    d=datos_entrada(opcion)
    return float(d[0])+float(d[1])
#Calcula la resta de dos numeros
def resta(opcion):
    print(menu[opcion-1])
    d=datos_entrada(opcion)
    return float(d[0])-float(d[1])
#Calcula la multiplicacion de dos numeros
def multiplicacion(opcion):
    print(menu[opcion-1])
    d=datos_entrada(opcion)
    return float(d[0])*float(d[1])
#Calcula la division de dos numeros
def division(opcion):
    print(menu[opcion-1])
    d=datos_entrada(opcion)
    try:
        return round(float(d[0])/float(d[1]),2)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
#Calcula la potencia basado en el base y el exponente
def potencia(opcion):
    print(menu[opcion-1])
    d=datos_entrada(opcion)
    return math.pow(float(d[0]),float(d[1]))
#Calcula el logaritmo basado en el numero y la base
def logaritmo(opcion):
    print(menu[opcion-1])
    d=datos_entrada(opcion)
    return math.log(float(d[0]),int(d[1]))
#Calcula el coseno de un angulo, en radianes
def coseno(opcion):
    print(menu[opcion-1])
    d=float(datos_entrada(opcion))
    return math.cos(math.radians(d))
#Calcula el seno de un angulo, en radianes
def seno(opcion):
    print(menu[opcion-1])
    d=float(datos_entrada(opcion))
    return math.sin(math.radians(d))
#Calcula la raiz cuadrada de un numero
def raiz(opcion):
    print(menu[opcion-1])
    d=float(datos_entrada(opcion))
    return math.sqrt(d)
#Convierte un decimal a un binario
def dec_bin(opcion):
    print(menu[opcion-1])
    d=int(datos_entrada(opcion))# este es el número que queremos convertir a binario

    modulos = [] # la lista para guardar los módulos

    while d != 0: # mientras el número de entrada sea diferente de cero
        # paso 1: dividimos entre 2
        modulo = d % 2
        cociente = d // 2
        modulos.append(str(modulo)) # guardamos el módulo calculado
        d = cociente # el cociente pasa a ser el número de entrada
        cadena="".join(modulos)
    return cadena
#Covierte binario a decimal
def bin_dec(opcion):
    print(menu[opcion-1])
    d=datos_entrada(opcion)
    numero_decimal = 0
    for posicion, digito_string in enumerate(d[::-1]):
    	numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal
#Diccionario que permite llamar la respectiva funcion
# basado en la clave ingresada por el usuario
switch_ope={
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: potencia,
    6: logaritmo,
    7: coseno,
    8: seno,
    9: raiz,
    10: dec_bin,
    11: bin_dec}
#Obtiene el valor del diccionario basado en la llave,
# posteriormente llama la funcion corresondiente
print(switch_ope.get(opcion)(opcion))