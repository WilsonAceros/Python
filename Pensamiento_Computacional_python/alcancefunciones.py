valor1=5
valor2=2

def operaciones(valor2, valor3):
    suma=valor1+valor2
    resta=valor2-valor3
    return (suma, resta)

multiplicacion= valor1*valor2

datos=operaciones(4,8)
print(f'suma y resta {datos} multiplicacion {multiplicacion}')