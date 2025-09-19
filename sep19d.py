import numpy as np
a=np.array([[2],
            [4],
            [6]])
b=np.array([[1,2,3]])
c=a@b
print(c)
print(np.shape(a))
print(np.shape(b))
print(np.matmul(a,b))


