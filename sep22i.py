#10. Write a program to generate two (3, 3) matrices with random integers and compute:
#     - A @ B (matrix multiplication)
#     - A * B (element-wise multiplication)
# → Compare the outputs.

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[2,3,4],[5,6,7],[9,4,2]])
print(a@b)
print(a*b)

# a@b perfomes matrix multiplication using rows * column cocept
# a*b perfomes element wise multiplication whic directly multiplices each element