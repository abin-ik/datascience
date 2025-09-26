# ⿣ ravel() – Similar to flatten(), returns a view (faster)
# =======================================
# Q3: Given: arr = np.array([[1, 2, 3], [4, 5, 6]])
# → Use ravel() to convert it into 1D and change the 0th element of the result to 100
# → Check if the original array changes

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
c = a.ravel()
c[0]=100
print(c)
print(a)  # it chnages the orginal value