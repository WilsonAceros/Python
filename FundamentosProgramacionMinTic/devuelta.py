"""6. Elabora el pseudocódigo y el diagrama de flujo de un
programa que calcule una devuelta sobre una compra, con un
valor constante.
7. Escribe el programa en un archivo con nombre devuelta.py
y haz la prueba de escritorio."""

buy=int(input("Valor de la compra: $"))
cash=int(input("Con cuanto pagas: $"))
devuelta=cash-buy
print("Su devuelta es $",devuelta)
