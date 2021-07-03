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
ingreso=True
error=True
favorite='0' #Permence en cero sino ha ingresado al menu de favoritos
contador=0 #Para llevar el conteo del numero de intentos de error en el menu
i=0
j=0

#Este loop valida el nombre de usuario inicialmente
while ingreso:

    #Este while permite asegurarse que el nombre de usuario sera un numero entero
    #while error:

    usuario=input("Nombre de Usuario: ")

    """ #El try except permite tratar el error por ingresar un string
        try:
            usuario=int(input("Nombre de Usuario: "))
            break
        except ValueError:
            print("Por favor ingresa el usuario correspondiente al numero de grupo")
            continue"""

    #Validar que el usuario ingresado sea el valor verdadero de la credencial
    if usuario==codigo_grupo:

        #Este while permite asegurarse que la contraseña sera un numero entero
        #while error:

        password=input("Contraseña: ")
            #El try except permite tratar el error por ingresar un string
        """     try:
                password=int(input("Contraseña: "))
                break
            except ValueError:
                print("Por favor ingresa la contraseña en numeros")
                continue"""

        #Loop para validar la contraseña
        while ingreso:

            #Validar que la contraseña ingresada sea el valor verdadero de la credencial
            if password==codigo_inver:
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

                #Este while permite asegurarse que captcha sera un numero entero
                while error:

                    #El try except permite tratar el error por ingresar un string
                    try:
                        print("Captcha Seguridad")
                        #Calculo la operacion de forma aleatoria para obtener el penultimo numero
                        resul_operacion=switch_captcha.get(random.randint(1,5))()
                        captcha_correct=721+resul_operacion
                        #Guardo el resultado del captcha capturado del usuario
                        captcha=int(input(f"721+{resul_operacion}: "))
                        break
                    except ValueError:
                        print("Por favor ingrese el resultado en numeros")
                        continue

                #Funcion para limpiar consola de acuerdo al system
                def limpiar_consola():
                    if platform.system() == "Windows":
                        os.system('cls') #Borra la consola
                    else: #Linux, macOS
                        os.system('clear')

                #Loop para validar captcha seguridad
                while ingreso:

                    #Validar que la contraseña ingresada sea el valor verdadero de la credencial
                    if captcha==captcha_correct:
                        print("Sesión iniciada") #Mensaje de sesion iniciada
                        time.sleep(0) #Espera 1 seg
                        limpiar_consola()

                        #Menu de opciones inicial, utilizando un diccionario
                        menu={
                            1: "Cambiar contraseña",
                            2: "Ingresar coordenadas actuales",
                            3: "Ubicar zonas wifi más cercana",
                            4: "Guardar archivo con ubicación cercana",
                            5: "Actualizar registros de zonas wifi desde archivo",
                            6: "Elegir opción de menú favorita",
                            7: "Cerrar sesión"}

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

                        #Loop para seleccionar opcion del menu
                        while ingreso:
                            print(menu) #Imprimir el menu inicial
                            #if favorite=='0':
                            opcion=input("Elija una opción ") #Elegir opcion
                            if opcion in ['1','2','3','4','5']:
                                print(f"Usted ha elegido la opción {opcion}") #Salto de linea
                            if opcion in ['1','2','3','4','5','6','7']:
                                valores=menu[int(opcion)]
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
                                    ingreso=False #Cambio la bandera a False, para terminar el programa
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
                                                    ingreso=False #Cambio la bandera a False, para terminar el programa
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
                                                        ingreso=False #Cambio la bandera a False, para terminar el programa
                                                        error=False
                                                        break
                                                else:
                                                    print("Error")
                                                    i=0
                                                    j=0
                                                    ingreso=False #Cambio la bandera a False, para terminar el programa
                                                    error=False
                                                    break
                                            else:
                                                print("Error")
                                                i=0
                                                j=0
                                                ingreso=False #Cambio la bandera a False, para terminar el programa
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
                                    elif opcion_coord=='1':
                                        act_coord=coordenadas[0]
                                        ingreso=actualizar_coord(act_coord,0)
                                    elif opcion_coord=='2':
                                        act_coord=coordenadas[1]
                                        ingreso=actualizar_coord(act_coord,1)
                                    elif opcion_coord=='3':
                                        act_coord=coordenadas[2]
                                        ingreso=actualizar_coord(act_coord,2)
                                    else:
                                        print("Error actualización")
                                        ingreso=False #Cambio la bandera a False, para terminar el programa
                            elif valores=="Ubicar zonas wifi más cercana":
                                ingreso=False #Cambio la bandera a False, para terminar el programa
                            elif valores=="Guardar archivo con ubicación cercana":
                                ingreso=False #Cambio la bandera a False, para terminar el programa
                            elif valores=="Actualizar registros de zonas wifi desde archivo":
                                ingreso=False #Cambio la bandera a False, para terminar el programa
                            elif valores=="Elegir opción de menú favorita":
                                #Elegir opcion favorita del menu
                                favorite=input("Seleccione opción favorita ")
                                if favorite=='1':
                                    adivinanzas()
                                    continue
                                elif favorite=='2':
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 2 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(2)})
                                        menu.update({
                                            2: change_menu})
                                        limpiar_consola()
                                        continue
                                    else:
                                        continue
                                elif favorite=='3':
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 3 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(3)})
                                        menu.update({
                                            3: change_menu})
                                        limpiar_consola()
                                        continue
                                    else:
                                        continue
                                elif favorite=='4':
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 4 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(4)})
                                        menu.update({
                                            4: change_menu})
                                        limpiar_consola()
                                        continue
                                    else:
                                        continue
                                elif favorite=='5':
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 5 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(5)})
                                        menu.update({
                                            5: change_menu})
                                        limpiar_consola()
                                        continue
                                    else:
                                        continue
                                else:
                                    print("Error") #Muestro mensaje de error porque eligió una opcion del menu diferente 1 a 5
                                    ingreso=False #Cambio la bandera a False, para terminar el programa
                            elif valores=="Cerrar sesión":
                                print("Hasta pronto") #Sesión cerrada
                                ingreso=False #Cambio la bandera a False, para terminar el programa
                            else:
                                print("Error") #Muestro mensaje de error porque eligió una opcion que no esta en el menu
                                contador+=1#Cuando complete 3 errores sale del programa
                                if contador==3:
                                    ingreso=False#Cambio la bandera a False, para terminar el programa
                                continue
                    else:
                        print("Error") #Muestro mensaje de error porque el captcha no coincide
                        ingreso=False #Cambio la bandera a False, para terminar el programa

            else:
                print("Error") #Muestro mensaje de error porque la contraseña no coincide
                ingreso=False #Cambio la bandera a False, para terminar el programa
    else:
        print("Error") #Muestro mensaje de error porque el usuario no coincide
        ingreso=False #Cambio la bandera a False, para terminar el programa