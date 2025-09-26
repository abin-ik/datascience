# ⿦ vstack() and hstack() – Stack vertically or horizontally
# =======================================

import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,9,6,7])
print(np.vstack((a,b)))
print(np.hstack((a,b)))