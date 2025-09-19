import numpy as np
a=np.array([[1,2],[4,5]])
b=np.array([[4,5],[5,6]])
c=a@b
print(c)
print(a.dot(b))
print(np.matmul(a,b))