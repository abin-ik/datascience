# ⿥ concatenate() – Join two or more arrays
# ===========================

import numpy as np
a = np.array([[1,2,3],[4,3,2]])
b = np.array([[5,3,4],[1,2,3]])
c = np.concatenate((a,b),axis=0)
print(c)