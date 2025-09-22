# 9. Create a (3, 3) identity matrix using NumPy and multiply it with a (3, 3) random integer matrix.
# → What do you observe?

import numpy as np
a=np.eye(3)
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(b)
print(a@b)

#output is same as the random integer matrix