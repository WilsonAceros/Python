"""3.	Crea un programa que se llame Calculadora.py
y que calcule la suma, la resta, la multiplicación,
la división y la potencia cuadrada."""
print("¿Que operación matemática vas a realizar?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
operacion=int(input("Elige una opción: "))
a=float(input("Ingresa un número: "))
b=float(input("Ingresa otro número: "))
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
def potencia(a,b):
    return a**b
switch_ope={
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: potencia}
print(switch_ope.get(operacion)(a,b))