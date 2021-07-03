#FUncion con argumentos arbitrarios
#Se utiliza un asterisco para poder ingresar varios argumentos arbitrarios, funciona como una tupla
def sistema_opertarivos(*sistema):
    for i in sistema:
        print("EL S.O es: ",i)

sistema_opertarivos("Windows","Linux","Mac","Android")

#Funcion con claves arbitrarias
#Se utiliza doble asterisco para poder ingresar varias claves arbitrarias, funciona como un diccionario
def imprimir_nombre(**nombres):
    print("Su nombres es",nombres["nombre"],nombres["apellido"])

imprimir_nombre(nombre="Wilson",apellido="Aceros")

# RECURSIVIDAD
def imprimir(num):
    print(num)
    num=num+1
    if num<100:
        imprimir(num)

imprimir(5)

# Validar credenciales usando claves arbitrarias
def inicio(**credenciales):
    if credenciales["user"]=='usuario' and credenciales["password"]=='12345':
        print("Inicio de sesión")
        return False
    else:
        return True
c=0
ingreso=True
while ingreso:
    u=input("Usuario: ")
    p=input("Contraseña: ")
    ingreso=inicio(user=u,password=p)
    c+=1
    if c>2:
        print("Excedio los 3 intentos, cuenta bloqueada")
        ingreso=False

#Abre el archivo, pero solo se le pueden ingresar string, no listas ni dict
archivo = open("C:\MinTic\FundamentosProgramacion\CodigosFuentes\FundamentosProgramacionMinTic\Betulia.txt", "r")
dat=archivo.read()#Escribe la cadena+os.linesep
print(dat)
print(type(dat))
archivo.close()#Cierra el archivo
zona=[]
zona_wifi=[]
n=""
c=0
#Guarda las coordenadas en una matriz de coordenadas zona_matriz
for fila in dat:
    if fila==',':
        zona.append(n)
        print(n)
        print(zona)
        n=""
        c+=1
        if c>2:
            zona_wifi.append(zona)
            print(zona_wifi)
            zona=[]
            c=0
    else:
        n=n+fila
