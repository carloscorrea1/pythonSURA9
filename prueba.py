import pandas as pd

tabla=pd.read_csv('./Siembras.csv')

##tabla estadisticas 

tablaEstadistica=tabla.describe()

#solo obtener medidas de la tabla estadistica (SOLO 1 FILA)

tablamedias=tablaEstadistica.loc[['mean']]

## solo obtener los datos de una columna

tablaMediaArboles=tablamedias['Arboles'].to_frame()

print(tablaMediaArboles)
