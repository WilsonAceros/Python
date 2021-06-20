"""3.	Escribe un programa que lea dos matrices de la misma
longitud y permita realizar las siguientes operaciones:
Suma, Resta y Multiplicación por escalar. Reusa el código
del punto anterior para leer las matrices e imprimir el
resultado. Guarda el archivo como OperacionesMatriz. Py"""
def suma_matriz(mat1,mat2):
    matriz=[]
    for x in range(int(m)):
        interna=[]
        for y in range(int(n)):
            sum=float(mat1[x][y])+float(mat2[x][y])
            interna.append(round(sum,1))
        matriz.append(interna)
    return matriz

def resta_matriz(mat1,mat2):
    matriz=[]
    for x in range(int(m)):
        interna=[]
        for y in range(int(n)):
            rest=float(mat1[x][y])-float(mat2[x][y])
            interna.append(round(rest,1))
        matriz.append(interna)
    return matriz

def multiplicacion_escalar_matriz(mat,escalar):
    matriz=[]
    for x in range(int(m)):
        interna=[]
        for y in range(int(n)):
            mul=float(escalar)*float(mat[x][y])
            interna.append(round(mul,1))
        matriz.append(interna)
    return matriz

def mostrar_matriz(mat_result):
    #Ciclo para imprimir como pide el requerimiento
    for x in range(int(n)):
        for y in range(int(m)):
            if y==0:
                print("|",mat_result[x][y], end="\t")
            else:
                print(mat_result[x][y], end="\t")
        print("|")

print("Ingresa el tamaño de la matriz 1")
n=input("n: ")
m=input("m: ")
mat1=[]

#Ciclo para ingresar los datos a la matrix 1
for i in range(int(n)):
    lista_interna=[]
    for j in range(int(m)):
        numero=input("Digite un numero matriz 1: ")
        lista_interna.append(numero)
    mat1.append(lista_interna)

print("Ingresa el tamaño de la matriz 2")
x=input("n: ")
y=input("m: ")
mat2=[]

if x==n and y==m:
    #Ciclo para ingresar los datos a la matrix 2
    for i in range(int(n)):
        lista_interna=[]
        for j in range(int(m)):
            numero=input("Digite un numero matriz 2: ")
            lista_interna.append(numero)
        mat2.append(lista_interna)
    mat_result=suma_matriz(mat1,mat2)
    print("Matriz 1")
    mostrar_matriz(mat1)
    print("-----------------")
    print("Matriz 2")
    mostrar_matriz(mat2)
    print("-----------------")
    print("Suma de Matrices")
    mostrar_matriz(mat_result)
    print("-----------------")
    print("Resta de Matrices")
    mat_result=resta_matriz(mat1,mat2)
    mostrar_matriz(mat_result)
    print("-----------------")
    print("Multiplicación matriz por escalar")
    escalar=input("Ingresa un escalar: ")
    mat_result=multiplicacion_escalar_matriz(mat1,escalar)
    mostrar_matriz(mat_result)
else:
    print("Debes ingresar matrices de igual tamaño")