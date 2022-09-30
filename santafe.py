from asyncore import read
import pandas as pd

tablaSiembra = pd.read_csv('./Siembras.csv')

print(tablaSiembra.to_string)

santafe = tablaSiembra[(tablaSiembra['Ciudad']=="Santa Fe de Antioquia")&(tablaSiembra['Arboles']>250)]

print(santafe)


santafe=santafe.to_html()
archivoTEXTO=open("santafe.html","w",encoding="utf-8")
archivoTEXTO.write(santafe)
archivoTEXTO.close()