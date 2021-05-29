import random
#Probabilidad de obtener un 12 en por lo 
# menos 10 tiros con dos dados

def tirar_dado(numero_tiros):
    secuencia_tiros=[]
    for _ in range(numero_tiros):
        tiro1=random.choice([1,2,3,4,5,6])
        tiro2=random.choice([1,2,3,4,5,6])
        resultado=tiro1+tiro2
        secuencia_tiros.append(resultado)
    return secuencia_tiros


def main(numero_tiros,numero_intentos):
    tiros=[]
    for _ in range (numero_intentos):
        secuencia_tiros=tirar_dado(numero_tiros)
        tiros.append(secuencia_tiros)

    tiros_con_12=0
    for tiro in tiros:
        if 12 in tiro:
            tiros_con_12+=1
    probabilidad_tiros_con_12=tiros_con_12/numero_intentos
    print(f'Probabilidad de obtener por lo menos un 12 en {numero_tiros} tiros= {probabilidad_tiros_con_12}')
    
if __name__=='__main__':
    numero_tiros=int(input('Cuantas veces tiras del dado: '))
    numero_intentos=int(input('Cuantas veces correra la simulacion: '))
    
    main(numero_tiros, numero_intentos)