#ambio de las variables
mensaje="Hola" #Ambito global

def imprimir():
    global mensaje #La vuelvo global
    mensaje="Hello" #Ambito local
    print(mensaje)

imprimir()
print(mensaje)
