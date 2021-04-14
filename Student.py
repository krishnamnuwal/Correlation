##importing the required modules 
import numpy as np
import csv
import plotly.express as px
import plotly 

##function to add data to the lists
def dataSource(path):
    percentage=[]
    present=[]
    with open(path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        # fig=px.scatter(csv_reader,x="Marks In Percentage",y="Days Present")
        # plotly.offline.plot(fig)
        for row in csv_reader:
            percentage.append(float(row['Marks In Percentage']))
            present.append(float(row['Days Present']))
    return{"x":percentage,"y":present}

##function to find correlation
def findcorrelation(data):
    correlation=np.corrcoef(data["x"],data["y"])
    print("correlatiion between the marks of students N day he present=>",correlation[0,1])

##function for the implementation of other functions
def setup():
    path="./data1.csv"
    data=dataSource(path)

    findcorrelation(data)

setup()

##forming graph between marks and presnt of student
with open('data1.csv')as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    plotly.offline.plot(fig)