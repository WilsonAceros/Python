import math
import matplotlib.pyplot as plt

x=[]
y=[]

for i in range(0,360):
    angulo=math.radians(i)
    x.append(angulo)
    y.append(math.sin(angulo))

plt.plot(x,y)
plt.ylabel("Funcion seno")
plt.xlabel("Angulo en radianes")
plt.show()