
# 2D Example
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6]])
C = np.concatenate((A, B), axis=0)
print("concatenate 2D:\n", C)

