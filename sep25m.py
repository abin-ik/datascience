# 11. Create a 5×5 array of random integers between 1 and 100
# → Filter elements that are multiples of 5
# → Find their sum, mean, and total count

import numpy as np
a = np.random.randint(1,100,size = (5,5))
print(a)
c = a[a % 5 ==0]
print(c)
print(sum(c))
print(np.mean(a))
print(a.size)