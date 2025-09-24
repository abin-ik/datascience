# 10. Write a program to generate two (2, 3) and (3, 2) random integer matrices.
#     - Compute A @ B (valid matrix multiplication).
#     - Try B @ A (check the result shape).
# → Compare the two outputs.

import numpy as np
a = np.array([[1,2,3],[6,7,8]])
b = np.array([[1,2],[3,4],[5,6]])
print(a@b)
print(b@a)

# first it is (2,3) @ (3,2) so output is (2,2)
# second it is (3,2) @ (2,3) so output is (3,3)