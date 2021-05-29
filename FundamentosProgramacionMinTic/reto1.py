import random

#Mensaje de inicio

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

#Credenciales de entrada
codigo_grupo=51721
codigo_inver=12715

#Banderas para permanecer o salir de los while
ingreso=True
error=True

#Captchas seguridad
"""
captcha1=7-(5*1)
captcha2=(5*2)-(7+1)
captcha3=(5%2)+(7%2)
captcha4=(7//2)-(5%2)
captcha5=(5*7)-2**5-1
captcha=721+2
"""


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
                    return 7-(5*1)

                def captcha2():
                    return (5*2)-(7+1)

                def captcha3():
                    return (5%2)+(7%2)

                def captcha4():
                    return (7//2)-(5%2)

                def captcha5():
                    return (5*7)-2**5-1

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

                        #Guardo el resultado del captcha capturado del usuario
                        captcha=int(input(f"721+{resul_operacion}: "))
                        break
                    except ValueError:
                        print("Por favor ingrese el resultado en numeros")
                        continue

                #Loop para validar captcha seguridad
                while ingreso:

                    #Validar que la contraseña ingresada sea el valor verdadero de la credencial
                    if captcha==723:
                        print("Sesión iniciada") #Mensaje de sesion iniciada
                        ingreso=False #Cambio la bandera a False, para terminar el programa
                    else:
                        print("Error") #Muestro mensaje de error porque la contraseña no coincide
                        ingreso=False #Cambio la bandera a False, para terminar el programa

            else:
                print("Error") #Muestro mensaje de error porque la contraseña no coincide
                ingreso=False #Cambio la bandera a False, para terminar el programa
    else:
        print("Error") #Muestro mensaje de error porque la contraseña no coincide
        ingreso=False #Cambio la bandera a False, para terminar el programa