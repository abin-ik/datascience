import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8]])
print(np.sum(a))
print(np.argmin(a)) # index position of minimum element
print(np.argmax(a)) # index posotion of mAXIMUM ELEMENT
print(np.max(a))  # maximum element 
print(np.min(a)) # minimum element
print(np.mean(a)) # to calculate mean value
print(np.sum(a,axis = 0))  # axis = 0 to add elements column wise
print(np.sum(a,axis = 1))  # axis = 1 to add elements row wise
print(np.prod(a)) # to add product of all elements
print(a.size)   # to find size of array 
print(np.size(a))  # to find size of array using numpy
print(np.random.randint(1,101,size=54))