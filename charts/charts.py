import matplotlib.pyplot as plt

def generate_pie_charts():
    labels =['A','B','C']
    values =[123,456,789]

    fig, ax= plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()