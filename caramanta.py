import pandas as pd


tablasiembra = pd.read_csv('./Siembras.csv')

print(tablasiembra.to_string)

caramanta= tablasiembra[tablasiembra['Ciudad']=="Caramanta"]

print(caramanta)

caramanta=caramanta.to_html()
archivoTEXTO=open("caramanta.html","w",encoding="utf-8")
archivoTEXTO.write(caramanta)
archivoTEXTO.close()