import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a[a>2])
print(a[(a>2) & (a<8)])
print(a[(a>5) | (a<8)])
print(~(a == 2))