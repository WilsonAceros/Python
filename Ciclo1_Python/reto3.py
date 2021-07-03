import random
import time #Para poder usar el time.sleep()
import os #Para poder usar os.system
import platform

#Mensaje de inicio
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

#Credenciales de entrada
codigo_grupo="51721"
codigo_inver="12715"

#Variables para guardar las coordenadas ingresadas
coordenadas=[]
fila=[]
norte=[]
oriente=[]

#Rango de coordendas
Municipio=['Calamar','Bolivar']
rango_latitud=[10.103,10.362]
rango_longitud=[-75.088,-74.918]

#Banderas para permanecer o salir de los while
ingreso_menu=False
favorite='0' #Permence en cero sino ha ingresado al menu de favoritos
contador=0 #Para llevar el conteo del numero de intentos de error en el menu
i=0
j=0

#Menu de opciones inicial, utilizando un diccionario
menu=["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zonas wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]

def mostrar_menu():
    for i in range(len(menu)):
        print(i+1,'. ',menu[i])
# mostrar_menu()

#Diferentes operaciones que devuelven el penultimo numero grupo: 2
def captcha1():
    return 7-(5*1)

def captcha2():
    return (5*2)-(7+1)

def captcha3():
    return (7*1-5)//1

def captcha4():
    return (7//2)-(5%2)

def captcha5():
    return (5*7)-2**5-1

#Diccionario para ingresar a cada funcion que retorna 2
switch_captcha = {
    1: captcha1,
    2: captcha2,
    3: captcha3,
    4: captcha4,
    5: captcha5,}

#Funcion para limpiar consola de acuerdo al system
def limpiar_consola():
    if platform.system() == "Windows":
        os.system('cls') #Borra la consola
    else: #Linux, macOS
        os.system('clear')

def adivinanzas():
    adiv1=int(input("Para confirmar por favor responda: Estás participando en una carrera. Adelantas al segundo. ¿En qué posición terminas?: "))
    if adiv1==2:
        adiv2=int(input("Para confirmar por favor responda: Un agricultor tiene tres montones de paja en el pajar y cuatro en el prado. Si los junta ¿cuántos montones tiene?: "))
        if adiv2==1:
            return True
        else:
            print("Error")
            return False
    else:
        print("Error")
        return False

#Funcion para actualizar coordenada
def actualizar_coord(act_coord,x):
    latitud=input("Latitud: ")
    if latitud!="":
        #Valido que latitud esta en el rango segun el grupo
        if (float(latitud)>=rango_latitud[0]) and (float(latitud)<=rango_latitud[1]):
            act_coord[0]=latitud #Agrega latitud al final de la lista
            longitud=input("Longitud: ")
            if longitud!="":
                #Valido que longitud esta en el rango segun el grupo
                if (float(longitud)>=rango_longitud[0]) and (float(longitud)<=rango_longitud[1]):
                    act_coord[1]=longitud#Agrega latitud al final de la lista
                    coordenadas[x]=act_coord
                    return True
                    #print(coordenadas)
                else:
                    print("Error coordenada")
                    return False
            else:
                print("Error")
                return False
        else:
            print("Error coordenada")
            return False
    else:
        print("Error")
        return False

usuario=input("Nombre de Usuario: ")

#Validar que el usuario ingresado sea el valor verdadero de la credencial
if usuario==codigo_grupo:

    password=input("Contraseña: ")

    #Validar que la contraseña ingresada sea el valor verdadero de la credencial
    if password==codigo_inver:

        print("Captcha Seguridad")
        #Calculo la operacion de forma aleatoria para obtener el penultimo numero
        resul_operacion=switch_captcha.get(random.randint(1,5))()
        captcha_correct=str(721+resul_operacion)
        #Guardo el resultado del captcha capturado del usuario
        captcha=input(f"721+{resul_operacion}: ")
        #Validar que la contraseña ingresada sea el valor verdadero de la credencial
        if captcha==captcha_correct:
            print("Sesión iniciada") #Mensaje de sesion iniciada
            time.sleep(0) #Espera 1 seg
            limpiar_consola()
            ingreso_menu=True
            #Loop para seleccionar opcion del menu
        else:
            print("Error") #Muestro mensaje de error porque el captcha no coincide
    else:
        print("Error") #Muestro mensaje de error porque la contraseña no coincide
else:
    print("Error") #Muestro mensaje de error porque el usuario no coincide

while ingreso_menu:
    mostrar_menu() #Imprimir el menu inicial
    #if favorite=='0':
    opcion=input("Elija una opción ") #Elegir opcion
    if opcion in ['1','2','3','4','5']:
        print(f"Usted ha elegido la opción {opcion}") #Salto de linea
    if opcion in ['1','2','3','4','5','6','7']:
        valores=menu[int(opcion)-1]
    else:
        valores="Opcion diferente"
    #print(valores)
    #Condicionales para ingresar al menu seleccionado
    if valores=="Cambiar contraseña":
        password=input("Contraseña actual: ")
        if password==codigo_inver:#Valida si la contraseña actual es igual a la inicial
            password1=input("Nueva Contraseña: ")#Ingresa nueva contraseña para cambiar
            if password1==codigo_inver:
                print("La contraseña debe ser diferente a la actual")
                continue
            else:
                codigo_inver=password1#Asigna el valor de la nueva contraseña
                continue
        else:
            print("Error")
            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    elif valores=="Ingresar coordenadas actuales":
        if coordenadas==[]:
            error=True
            while i<3 and error:
                i+=1 #Sumo 1 al contador i
                while j<1 and error:
                    j+=1 #suma 1 al contador j
                    latitud=input("Latitud: ")
                    if latitud!="":
                        #Valido que latitud esta en el rango segun el grupo
                        if (float(latitud)>=rango_latitud[0]) and (float(latitud)<=rango_latitud[1]):
                            fila.append(latitud)#Agrega latitud al final de la lista
                            longitud=input("Longitud: ")
                        else:
                            print("Error coordenada")
                            i=0 #Es necesario reiniciar el contador para la proxima vez que ingrese
                            j=0 #Es necesario reiniciar el contador para la proxima vez que ingrese
                            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
                            error=False #Para salir del while
                            break #Sale del while anidado
                        if longitud!="":
                            #Valido que longitud esta en el rango segun el grupo
                            if (float(longitud)>=rango_longitud[0]) and (float(longitud)<=rango_longitud[1]):
                                fila.append(longitud)#Agrega longitud al final de la lista
                                coordenadas.append(fila[-2:])#agega la sublista (los dos ultimos numeros) a la lista coordendas
                                j=0
                                break
                            else:
                                print("Error coordenada")
                                i=0
                                j=0
                                ingreso_menu=False #Cambio la bandera a False, para terminar el programa
                                error=False
                                break
                        else:
                            print("Error")
                            i=0
                            j=0
                            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
                            error=False
                            break
                    else:
                        print("Error")
                        i=0
                        j=0
                        ingreso_menu=False #Cambio la bandera a False, para terminar el programa
                        error=False
                        break
            i=0
            continue
        else:
            #Imprime la coordenadas guardadas
            for i in range(len(coordenadas)):
                print("coordenada [latitud,longitud] {} : {}".format(i+1,coordenadas[i]))
            #Calcula la coordenada mas al norte
            for i in range(len(coordenadas)):
                cord=coordenadas[i]
                for j in range(1):
                    norte.append(cord[j])
            #print(norte)
            #Calcula la coordenada mas al oriente
            print("La coordenada {} es la que está más al norte".format((norte.index(max(norte)))+1))
            norte.clear()
            for i in range(len(coordenadas)):
                cord=coordenadas[i]
                for j in range(1):
                    oriente.append(cord[j+1])
            #print(oriente)
            print("La coordenada {} es la que está más al oriente".format((oriente.index(min(oriente)))+1))
            oriente.clear()
            opcion_coord=input("Presione 1,2 o 3 para actualizar la respectiva coordenadas\npresione 0 para regresar al menu ")
            if opcion_coord=='0':
                pass
            elif opcion_coord in ['1','2','3']:
                act_coord=coordenadas[int(opcion_coord)-1]
                ingreso_menu=actualizar_coord(act_coord,int(opcion_coord)-1)
            else:
                print("Error actualización")
                ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    elif valores=="Ubicar zonas wifi más cercana":
        ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    elif valores=="Guardar archivo con ubicación cercana":
        ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    elif valores=="Actualizar registros de zonas wifi desde archivo":
        ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    elif valores=="Elegir opción de menú favorita":
        #Elegir opcion favorita del menu
        favorite=input("Seleccione opción favorita ")
        if favorite in ['1','2','3','4','5']:
            adivinanzas()
            ftext=menu.pop(int(favorite)-1)
            menu.insert(0,ftext)
            continue
        else:
            print("Error") #Muestro mensaje de error porque eligió una opcion del menu diferente 1 a 5
            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    elif valores=="Cerrar sesión":
        print("Hasta pronto") #Sesión cerrada
        ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    else:
        print("Error") #Muestro mensaje de error porque eligió una opcion que no esta en el menu
        contador+=1#Cuando complete 3 errores sale del programa
        if contador==3:
            ingreso_menu=False#Cambio la bandera a False, para terminar el programa
        continue