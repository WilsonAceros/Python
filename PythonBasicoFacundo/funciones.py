"""def imprimir_mensaje():
    print("Mensaje especial 1: ")
    print("Estoy aprendiendo a usar funciones:")
    
imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()"""

opcion=int(input("Elige una opcion (1,2,3): "))

def conversacion(mensaje):
    print("Hola")
    print("Como estas")
    print(mensaje)
    print("Adios")
if opcion==1:
    conversacion("Elegiste la opcion 1")
elif opcion==2:
    conversacion("Elegiste la opcion 2")
elif opcion==3:
    conversacion("Elegiste la opcion 3")
else: 
    print("Elige una opcion correcta")
    
def suma(a,b):
    print("Se suman dos numeros")
    resultado=a+b
    return resultado

sumatoria=suma(1,4)
print(sumatoria)