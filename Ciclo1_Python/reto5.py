import random
import time #Para poder usar el time.sleep()
import os #Para poder usar os.system
import platform
import math
# import pandas as pd
# from pandas import ExcelWriter

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
distancia=[]
usuarios=[]
t=[]
zona=[]

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

R=6372.795477598 #km Radio de la Tierra
#Calcular distancia entre coordenadas
def calcular_distancia(lat1,lat2,long1,long2,R):
    a=(math.sin((lat2-lat1)/2))**2
    b=(math.cos(lat1))
    c=math.cos(lat2)
    d=(math.sin((long2-long1)/2))**2
    e=math.sqrt(a+b*c*d)
    distancia=2*R*math.asin(e)
    return distancia

velocidad_prom_bus=16.67 #m/s
velocidad_prom_pie=0.483 #m/s

#Calcular tiempo de acuerdo a bus y a pie
def calcular_tiempo(d,velocidad_prom_bus,velocidad_prom_pie):
    tiempo1=d/velocidad_prom_bus
    tiempo2=d/velocidad_prom_pie
    return tiempo1,tiempo2

#Envia mensaje para saber las indicaciones de acuerdo al punto frecuentado
def mensaje_indicacion(lat1,long1,lat2,long2):
    if long2>long1 and lat2>lat1:
        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
    elif long2<long1 and lat2>lat1:
        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
    elif long2>long1 and lat2<lat1:
        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el sur")
    elif long2<long1 and lat2<lat1:
        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur")

def calcular_prom(n):
    sum=0
    for i in range(n):
        lat_prom=input("Latitud {}: ".format(i+1))
        sum=sum+float(lat_prom)
    return sum/n

#RF01
zona_wifi=[[10.127,-74.950,0],[10.196,-74.935,0],[10.305,-75.040,2490],[10.196,-74.94,101]]
# for x in range(4):
#     print (zona_wifi[x])
#     print()

