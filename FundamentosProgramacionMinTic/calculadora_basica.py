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

for i in range(len(menu)):
    print(i+1,". ",menu[i])

opcion=int(input("Elige una opción: "))

def datos_entrada():
    a=float(input("Digite un número: "))
    b=float(input("Digite un número: "))
    return a,b

def datos_entrada2():
    a=float(input("Digite un numero: "))
    return a

def datos_entrada3():
    a=input("Digite un numero: ")
    return a

def suma(opcion):
    print(menu[opcion-1])
    d=datos_entrada()
    return d[0]+d[1]

def resta(opcion):
    print(menu[opcion-1])
    d=datos_entrada()
    return d[0]-d[1]

def multiplicacion(opcion):
    print(menu[opcion-1])
    d=datos_entrada()
    return d[0]*d[1]

def division(opcion):
    print(menu[opcion-1])
    d=datos_entrada()
    try:
        return d[0]/d[1]
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

def potencia(opcion):
    print(menu[opcion-1])
    d=datos_entrada()
    return math.pow(d[0],d[1])

def logaritmo(opcion):
    print(menu[opcion-1])
    d=datos_entrada2()
    return math.log(d)

def coseno(opcion):
    print(menu[opcion-1])
    d=datos_entrada2()
    return math.cos(math.radians(d))

def seno(opcion):
    print(menu[opcion-1])
    d=datos_entrada2()
    return math.sin(math.radians(d))

def raiz(opcion):
    print(menu[opcion-1])
    d=datos_entrada2()
    return math.sqrt(d)

def dec_bin(opcion):
    print(menu[opcion-1])
    d=int(datos_entrada3())# este es el número que queremos convertir a binario

    modulos = [] # la lista para guardar los módulos

    while d != 0: # mientras el número de entrada sea diferente de cero
        # paso 1: dividimos entre 2
        modulo = d % 2
        cociente = d // 2
        modulos.append(str(modulo)) # guardamos el módulo calculado
        d = cociente # el cociente pasa a ser el número de entrada
        cadena="".join(modulos)
    return cadena

def bin_dec(opcion):
    print(menu[opcion-1])
    d=datos_entrada3()
    numero_decimal = 0
    for posicion, digito_string in enumerate(d[::-1]):
    	numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal

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
print(switch_ope.get(opcion)(opcion))