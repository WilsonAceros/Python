import math

R=6372.795477598 #km Radio de la Tierra
lat1=10.3
long1=-75
lat2=10.127
long2=-74.95

distancia=[]

def calcular_distancia(lat1,lat2,long1,long2,R):
    a=(math.sin((lat2-lat1)/2))**2
    b=(math.cos(lat1))
    c=math.cos(lat2)
    d=(math.sin((long2-long1)/2))**2
    e=math.sqrt(a+b*c*d)
    distancia=2*R*math.asin(e)
    return distancia

distancia.append(calcular_distancia(lat1,long1,lat2,long2,R))
print(distancia)
min_distancia=min(distancia)