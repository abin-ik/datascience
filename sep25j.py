# 8. Aggregation on Condition
# Given a 2D array:
#matrix = np.array([[23, 45, 67],
#                   [89, 12, 34],
#                   [56, 78, 90]])
# → Filter all even numbers
# → Calculate their maximum and minimum


import numpy as np
matrix = np.array([[23, 45, 67],
                   [89, 12, 34],
                   [56, 78, 90]])
e = matrix[matrix %2 == 0]
print(e)
print(max(e))
print(min(e))