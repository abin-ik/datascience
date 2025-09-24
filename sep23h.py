# 9. Create a (4, 4) identity matrix using NumPy and multiply it with a (4, 4) random integer matrix.
# → What do you observe?

import numpy as np
a = np.random.randint(1,10,(4,4))
b = np.eye(4)
print(a)
print(a@b)


# the result is a