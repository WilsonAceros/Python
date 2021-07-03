"""2.	Escribe un programa que lea una matriz de longitud n x m,
luego imprime la matriz en consola similar al referente de la
imagen. Guarda el archivo como LecturaMatriz.py"""
print("Ingresa el tamaño de la matriz nxm")
n=input("n: ")
m=input("m: ")
mat=[]
#Ciclo para ingresar los datos a la matrix nxm
for x in range(int(n)):
    lista_interna=[]
    for y in range(int(m)):
        numero=input("Digite un numero: ")
        lista_interna.append(numero)
    mat.append(lista_interna)
#Ciclo para imprimir como pide el requerimiento
for x in range(int(n)):
    for y in range(int(m)):
        if y==0:
            print("|",mat[x][y], end="\t")
        else:
            print(mat[x][y], end="\t")
    print("|")
