#Cómo trabajar con archivos import os #
print("RUTA",__file__)
archivo=open("Teste.txt","w")
archivo.write("Hola mundo\n")
archivo.write("Hello world\n")
archivo.close()