# 2. Given the 2D array:
# arr = np.array([[11, 12, 13, 14],
#                 [21, 22, 23, 24],
#                 [31, 32, 33, 34],
#                 [41, 42, 43, 44]])
# → Slice out the subarray [[22, 23], [32, 33]].

import numpy as np
a = np.array([[11, 12, 13, 14],
                [21, 22, 23, 24],
                [31, 32, 33, 34],
                [41, 42, 43, 44]])
print(a[1:3,1:3])