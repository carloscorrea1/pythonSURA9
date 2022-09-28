
import pandas as pd

tablaempleados = pd.read_csv('./empleados (2).csv')

print(tablaempleados.to_string)

tablaanalistas1= tablaempleados[tablaempleados['cargo']=="analista1"].head(50)

archivohtml=tablaanalistas1.to_html()
archivoTEXTO= open("datosanalista.html","w",encoding="utf-8")
archivoTEXTO.write(archivohtml)
archivoTEXTO.close()


tablaanalistas2=tablaempleados[tablaempleados['cargo']=="analista2"].head(10)

archivohtml2=tablaanalistas2.to_html()
archivoTEXTO=open("datosanalista2.html","w",encoding="utf-8")
archivoTEXTO.write(archivohtml2)
archivoTEXTO.close()


tablanalistafiltro=tablaempleados[(tablaempleados['salario']>5500000)&(tablaempleados["edad"]>30)]
print(tablanalistafiltro)

archivohtml3=tablanalistafiltro.to_html()
archivoTEXTO=open("datosfiltro.html","w",encoding="utf-8")
archivoTEXTO.write(archivohtml3)
archivoTEXTO.close()


























































print(tablaanalistas)

