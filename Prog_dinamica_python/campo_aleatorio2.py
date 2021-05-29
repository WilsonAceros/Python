from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure,show

def caminata(campo,borracho,pasos):
    inicio=campo.obtener_coordenada(borracho)
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos,numero_intentos,tipo_borracho):
    borracho=tipo_borracho(nombre='David')
    origen=Coordenada(0,0)
    distancias=[]
    
    for _ in range(numero_intentos):
        campo=Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata=caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata,1))
    
    return distancias

def graficar(x,y):
    grafica=figure(title='Camino Aleatorio',x_axis_label='Pasos', y_axis_label='Distancia recorrida')
    grafica.line(x,y, legend='Distancia media')
    
    show(grafica)
    
def main(distancias_caminata, numero_intentos,tipo_borracho):
    distancias_media_por_caminata=[]
    for pasos in distancias_caminata:
        distancias=simular_caminata(pasos,numero_intentos,tipo_borracho)
        distancia_media=round(sum(distancias)/len(distancias),4)
        distancia_maxima=max(distancias)
        distancia_minima=min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos ')
        print(f'Media= {distancia_media}')
        print(f'Max= {distancia_maxima}')
        print(f'Min= {distancia_minima}')
    graficar(distancias_caminata,distancias_media_por_caminata)
        
if __name__=='__main__':
    distancias_caminata=[10,100,1000,10000]
    numero_intentos=100
    
    main(distancias_caminata, numero_intentos, BorrachoTradicional)