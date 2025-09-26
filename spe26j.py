
# =======================================
# ⿡ reshape() – Change the shape of an array
# =======================================
# Q1: Given the array: arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# → Reshape it into a 4x2 2D array and print the result

import numpy as np
a = np.array([1,2,3,4,5,6,7,8])
b=a.reshape(4,2)
print(b)