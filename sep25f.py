# 4. Filtering + Min
# Given an array:
#data = np.array([120, 56, 89, 45, 38, 99, 140, 110])
# → Filter all values less than 100
# → Find the minimum among the filtered values


import numpy as np
data = np.array([120, 56, 89, 45, 38, 99, 140, 110])
d = data[data<100]
print(d)
print(min(d))