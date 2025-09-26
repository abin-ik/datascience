# ⿥ concatenate() – Join two or more arrays
# =======================================
# Q5: Given: a = np.array([10, 20, 30]), b = np.array([40, 50, 60])
# → Concatenate these two arrays into one 1D array
# → Also try concatenating them column-wise as a 2D array

import numpy as np
a = np.array([10,20,30])
b = np.array([40,50,60])
print(np.concatenate((a,b)))
e = np.array([[10,20,30]])
f = np.array([[40,50,60]])
print(np.concatenate((e,f),axis= 1))