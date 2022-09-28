import pandas as pd

tablasiembra = pd.read_csv('./Siembras.csv')

print(tablasiembra.to_string)

medellin= tablasiembra[tablasiembra['Ciudad']=="Medellín"].sort_values('Arboles',ascending=False)
print(medellin)

medellin=medellin.to_html()
archivoTEXTO=open("medellin.html","w",encoding="utf-8")
archivoTEXTO.write(medellin)
archivoTEXTO.close()

