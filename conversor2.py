"""Convertir de pesos a dolares, pesos mexicanos
o pesos argentinos"""

pesos=input("Cuantos pesos colombianos tienes?: ")
pesos=float(pesos)
valor_dolar=3875
dolares=pesos/valor_dolar
dolares=round(dolares,2)
dolares=str(dolares)
print(f'Tienes ${dolares} dolares')