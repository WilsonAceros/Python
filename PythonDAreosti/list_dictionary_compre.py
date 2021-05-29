#LIST
pares=[]
for num in range(1,31):
    if num%2==0:
        pares.append(num)
print(pares)

#List comprehension
even=[num for num in range (1,31) if num%2==0]
print(even)

#DICTIONARY
cuadrados={}
for num in range(1,11):
    cuadrados[num]=num**2
print(cuadrados)

#Dictionary comprehension
squares={num: num**2 for num in range(1,11)}
print(squares)