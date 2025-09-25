# 6. Count Filtered Elements
# Given an array of student scores:
#scores = np.array([34, 56, 78, 90, 45, 66, 89, 91, 50])
# → Filter scores above 60
# → Find how many such scores there are (count)
# → Find their average

import numpy as np
scores = np.array([34, 56, 78, 90, 45, 66, 89, 91, 50])
f = scores[scores>60]
print(f)
print(np.size(f))
print(np.average(f))