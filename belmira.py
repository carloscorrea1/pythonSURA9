import pandas as pd

tablasiembra = pd.read_csv('./Siembras.csv')

print(tablasiembra.to_string)

belmira= tablasiembra[tablasiembra['Vereda'].isin(['Rio Arriba','La Salazar'])]

print(belmira)

belmira=belmira.to_html()
archivoTEXTO=open("belmira.html","w",encoding="utf-8")
archivoTEXTO.write(belmira)
archivoTEXTO.close()