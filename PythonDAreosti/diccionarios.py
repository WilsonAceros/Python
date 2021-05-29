mi_dicc={}
mi_dicc['primer']='Hola'
mi_dicc['segundo']='Adios'

print(mi_dicc['primer'])

for key in mi_dicc:
    print(key)

for value in mi_dicc.values():
    print(value)

for key, value in mi_dicc.items():
    print(f'llave: {key}, valor: {value}')