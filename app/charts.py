#         python app/charts.py
import matplotlib.pyplot as plt

def generateBarChart():
  labels=['a','b','c']
  values=[100,20,90]
  
  fig,ax=plt.subplots()
  ax.bar(labels,values)
  plt.show()

def generatePieChart():
  labels=['a','b','c']
  values=[100,400,90]
  fig,ax=plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.show()
if __name__=='__main__':
  generateBarChart()

