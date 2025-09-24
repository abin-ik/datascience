
# 3. From the array:
# arr = np.arange(1, 26).reshape(5, 5)
# → Extract the last column using slicing.

import numpy as np
a = np.arange(1,26).reshape(5,5)
print(a)
print(a[:5,4:5])