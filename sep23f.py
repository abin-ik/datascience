# 7. Verify the shape of the result when multiplying a (4, 3) matrix with a (3, 2) matrix

import numpy as np
a = np.array([[1,2,3],[3,4,5],[2,5,6],[6,3,2]])
b = np.array([[1,2],[1,2],[1,2]])
c=a@b
print(c.shape) 


#(4,3) @ (3,2) result be (4,2)