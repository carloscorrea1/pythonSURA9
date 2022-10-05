import pandas as pd


tablasiembra = pd.read_csv('./Siembras.csv')

print(tablasiembra.to_string)

bello= tablasiembra[(tablasiembra['Ciudad']=='Bello')&(tablasiembra['Vereda']=='Quitasol')]

print(bello)

bello=bello.to_html()
archivoTEXTO=open("bello.html","w",encoding="utf-8")
archivoTEXTO.write(bello)
archivoTEXTO.close()