#RETO 1
usuario=input("Nombre de Usuario: ")
#Validar que el usuario ingresado sea el valor verdadero de la credencial
if usuario==codigo_grupo:

    password=input("Contraseña: ")

    if password=="m1s10nt1c":
        n=input("Cantidad de latitudes: ")
        promedio=calcular_prom(int(n))
        print("El promedio es:",promedio)
        exit()
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
            print("La coordenada {} es la que está más al norte".format((norte.index(max(norte)))+1))
            norte.clear()
            #Calcula la coordenada mas al oriente
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
    #RF02
    elif valores=="Ubicar zonas wifi más cercana":
        if coordenadas==[]:
            print("Error sin registro de coordenadas")
            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
        else:
            #Imprime la coordenadas guardadas
            for i in range(len(coordenadas)):
                print("coordenada [latitud,longitud] {} : {}".format(i+1,coordenadas[i]))
            opcion_dist=input("Por favor elija su ubicación actual (1,2 o 3) para calcular la distancia a los puntos de conexión ")
            if opcion_dist in ['1','2','3']:
                #Calcula la distancia
                coor_actual=coordenadas[int(opcion_dist)-1]#asigna la coordenada seleccionada
                lat1=float(coor_actual[0]) #Asigna latitud 1
                long1=float(coor_actual[1]) #Asigna longitud 1
                # print(lat1,long1)
                for i in range(4):
                    zona=zona_wifi[i]#Asigno a zona la primera zona wifi
                    # print(zona)
                    for j in range(1):
                        lat2=zona[j] #asisgno latitud 2 de la zona previamente seleccionada
                        long2=zona[j+1] #asisgno longitud 2 de la zona previamente seleccionada
                        # print(lat2,long2)
                        d=calcular_distancia(lat1,long1,lat2,long2,R)#Funcion para calcular la distancia
                        distancia.append(d) #Agrego a la lista distancia todas las distancias calculadas
                        # print(distancia)
                        usuarios.append(zona[j+2])#Agrego a la lista usuarios los promedios de cada zona wifi
                        # print(usuarios)
                        min_usuarios1=min(usuarios)#Calcula el minimo usuarios promedio de la lista usuarios
                # print(min_usuarios1)
                index_min1=usuarios.index(min_usuarios1)#Asigno el indice del correspondiente promedio minimo
                d1=round(distancia[index_min1],2)
                print("Zonas wifi cercanas con menos ususarios")
                print("La zona wifi {}: ubicada en {} a {} metros, tiene en promedio {} usuarios".format(index_min1+1,zona_wifi[index_min1][:2],d1,zona_wifi[index_min1][2]))
                x=usuarios.pop(index_min1)#Elimino el indice minimo
                y=max(usuarios)#calculo el maximo promedio
                usuarios.insert(index_min1,y)#inserto el valor maximo en la lista usuarios, con tal de reemplazar el minimio inicial
                # print(usuarios)
                min_usuarios2=min(usuarios)#Calculo el numero minimo, correspondiente el segundo minimo original
                # print(min_usuarios2)
                index_min2=usuarios.index(min_usuarios2)#Asigno el indice del correspondiente segundo promedio minimo
                d2=round(distancia[index_min2],2)
                print("La zona wifi {}: ubicada en {} a {} metros, tiene en promedio {} usuarios".format(index_min2+1,zona_wifi[index_min2][:2],d2,zona_wifi[index_min2][2]))
                #RF03
                indicaciones_llegada=input("Elija 1 o 2 para recibir indicaciones de llegada ")
                usuarios.clear()
                distancia.clear()
                if indicaciones_llegada=='1':
                    lat2=zona_wifi[index_min1][0]
                    long2=zona_wifi[index_min1][1]
                    mensaje_indicacion(lat1,long1,lat2,long2)
                    d=d1
                    t=calcular_tiempo(d,velocidad_prom_bus,velocidad_prom_pie)
                    tb=round(t[0]/60,2)
                    tp=round((t[1]/60)/60,2)
                    print("Tiempo en bus: ",tb," min")
                    print("Tiempo a pie: ",tp," hr")
                    salir=True
                    while salir:
                        sel=input("Presione 0 para salir ")
                        if sel=='0':
                            salir=False
                        else:
                            salir=True
                elif indicaciones_llegada=='2':
                    lat2=zona_wifi[index_min2][0]
                    long2=zona_wifi[index_min2][1]
                    mensaje_indicacion(lat1,long1,lat2,long2)
                    d=d2
                    t=calcular_tiempo(d,velocidad_prom_bus,velocidad_prom_pie)
                    tb=round(t[0]/60,2)
                    tp=round((t[1]/60)/60,2)
                    print("Tiempo en bus: ",tb," min")
                    print("Tiempo a pie: ",tp," hr")
                    salir=True
                    while salir:
                        sel=input("Presione 0 para salir ")
                        if sel=='0':
                            salir=False
                        else:
                            salir=True
                else:
                    print("Error zona wifi")
                    ingreso_menu=False #Cambio la bandera a False, para terminar el programa
            else:
                print("Error ubicación")
                ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    elif valores=="Guardar archivo con ubicación cercana":
        if coordenadas==[] or t==[]:
            print("Error de alistamiento")
            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
        else:
            if indicaciones_llegada=='1':
                index_min=index_min1
            elif indicaciones_llegada=='2':
                index_min=index_min2
            #Creo el diccionario para exportar la informacion a un archivo.
            #Tener en cuenta que se puede guardar siempre y cuando las listas tengan la misma longitud
            informacion = {
                'actual':[lat1,long1,0],
                'zonawifi':zona_wifi[index_min],
                'recorrido':[d,'Bus',str(tb)+' min']}
            print(informacion)
            opcion_exportar=input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal ")
            if opcion_exportar=='1':

                #RUTINA PARA CREAR ARCHIVO CSV CON PANDAS
                # df = pd.DataFrame(informacion)
                # # print(df)
                # #mode=a, funciona como un append dentro del archivo, no borra lo anterior
                # df.to_csv('FundamentosProgramacionMinTic/datos.csv', mode='w', index=False, header=True,sep=';',decimal='.',encoding='utf-8')

                #RUTINA PARA CREAR ARCHIVO DE TEXTO PLANO
                #Primero convierto el diccionario en un string
                z=[]
                for i in informacion:
                    z.append(i)
                    y=informacion[i]
                    for j in y:
                        z.append(str(j))
                # print(z)51
                cadena = ", ".join(z)#Vuelve una lista en cadena string
                # print(cadena)

                #Crea el archivo de texto, pero solo se le pueden ingresar string, no listas ni dict
                file = open("datos.txt", "w")
                file.write(cadena+os.linesep)#Escribe la cadena+os.linesep
                file.close()#Cierra el archivo

                # FORMA DE EDITAR EL ARCHIVO
                # with open("datos.txt", "w") as archivo:
                #     archivo.writelines("Hola")
                print("Exportando archivo")
                ingreso_menu=False #Cambio la bandera a False, para terminar el programa
            elif opcion=='0':
                continue
    elif valores=="Actualizar registros de zonas wifi desde archivo":
        # LEER ARCHIVO CON PANDAS
        # archivo=pd.read_csv(r'FundamentosProgramacionMinTic/Betulia.csv',encoding='utf-8',delimiter=";")
        # print(archivo)
        # dat=archivo.values.tolist()
        # print(zona_wifi)
        # zona_wifi.clear()
        # for fila in dat:
        #     for c in range(len(fila)):
        #         zona.append(float(fila[c]))
        #     zona_wifi.append(zona[-3:])
        # print(zona_wifi)

        #Abre el archivo, pero solo se le pueden ingresar string, no listas ni dict
        archivo = open("Betulia.txt", "r")
        dat=archivo.read()#Escribe la cadena+os.linesep
        # print(dat)
        archivo.close()#Cierra el archivo
        n=""
        c=0
        zona_wifi.clear()
        for fila_interna in dat:
            if fila_interna==',':
                zona.append(float(n))
                # print(n)
                # print(zona)
                n=""
                c+=1
                if c>2:
                    zona_wifi.append(zona)
                    zona=[]
                    c=0
            else:
                n=n+fila_interna

        opcion_principal=input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal ")
        if opcion_principal=='0':
            continue
        else:
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
    elif opcion=="2022":
        coord_latino=input("Escribe una coordenada de una longitud en Sudamérica y te diré su huso horario: ")
        if float(coord_latino)>=-81.296 and float(coord_latino)<=-67.401:
            print("El huso horario es -5")
            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
        elif float(coord_latino)>-67.402 and float(coord_latino)<-54.316:
            print("El huso horario es -4")
            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
        elif float(coord_latino)>-54.316 and float(coord_latino)<-35.833:
            print("El huso horario es -3")
            ingreso_menu=False #Cambio la bandera a False, para terminar el programa
    else:
        print("Error") #Muestro mensaje de error porque eligió una opcion que no esta en el menu
        contador+=1#Cuando complete 3 errores sale del programa
        if contador==3:
            ingreso_menu=False#Cambio la bandera a False, para terminar el programa
        continue