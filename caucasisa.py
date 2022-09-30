import pandas as pd

tablaSiembra = pd.read_csv('./Siembras.csv')

print(tablaSiembra.to_string)

caucasia = tablaSiembra[tablaSiembra['Ciudad']=="Caucasia"]

caucasiahtml=caucasia.to_html()
archivoTEXTO= open("Caucasia.html","w",encoding="utf-8")
archivoTEXTO.write(caucasiahtml)
archivoTEXTO.close()