"""3.	Crea un programa que se llame Calculadora.py
y que calcule la suma, la resta, la multiplicación,
la división y la potencia cuadrada.
2. Edita el programa Calculadora.py, en el que agregue
opciones decorativas de menú y uses ASCII art. Recuerda
aplicar las secuencias de escape.
3. Agrega comentarios de línea y de párrafo, en los que
se expliquen las principales partes del programa."""
cadena1="{:>12} {:>3} {:>5} {:<1} {:>22} {:>4}"
cadena2="{:>12} {:>3} {:>5} {:<1} {:>21} {:>4}"
cadena3="{:>12} {:>3} {:>5} {:<1} {:>12} {:>4}"
cadena4="{:>12} {:>3} {:>5} {:<1} {:>18} {:>4}"
cadena5="{:>12} {:>3} {:>5} {:<1} {:>18} {:>4}"
print("             ________________________________________")
print("            /                                        \\")
print("           |    _________________________________     |")
print("           |   |                                 |    |")
print("           |   | C:\>\"Operación matemática\"      |    |")
print("           |   |                                 |    |")
print(cadena1.format("|","|","1.","Suma","|","|"))
print(cadena2.format("|","|","2.","Resta","|","|"))
print(cadena3.format("|","|","3.","Multiplicación","|","|"))
print(cadena4.format("|","|","4.","División","|","|"))
print(cadena5.format("|","|","5.","Potencia","|","|"))
print("           |   |                                 |    |")
print("           |   |                                 |    |")
print("           |   |                                 |    |")
print("           |   |_________________________________|    |")
print("           |                                          |")
print("            \_________________________________________/")
print("                   \___________________________/")
print("                _____________________________________")
print("             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_")
print("          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_")
print("       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
print("    _-'.-.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_")
def suma(a,b):#Funcion de suma
    return a+b
def resta(a,b):#Funcion de resta
    return a-b
def multiplicacion(a,b):#Funcion de multiplicación
    return a*b
def division(a,b):#Funcion de división
    return a/b
def potencia(a,b):#Funcion de potencia
    return a**b
#Estes dictionario permite llamar cada funcion de acuerdo a la selección del menú
switch_ope={
    '1': suma,
    '2': resta,
    '3': multiplicacion,
    '4': division,
    '5': potencia}
operacion=input("Elige una opción: ")
if operacion in ['1','2','3','4','5']:#Valida que sea una selección valida
    a=float(input("Ingresa un número: "))
    b=float(input("Ingresa otro número: "))
    if operacion=='4' and b==0.0:#Valida si se va dividir entre cero, para evitar el error
        print("No se puede dividir entre cero")
    else:
        #Obtiene el valor de acuerdo a la llave del diccionario, y porteriormente llama a la funcion
        resul=switch_ope.get(operacion)(a,b)
        #Formato al resultado
        cadena6="{:<2} {:.2f}"
        print(cadena6.format("El resultado es:",resul))
else:
    print("Escoge una opción valida")#Impirme un mensaje por elegir opcion no valida