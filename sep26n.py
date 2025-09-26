# ⿤ transpose() / .T – Swap rows and columns
# =======================================
# Q4: Given: arr = np.array([[1, 2, 3], [4, 5, 6]])
# → Transpose this array and print both the original and transposed arrays
# → What is the new shape?

import numpy as np
a = ([[1,2,3,],[4,5,6]])
c = np.transpose(a)
print(a)
print(c)  
print(c.shape) #(3,2)