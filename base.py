import pandas as pd

tablasiembra = pd.read_csv('./Siembras.csv')

print(tablasiembra.to_string)

grupo1= tablasiembra[tablasiembra['Ciudad'].isin(['Andes','Barbosa','Caldas','Támesis','Yarumal'])]
print(grupo1)

grupo1=grupo1.to_html()
archivoTEXTO=open("grupo1.html","w",encoding="utf-8")
archivoTEXTO.write(grupo1)
archivoTEXTO.close()
