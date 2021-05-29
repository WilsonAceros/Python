# -*- coding: utf-8 -*-

def binary_search(numbers, number_find,low,high):
    
    if low>high:
        return False
    
    mid=int((low+high)/2)
    
    if numbers[mid]==number_find:
        return True
    elif numbers[mid]>number_find:
        return binary_search(numbers,number_find,low,mid-1)
    else:
        return binary_search(numbers,number_find,mid+1,high)

if __name__=='__main__':
    numbers=[1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]
    
    number_find=int(input('Ingresa un numero: '))
    
    result=binary_search(numbers,number_find,0,len(numbers)-1)
    
    if result is True:
        print('El numero sí está en la lista')
    else:
        print('El numero no está en la lista')
    