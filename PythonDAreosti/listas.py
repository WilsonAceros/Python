amigos=list()
amigos.append('pedro')
print(amigos)
amigos.append('enrique')
print(amigos)
amigos.append('wilson')
print(amigos)
print(amigos[0])

def average_temps(temps):
    sum_temps=0
    
    for temp in temps:
        sum_temps+=temp
    
    return sum_temps/len(temps)

if __name__=='__main__':
    temps=[21,24,24,22,20,23,24]
    average=average_temps(temps)
    print(f'La temperatura promedio es {average}')