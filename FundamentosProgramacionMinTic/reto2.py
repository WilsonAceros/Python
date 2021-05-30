import random
import time #Para poder usar el time.sleep()
import os #Para poder usar os.system

#Mensaje de inicio
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

#Credenciales de entrada
codigo_grupo="51721"
codigo_inver="12715"

#Banderas para permanecer o salir de los while
ingreso=True
error=True

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

                #Loop para validar captcha seguridad
                while ingreso:

                    #Validar que la contraseña ingresada sea el valor verdadero de la credencial
                    if captcha==captcha_correct:
                        print("Sesión iniciada") #Mensaje de sesion iniciada
                        time.sleep(1) #Espera 1 seg
                        command = 'cls' #Comando clear en windows
                        os.system(command) #Borra la consola

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

                        #Loop para seleccionar opcion del menu
                        while ingreso:
                            print(menu) #Imprimir el menu inicial
                            opcion=int(input("Elija una opción ")) #Elegir opcion
                            print("\n") #Salto de linea

                            #Condicionales para ingresar al menu seleccionado
                            if opcion==1:
                                continue
                            elif opcion==2:
                                continue
                            elif opcion==3:
                                continue
                            elif opcion==4:
                                continue
                            elif opcion==5:
                                continue
                            elif opcion==6:
                                #Elegir opcion favorita del menu
                                favorite=int(input("Seleccione opción favorita "))
                                if favorite==1:
                                    adivinanzas()
                                    continue
                                elif favorite==2:
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 2 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(2)})
                                        menu.update({
                                            2: change_menu})
                                        os.system(command) #Borra la consola
                                        continue
                                    else:
                                        continue
                                elif favorite==3:
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 3 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(3)})
                                        menu.update({
                                            3: change_menu})
                                        os.system(command) #Borra la consola
                                        continue
                                    else:
                                        continue
                                elif favorite==4:
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 4 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(4)})
                                        menu.update({
                                            4: change_menu})
                                        os.system(command) #Borra la consola
                                        continue
                                    else:
                                        continue
                                elif favorite==5:
                                    adv_correct=adivinanzas()
                                    if adv_correct:
                                        #Pone la opcion 5 como 1 en el menu
                                        change_menu=menu.get(1) #Guardo la opcion 1 antes de reemplazarla
                                        #Actualizo el menu de acuerdo a la seleccion
                                        menu.update({
                                            1: menu.get(5)})
                                        menu.update({
                                            5: change_menu})
                                        os.system(command) #Borra la consola
                                        continue
                                    else:
                                        continue
                                else:
                                    print("Error") #Muestro mensaje de error porque eligió una opcion del menu diferente 1 a 5
                                    ingreso=False #Cambio la bandera a False, para terminar el programa
                            elif opcion==7:
                                print("Hasta pronto") #Sesión cerrada
                                ingreso=False #Cambio la bandera a False, para terminar el programa
                            else:
                                print("Error") #Muestro mensaje de error porque eligió una opcion que no esta en el menu
                                ingreso=False #Cambio la bandera a False, para terminar el programa
                    else:
                        print("Error") #Muestro mensaje de error porque el captcha no coincide
                        ingreso=False #Cambio la bandera a False, para terminar el programa

            else:
                print("Error") #Muestro mensaje de error porque la contraseña no coincide
                ingreso=False #Cambio la bandera a False, para terminar el programa
    else:
        print("Error") #Muestro mensaje de error porque el usuario no coincide
        ingreso=False #Cambio la bandera a False, para terminar el programa