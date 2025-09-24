# A = np.array([[3, 1], [0, 2]])
# B = np.array([[4], [5]])
# → Perform matrix multiplication (A @ B) and explain the result.


import numpy as np
A = np.array([[3, 1], [0, 2]])
B = np.array([[4], [5]])
print(A@B)

# step 1 = 3*4 + 1*5 = 17
# step 2 = 0*4 + 2*5 = 10
