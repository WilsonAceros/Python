import pandas as pd

#Creo el diccionario para exportar la informacion a un archivo.
#Tener en cuenta que se puede guardar siempre y cuando las listas tengan la misma longitud
informacion = {
    'actual':[10.362,-75.4,None],
    'zonawifi':[10.103,-74.918,0],
    'recorrido':[8500,'Bus',str(15)+' min']}
print(informacion)
print("Exportando archivo")
df = pd.DataFrame(informacion)
print(df)
#mode=a, funciona como un append dentro del archivo, no borra lo anterior
df.to_csv('FundamentosProgramacionMinTic/datos.csv', mode='a', index=False, header=False,sep=';',decimal=',')