# ⿥ concatenate() – Join two or more arrays
# ===========================

import numpy as np
a = np.array([1,2,3])
b = np.array([5,6,7])
c = np.concatenate((a,b),axis=0)
print(c)