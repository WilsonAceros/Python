import random

#51721
def captcha1():
    print('(-5*1)+7= ')

def captcha2():
	print('(5*1)+2= ')

def captcha3():
	print('(7-(2*1)= ')

switch_captcha = {
	1: captcha1,
	2: captcha2,
	3: captcha3,
}

switch_resultados = {
	1: 2,
	2: 7,
	3: 5,
}

index=random.randint(1,3)

#tomamos la función asociada a la variable y la invocamos
switch_captcha.get(index)()

print(switch_resultados[index])