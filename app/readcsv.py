#       python app/readcsv.py
import csv #modulo para leer csv
import matplotlib.pyplot as plt


def unaFuncion():
  print("lallaa")

def generateBarChart(dic):
  ListaItems=list(dic.items())
  itemsGraficos=ListaItems
  fig,ax=plt.subplots()
  for key,value in itemsGraficos:
    ax.bar(key[:4],value)
  plt.savefig('bar.png')
  plt.close()
with open("data.csv","r") as csvfile:
  datos=csv.reader(csvfile,delimiter=",")
  header=next(datos)
  listaDatos=[]
  pais=str()
  for i in datos:
    combinacion=zip(header,i)
    dic={llave:valor for llave,valor in combinacion}
    listaDatos.append(dic)


def generatePieChart(labels,values):
  print(labels)
  print(values)
  fig,ax=plt.subplots()
  ax.pie(values,labels=labels)
  plt.savefig('pie.png')
  plt.close()
  
  

def inicio():
  pais=input("ingresa un pais a buscar y a graficar: ")
  aux=0
  print("Buscando el pais: ", pais)
  for i in listaDatos:
    if listaDatos[aux]["Country/Territory"]==pais:
     print("el pais: ",listaDatos[aux]["Country/Territory"],       "fue encontrado")
  generateBarChart(listaDatos[aux])
  aux+=1

def transformToList():
  with open("data.csv", "r") as csvFile:
    datos=csv.reader(csvFile,delimiter=",")
    header=next(datos)
    lista=[]
    for i in datos:
      mix=zip(header,i)
      dic={key:value for key,value in mix }
      lista.append(dic)
    return lista

def capitalsDic(lista):
  poblacion=[]
  paises=[]
  for i in lista:
    paises.append(i["Country/Territory"])
    poblacion.append(i["Growth Rate"])
  dic=dict(zip(paises,poblacion))
  return dic
if __name__ =='__main__':
  inicio()




'''''
def readcsv(path):Argentina

  with open(path,"r") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    lista=[]
    header=next(reader)
    for i in reader:
      combinacion=zip(header,i)
      dic={llave:valor for llave,valor in combinacion}
      lista.append(dic)
    return lista
if __name__== "__main__":
  data=readcsv("./app/data.csv")
  print(data[0])
  '''