# ⿤ transpose() / .T – Swap rows and columns
# =======================================

import numpy as np
a = np.arange(1,11).reshape(2,5)
print(a)
b = a.transpose()
print(b)