
# mat = [[1,3,5],
#         [10,20,6],
#         [7,0,8]]

mat=[]

for x in range(3):
    lista_interna=[]
    for y in range(2):
        numero=input("Digite un numero: ")
        lista_interna.append(numero)
    mat.append(lista_interna)

print(mat)

for x in range(3):
    for y in range(2):
        print(mat[x][y], end=" ")
    print()

valor = int(input("Digitie valor a buscar: "))
for x in range(3):
    for y in range(2):
        if valor==mat[x][y]:
            print("El valor esta en las coordenadas:", x+1,":", y+1)
