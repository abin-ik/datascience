# 🔟 Mixed Challenge
# =======================================
# Q10: Given: arr = np.array([[1, 2, 2], [3, 4, 4], [5, 6, 6]])
# → Flatten it
# → Find the unique values
# → Reshape it into a (2, -1) shape
# → Transpose the reshaped result

import numpy as np
a = np.array([[1, 2, 2], [3, 4, 4], [5, 6, 6]])
b = np.unique(a).reshape(2,-1)
c = b.transpose()
print(c)