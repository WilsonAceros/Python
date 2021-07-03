dictionary={1:'Uno',2:'Dos',
            3:'Tres',4:'Cuatro'}

print(len(dictionary))
listavalores=list(dictionary.values())
print(type(listavalores))
print(listavalores)
print(listavalores[0])
lista_key=list(dictionary.keys())
print(lista_key)

#Imprimo las KEYs
for x in dictionary:
    print(x)

#Imprimo los valores
for x in dictionary.values():
    print(x)

#Imprimo los valores
for x in dictionary:
    print(x,dictionary[x])

x = ('key1', 'key2', 'key3')
y = [0,1,2]

thisdict = dict.fromkeys(x, y)

print(thisdict)