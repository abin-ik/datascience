# 9. Create a (4, 4) identity matrix using NumPy and multiply it with a (4, 4) random integer matrix.
# → What do you observe?

import numpy as np
a = np.array([[1,2,3,4],[4,5,6,7],[7,3,1,2],[0,2,5,3]])
b = np.eye(4)
print(a@b)


# the result is a