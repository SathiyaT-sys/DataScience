

#a=[4,7,6]
#arr= numpy.array(a)
#print(type(arr))

# Task 1 # Create a 4*4 matrix and find mean of each row

#Arr= np.array(
   # [[3,6,5,7],
    # [3,7,8,4],
     #[4,7,7,3],
     #[3,4,6,6]]
#)
#print(Arr.mean(axis=1))

# Task 2 # Create a 3*3 matrix of random integer between 1 to 20 and perform 
#row wise sum
#column wise max
#replace all element greater than 10 with 0

import numpy as np
#Arr=np.array([
    #[ 2, 3, 4],
      #  [5, 6, 7],
       # [13, 14, 15] 
 #])

#print(Arr.sum(axis=1))
#print(Arr.max(axis=0))
#Arr[Arr>10]=0
#print(Arr)



matrix =np.random.randint(1,21,size=(3,3))
print(matrix)