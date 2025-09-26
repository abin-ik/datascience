# ⿨ split() – Split an array into multiple parts (2D)
# =======================================
# Q8: Given: arr2D = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# → Split this 2D array into 2 equal parts along rows and print them


import numpy as np
a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
c = a.flatten()
print(np.split(a,4))