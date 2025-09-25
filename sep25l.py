# 10. Filter with Logical NOT (~)
# Given:
#arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# → Filter all elements NOT greater than 40
# → Compute the mean of these remaining elements

import numpy as np
r = np.array([10, 20, 30, 40, 50, 60, 70, 80])
a = r[~(r>40)]
print(a)
print(np.mean(r>40))