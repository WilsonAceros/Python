menu="""
Bienvenido al conversor de Monedas 💲 a dolares EEUU

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Dolar Canadiense

Elige una opcion: """

opcion=int(input(menu))

if opcion==1:
    pesos=input("Cuantos pesos colombianos tienes?: ")
    pesos=float(pesos)
    valor_dolar=3875
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print(f'Tienes ${dolares} dolares americanos')
elif opcion ==2:
    pesos=input("Cuantos pesos mexicanos tienes?: ")
    pesos=float(pesos)
    valor_dolar=24
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print(f'Tienes ${dolares} dolares americanos')
elif opcion==3:
    pesos=input("Cuantos dolares canadienses tienes?: ")
    pesos=float(pesos)
    valor_dolar=1.34
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print(f'Tienes ${dolares} dolares americanos')
else:
    print("Elige una opcion correcta!")

