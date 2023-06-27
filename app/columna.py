#       python app/columna.py

import readcsv as read
lista=read.transformToList()
capitales=read.capitalsDic(lista)
print(type(capitales))
keys=list(capitales.keys())
values=list(capitales.values())
read.generatePieChart(keys,values)