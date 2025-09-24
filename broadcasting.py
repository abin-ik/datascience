# broadcasting is streching scalar vectors too vectors for matching shapes

import numpy as np 
a = np.array([1,2,3,4])  # vector , shape -> (1,4)
b = 5   # scalar , no shape then it is converted into vector shape -> (1,4) -> ([5,5,5,5])
c = a+b 
print(c)

# extending
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a+b)


# 0D array -> scalar , D -> dimension
# 1D array -> vector
# 2D array -> matrix
# 3D,4D array -> Tensor

#scalar

import numpy as np 
a = np.array([1,2,3,4])  # vector , shape -> (1,4)
b = 5   # scalar , no shape then it is converted into vector shape -> (1,4) -> ([5,5,5,5])
c = a+b 
print(c)

# vector
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a+b)

# matrix

#Tensor
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
c = np.array([[100],
              [200],
              [300]])
d = A + c 
print(d)
