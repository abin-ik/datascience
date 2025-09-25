
# 7. Chained Conditions + Aggregation
#'''Create a random array of 15 integers between 1 and 100'''
# → Filter numbers either less than 20 OR greater than 80
# → Find their mean and sum

import numpy as np
a = np.random.randint(1,100,size=15)
print(a)
m = a[(a>20) & (a<80)]
print(m)
print(np.mean(m))
print(np.sum(a))