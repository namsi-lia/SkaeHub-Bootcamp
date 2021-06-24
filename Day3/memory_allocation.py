#code implementation of arrays to show memory allocation of the array

import numpy as np

lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input([]))
lst=np.append(lst,ele) 
     
print(lst)

# Size of array * size of one array element
print("The memory size of array is {} bytes".format(lst.size * lst.itemsize))