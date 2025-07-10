
#x=[1,2,3,4,5]
#y=[10,20,30,40,50]
#plt.plot(x,y)
#plt.title("Basic line Graph")
#plt.xlabel("X-Axis")
#plt.ylabel("Y-Axis")
#plt.grid(True)
#plt.show()

import matplotlib.pyplot as plt

#TASK 1
labels=['Cooking','Sleeping','Reading','Working','Travelling']
size=[50,60,20,20,10]
plt.pie(size,labels=labels,autopct='%1.1f%%',colors=['blue','Pink','Green','Yellow','Red'])
plt.title("Daily Activities")
plt.show()

#Task 2


