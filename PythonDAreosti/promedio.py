def promedio():
    calificacion=[]
    for i in range(10):
        note=float(input('Ingresa una calificacion: '))
        calificacion.append(note)
    average=sum(calificacion)/len(calificacion)
    return average


if __name__=='__main__':
    result=promedio()
    
    print(f'El promedio es: {result}')