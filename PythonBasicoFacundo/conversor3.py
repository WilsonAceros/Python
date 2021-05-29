def convertir(tipo,valor_dolar):
    pesos=input("Cuantos "+tipo+" tienes?: ")
    pesos=float(pesos)
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print(f'Tienes ${dolares} dolares americanos')
    
menu="""
Bienvenido al conversor de Monedas 💲 a dolares EEUU

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Dolar Canadiense

Elige una opcion: """

opcion=int(input(menu))
    
if opcion==1:
    convertir("Pesos Colombianos",3875)
elif opcion ==2:
    convertir("Pesos Mexicanos",24)
elif opcion==3:
    convertir("Dolares Canadiense",1.34) 
else:
    print("Elige una opcion correcta!")

