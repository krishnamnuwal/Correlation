##importing the required modules 
import numpy as np 
import csv
import plotly.express as px
import plotly
##creating function which will add data to list
def dataSource(path):
     coffe_quantity=[]
     sleep=[]
     with open("data2.csv") as csv_file:
         csv_reader=csv.DictReader(csv_file)
         for row in csv_reader:
             coffe_quantity.append(float(row['Coffee in ml']))
             sleep.append(float(row["sleep in hours"]))
        
     return{"x":coffe_quantity ,"y":sleep}

##fucntion to find correlation
def findcorrelation(data):
    correlation=np.corrcoef(data["x"],data["y"])
    print("correlation between the coffee quantity and the amount they sleep=>",correlation[0,1])

##function for implementation of other functions 
def setup():
    path="./data2.csv"

    data=dataSource(path)
    findcorrelation(data)

setup()

##formming graph between coffee quantity and hours
with open('data2.csv')as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    plotly.offline.plot(fig)



