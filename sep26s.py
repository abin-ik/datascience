# ⿩ unique() – Find unique elements in an array
# =======================================
# Q9: Given: arr = np.array([2, 4, 4, 2, 5, 5, 7, 7, 7])
# → Find all the unique values and how many times each occurs

import numpy as np
a = np.array([2, 4, 4, 2, 5, 5, 7, 7, 7])
b = np.unique(a,return_counts=True)


print(b)