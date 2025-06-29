

#a=[4,7,6]
#arr= numpy.array(a)
#print(type(arr))

#Arr= np.array(
   # [[3,6,5,7],
    # [3,7,8,4],
     #[4,7,7,3],
     #[3,4,6,6]]
#)
#print(Arr.mean())
import numpy as np
Arr=np.array([
    [ 2, 3, 4],
        [5, 6, 7],
        [13, 14, 15] 
 ])

print(Arr.sum(axis=1))
print(Arr.max(axis=0))
print(Arr[Arr>10])