
#x=[1,2,3,4,5]
#y=[10,20,30,40,50]
#plt.plot(x,y)
#plt.title("Basic line Graph")
#plt.xlabel("X-Axis")
#plt.ylabel("Y-Axis")
#plt.grid(True)
#plt.show()



#TASK 1

#labels=['Cooking','Sleeping','Reading','Working','Travelling']
#size=[50,60,20,20,10]
#plt.pie(size,labels=labels,autopct='%1.1f%%',colors=['blue','Pink','Green','Yellow','Red'])
#plt.title("Daily Activities")
#plt.show()

#import matplotlib.pyplot as plt

#Task 2 # Make 2x2 grid (4 plot)in a single figure

#x=[1,4,6,8,10]
#y1=[12,34,45,56,78]
#y2=[14,25,39,45,88]
#y3=[13,29,38,49,90]


#y4=['Cricket','Tennis','Football','Golf','Chess']
#EX=[0,0,0,0,0.2]
#size=[10,25,15,30,40]

#plt.subplot(3,2,1)
#plt.plot(x,y1,color='Red')
#plt.title("Line Plot")

#plt.subplot(3,2,2)
#plt.bar(x,y2,color="Green")
#plt.title("Bar Plot")

#plt.subplot(3,2,3)
#plt.scatter(x,y3,color='Purple')
#plt.title("Scatter Plot")
#plt.xlabel("X-Axis")
#plt.ylabel("Y-axis")

#plt.subplot(3,2,4)
#plt.pie(size,labels=y4,explode=EX,shadow=True)
#plt.title("Pie chart")

#plt.subplot(3,2,5)
#plt.tight_layout()
#plt.scatter(y4,y3,color='Purple')
#plt.plot(y4,y1,color='Red')
#plt.bar(y4,y2,color="Green",width=0.2)
#plt.title("All Chart")

#plt.show()


#Task 3 # placed age and salary in line plot after handle the missing values from data.csv

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('data.csv')
y=df["Salary"].mean()
x=df["Age"].mean()
x1=df["Age"]
y1=df["Salary"]
df.fillna({"Salary": y},inplace=True)
df.fillna({"Age": x},inplace=True)
plt.plot(x1,y1,color='Red',linestyle='--',marker='o')
plt.title("Line Graph")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()






