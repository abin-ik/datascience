# 2. Filtering + Mean
# Given an Array:
#arr = np.array([12, 45, 67, 89, 34, 22, 90, 100])
# → Select values between 40 and 90 (exclusive)
# → Calculate their mean


import numpy as np
a = np.array([12, 45, 67, 89, 34, 22, 90, 100])
mean = a[(a>40) & (a<90)]
print(mean)
print(np.sum(mean))