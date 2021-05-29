import random

#Mensaje de inicio

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

#Credenciales de entrada
codigo_grupo=51721
codigo_inver=12715

#Banderas para permanecer o salir de los while
ingreso=True
error=True

#Este loop valida el nombre de usuario inicialmente
while ingreso:

    #Este while permite asegurarse que el nombre de usuario sera un numero entero
    while error:

        #El try except permite tratar el error por ingresar un string
        try:
            usuario=int(input("Nombre de Usuario: "))
            break
        except ValueError:
            print("Por favor ingresa el usuario correspondiente al numero de grupo")
            continue

    #Validar que el usuario ingresado sea el valor verdadero de la credencial
    if usuario==codigo_grupo:

        #Este while permite asegurarse que la contraseña sera un numero entero
        while error:
            #El try except permite tratar el error por ingresar un string
            try:
                password=int(input("Contraseña: "))
                break
            except ValueError:
                print("Por favor ingresa la contraseña en numeros")
                continue

        #Loop para validar la contraseña
        while ingreso:

            #Validar que la contraseña ingresada sea el valor verdadero de la credencial
            if password==codigo_inver:

                def captcha1():
                    print('(-5*1)+7= ')

                def captcha2():
	                print('(5*1)+2= ')

                def captcha3():
	                print('(7-(2*1)= ')

                switch_captcha = {
	                1: captcha1,
	                2: captcha2,
	                3: captcha3,}

                switch_resultados = {
                	1: 2,
	                2: 7,
	                3: 5,}

                index=random.randint(1,3)

                #Este while permite asegurarse que captcha sera un numero entero
                while error:
                    #El try except permite tratar el error por ingresar un string
                    try:
                        print("Captcha Seguridad \n")
                        #tomamos la función asociada a la variable y la invocamos
                        switch_captcha.get(index)()
                        print("\n")
                        #Guardo el resultado del captcha capturado del usuario
                        captcha=int(input("Cual es el resultado de la siguiente operacion: "))
                        break
                    except ValueError:
                        print("Por favor ingrese el resultado en numeros")
                        continue

                #Loop para validar captcha seguridad
                while ingreso:

                    #Validar que la contraseña ingresada sea el valor verdadero de la credencial
                    if captcha==switch_resultados[index]:
                        print("Sesión Iniciada") #Mensaje de sesion iniciada
                        ingreso=False #Cambio la bandera a False, para terminar el programa
                    else:
                        print("Error") #Muestro mensaje de error porque la contraseña no coincide
                        ingreso=False #Cambio la bandera a False, para terminar el programa
                #

            else:
                print("Error") #Muestro mensaje de error porque la contraseña no coincide
                ingreso=False #Cambio la bandera a False, para terminar el programa
    else:
        print("Error") #Muestro mensaje de error porque la contraseña no coincide
        ingreso=False #Cambio la bandera a False, para terminar el programa